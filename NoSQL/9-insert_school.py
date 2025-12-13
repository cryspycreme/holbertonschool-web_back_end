#!/usr/bin/env python3
"""Insert a document in Python"""

def insert_school(mongo_collection, **kwargs):
	"""Insert a document in Python"""
	added_data = mongo_collection.insert_one(kwargs)
	return added_data.inserted_id
	
if __name__ == '__main__':
	insert_school()