#!/usr/bin/env python3
"""
Module for caching and tracking web page access using Redis.
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def cache_with_expiration(expiration: int):
    """
    Decorator to cache the result of a function call with an expiration time.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            # Check if the result is already cached
            cached_page = r.get(f"cached:{url}")
            if cached_page:
                return cached_page.decode('utf-8')

            # If not cached, fetch the page
            result = func(url)

            # Cache the result with an expiration time
            r.setex(f"cached:{url}", expiration, result)
            return result

        return wrapper
    return decorator

@cache_with_expiration(10)
def get_page(url: str) -> str:
    """
    Fetch the content of a URL and cache it. Track the number of accesses.
    """
    # Increment the access count
    r.incr(f"count:{url}")

    # Fetch the page content
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
    print("Fetching URL...")
    print(get_page(url))
    print(f"URL accessed {r.get(f'count:{url}').decode('utf-8')} times")
