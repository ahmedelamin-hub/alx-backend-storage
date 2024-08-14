#!/usr/bin/env python3
""" Main file """

from exercise import Cache, replay

cache = Cache()

# Test storing and retrieving data
data = b"hello"
key = cache.store(data)
print(key)
print(cache.get(key))  # Should print b'hello'

# Test counting method calls
cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Should print b'2' or the correct count

# Test call history
replay(cache.store)  # Should display the history of calls
