#!/usr/bin/env python3
"""
Main file to test the Cache class
"""
from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    print(f"Stored value: {value}, Retrieved value: {result}")
    assert result == value
