#!/usr/bin/env python3
"""
10-update_topics.py
This script contains a function to update the 'topics' field of documents in a MongoDB
collection based on the school name.
"""

from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Update the 'topics' field of all documents in the collection that match the given school name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school to update.
        topics (List[str]): A list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
