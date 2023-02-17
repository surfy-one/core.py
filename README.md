# Surfy Core Ecosystem for Python

This repository contains all the libraries for successful working with Surfy Ecosystem in a Python environment.

![Surfy](https://github.com/surfy-one/core.py/blob/main/imgs/surfy.cover.jpg?raw=true "Surfy")


## Installation

```
pip3 install surfy
```

## Libraries

- [SQLite](#sqlite)
- [Words](#words)

<br/>

# SQLite

### Usage
```python

from surfy.sqlite import SQLite
db = SQLite('PATH_TO_FILE')

```

### Query
```python

result = db.query('''CREATE TABLE IF NOT EXISTS test_table
	(id INTEGER PRIMARY KEY AUTOINCREMENT,
	createTime TEXT COLLATE NOCASE,
	data TEXT COLLATE NOCASE,
	extradata TEXT,
	counter INTEGER,
	realNumber REAL,
	object TEXT,
	array TEXT);''')

```
<br/>

### .remove()
```python

db.remove()

```
<br/>

### .table(table_name)
```python

table = db.table('test_table')

```
<br/>

### table.insert_one(row)
```python

row = {
	'createTime': 'CURRENT_TIME',
	'data': 'Some Data 1',
	'extradata': 'Some Extra Data',
	'counter': 2,
	'realNumber': 2.52,
	'object': {
		'field': 'value'
	},
	'array': [1,2,3]
}

inserted_id = table.insert_one(row) # Integer

```
<br/>

### table.insert(rows)
```python

rows = [
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

inserted_ids = table.insert(rows) # List of Integers

```
<br/>

### table.find_one(match, options)
```python

match = {
	'data': 'Some Data 2'
}

options = {
	'fields': ['id', 'currentTime', 'data']
}

result = testTable.find_one(match, options)

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
<br/>

### table.update_one(match, update, options)
Updates first matched record

```python

match = {
	'data': {
		'$like': 'Some Data %'
	}
}

update = {
	'currentTime': 'CURRENT_TIME'
}

options = {
	'skip': 2,
	'limit': 1
}

result = testTable.update_one(match, update, options)

```
<br/>

### table.update(match, update, options)
Updates all matched records

```python

match = {
	'data': {
		'$like': 'Some Data %'
	}
}

update = {
	'currentTime': 'CURRENT_TIME'
}

options = {
	'skip': 2
}

result = testTable.update(match, update, options)

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