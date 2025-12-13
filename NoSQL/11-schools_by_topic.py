#!/usr/bin/env python3
"""Return schools by specified topic"""

def schools_by_topic(mongo_collection, topic):
	"""Return schools with topic"""
	query_filter = {'topics': { '$regex': topic}}
	schools = list(mongo_collection.find(query_filter))
	return schools

if __name__ == '__main__':
	schools_by_topic()