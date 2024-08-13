#!/usr/bin/env python3
""" 101-students """

from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns a list of all students sorted by average score in descending order.

    :param mongo_collection: pymongo collection object
    :return: list of dictionaries with student data and averageScore
    """
    # Aggregate pipeline
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    
    # Run aggregation pipeline
    students = list(mongo_collection.aggregate(pipeline))
    
    return students
