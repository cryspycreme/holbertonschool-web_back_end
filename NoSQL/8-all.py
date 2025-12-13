#!/usr/bin/env python3
"""List all documents in Python"""

def list_all(mongo_collection):
	return list(mongo_collection.find())

if __name__ == '__main__':
	list_all(mongo_collection)