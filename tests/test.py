'''

Surfy Tests

'''

#pylint: disable=wrong-import-position

import sys
sys.path.append(sys.path[0]+'/..')

#pylint: enable=wrong-import-position

from sqlite_test import test as sqlite_test
from wiki_test import test as wiki_test
from surfy import Surfy


def go():

	'''
	
	Runs tests

	'''

	print('Surfy Class:', Surfy)

	# Runs Tests

	sqlite_test()
	wiki_test()

if __name__ == '__main__':
	go()
