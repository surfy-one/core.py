from surfy.sqlite import SQLite

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

print('Create Table: {}'.format(result))

# Table
testTable = db.table('test_table')
print('Test Table: {}'.format(testTable))

# Insert One
insertedID = testTable.insertOne({
	'data': 'Some Data 1',
	'extradata': 'Some Extra Data',
	'counter': 2,
	'realNumber': 2.52,
	'object': {
		'field': 'value'
	},
	'array': [1,2,3]
})

print('Inserted ID: {}'.format(insertedID))

# Insert
insertedIDs = testTable.insert([
	{ 'data': 'Some Data 2' },
	{ 'data': 'Some Data 3' },
	{ 'data': 'Some Data 4' },
	{ 'data': 'Some Data 5', 'extradata': 'CURRENT_TIME' },
])

print('Inserted IDs: {}'.format(insertedIDs))

# Find One
result = testTable.findOne({ 'data': 'Some Data 5' })
print('Find One:',result)

# Find
results = testTable.find({ 'data': { '$like': 'Some Data%' } })
print('Find: ', results)

# Remove
db.remove()