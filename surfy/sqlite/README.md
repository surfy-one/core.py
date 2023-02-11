# SQLite

<br/>

## Installation
```
pip3 install Surfy.SQLite
```

## Usage

```python

from sqlite import DB

db = DB('PATH_TO_FILE')

```
<br/>

## Methods


### .query(query)

```python
result = db.query('''CREATE TABLE IF NOT EXISTS test_table
	(id INTEGER PRIMARY KEY AUTOINCREMENT,
	createTime TEXT,
	data TEXT COLLATE NOCASE,
	extradata TEXT,
	counter INTEGER,
	realNumber REAL,
	object TEXT,
	array TEXT);''')

```
<br/>

### .table(table_name)

```python

testTable = db.table('test_table')

```
<br/>

### table.insertOne(row)
Inserts a single row into a table

```python

insertedID = testTable.insertOne({
	'createTime': 'CURRENT_TIME',
	'data': 'Some Data 1',
	'extradata': 'Some Extra Data',
	'counter': 2,
	'realNumber': 2.52,
	'object': {
		'field': 'value'
	},
	'array': [1,2,3]
})

```
<br/>

### table.insert(rows)
Inserts data into a table

```python

insertedIDs = testTable.insert(
	[
		{
			'createTime': 'CURRENT_TIME', 'data': 'Some Data 1'
		},
		{
			'createTime': 'CURRENT_TIME', 'data': 'Some Data 2'
		},
		{
			'createTime': 'CURRENT_TIME', 'data': 'Some Data 3'
		}
	]
)

```
<br/>

### table.findOne(match, options)
Finds one row in a table

```python

match = {
	'data': 'Some Data 2'
}

options = {
	'fields': ['id', 'currentTime', 'data']
}

result = testTable.findOne(match, options)

'''

result {
	'id': 3,
	'currentTime': datetime.datetime(2023, 2, 10, 21, 2, 20),
	'data': 'Some Data 2'
}

'''

```
<br/>

### table.find(match, options)
Finds matches in a table

```python

match = {
	'data': {
		'$like': 'Some Data %'
	}
}

options = {
	'fields': ['id', 'currentTime', 'data'],
	'skip': 2,
	'limit': 1
}

result = testTable.find(match, options)

'''

result [
	{
		'id': 3,
		'currentTime': datetime.datetime(2023, 2, 10, 21, 2, 20),
		'data': 'Some Data 2'
	}
]

'''

```

<br />
<br />

## MIT License

Alexander Yermolenko • [surfy.one](https://surfy.one)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.