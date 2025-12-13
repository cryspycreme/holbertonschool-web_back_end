#!/usr/bin/env python3
"""Change school topics"""

def update_topics(mongo_collection, name, topics):
	"""Updates school topics"""
	query_filter = {'name': name}
	update_operation = {'$set': {'topics': topics}}
	mongo_collection.update_many(query_filter, update_operation)

if __name__ == '__main__':
	update_topics()