'''

Surfy SQLite Test

'''

from surfy.sqlite import SQLite

def test():

	'''
	
	SQL Test

	'''

	print('\n\n##### Starting SQLite Test #####\n\n')

	print(f'SQLite Class: {SQLite}')

	# Runs Test

	db = SQLite('test_db')
	print('Created DB')

	# Create Table
	result = db.query('''CREATE TABLE IF NOT EXISTS test_table
				(id INTEGER PRIMARY KEY AUTOINCREMENT,
				data TEXT COLLATE NOCASE,
				extradata TEXT,
				counter INTEGER,
				realNumber REAL,
				object TEXT,
				array TEXT);''')

	print(f'Create Table: {result}')

	# Table
	test_table = db.table('test_table')
	print(f'Test Table: {test_table}')

	# Insert One
	inserted_id = test_table.insert_one({
		'data': 'Some Data 1',
		'extradata': 'Some Extra Data',
		'counter': 2,
		'realNumber': 2.52,
		'object': {
			'field': 'value'
		},
		'array': [1,2,3]
	})

	print(f'Inserted ID: {inserted_id}')

	# Insert
	inserted_ids = test_table.insert([
		{ 'data': 'Some Data 2' },
		{ 'data': 'Some Data 3' },
		{ 'data': 'Some Data 4' },
		{ 'data': 'Some Data 5', 'extradata': 'CURRENT_TIME' },
	])

	print(f'Inserted IDs: {inserted_ids}')

	# Find One
	result = test_table.find_one({ 'data': 'Some Data 5' })
	print('Find One:',result)

	# Find
	results = test_table.find({ 'data': { '$like': 'Some Data%' } })
	print('Find: ', results)

	# Update
	result = test_table.update_one({'data': 'Some Data 2'}, {'data': 'Updated Data'})
	print(f'Update result: {result}')

	result = test_table.find_one({'data': 'Updated Data'})
	print(f'Updated row: {result}')

	result = test_table.count()
	print(f'Documents Count: {result}')

	# Remove
	db.remove()
