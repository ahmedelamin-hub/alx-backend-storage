#!/usr/bin/env python3
"""
9-insert_school.py
This script contains a function to insert a new document into a MongoDB collection
based on keyword arguments and returns the new document's _id.
"""

from pymongo.collection import Collection
from typing import Any

def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """
    Insert a new document into the MongoDB collection with the given keyword arguments.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        **kwargs (Any): The fields and values to be inserted into the document.

    Returns:
        str: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
