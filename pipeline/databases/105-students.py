#!/usr/bin/env python3
"""
Module to return students sorted by average score from a MongoDB collection.
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    Each document returned includes the averageScore field.
    """
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
    return list(mongo_collection.aggregate(pipeline))
