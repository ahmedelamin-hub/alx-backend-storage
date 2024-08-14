#!/usr/bin/env python3
"""
Cache class for interacting with Redis, with additional functionality for counting
calls, storing call history, and retrieving the history of calls.
"""

import redis
from typing import Callable, Union, Optional
from functools import wraps
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the counter each time the method is called
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the inputs in the Redis list
        self._redis.rpush(input_key, str(args))

        # Execute the original method and store the output
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    
    return wrapper


class Cache:
    """
    Cache class that uses Redis to store and retrieve data.
    Implements methods to count method calls and store call history.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis and return the key.
        Generates a random key and stores the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and apply an optional conversion function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from Redis.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from Redis.
        """
        return self.get(key, fn=int)


def replay(method: Callable):
    """
    Display the history of calls to a method.
    """
    redis_instance = method.__self__._redis
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}")
