'''

Surfy Tests

'''

#pylint: disable=wrong-import-position

import sys
sys.path.append(sys.path[0]+'/..')

#pylint: enable=wrong-import-position

from sqlite_test import sqlite_test
from surfy import Surfy
from surfy.sqlite import SQLite


def go():

	'''
	
	Runs tests

	'''

	print(Surfy)
	print(SQLite)

	# Runs Tests

	sqlite_test()

if __name__ == '__main__':
	go()
