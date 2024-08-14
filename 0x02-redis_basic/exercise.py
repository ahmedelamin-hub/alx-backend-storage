#!/usr/bin/env python3
"""
This module defines a Cache class for interacting with Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class that interfaces with Redis to store and retrieve data.
    """

    def __init__(self):
        """
        Initialize the Cache instance and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
