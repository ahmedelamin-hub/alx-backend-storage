#!/usr/bin/env python3
"""
11-schools_by_topic.py
This script contains a function to find schools with a specific topic in their topics list.
"""

from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """
    Retrieve a list of schools where the topic is included in their topics.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        topic (str): The topic to search for in the school's topics list.

    Returns:
        List[Dict]: A list of dictionaries representing the schools that have the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
