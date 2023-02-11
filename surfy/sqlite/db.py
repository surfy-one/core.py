import os
import sqlite3
import re
from datetime import datetime
import json

'''

DB

'''

class DB:

	def __init__(self, file):
		self.file = file
		self.db = sqlite3.connect(file, check_same_thread=False)

	def query(self, query):
		cur = self.db.cursor()

		cur.execute(query)

		result = True
		if re.search('^SELECT', query):
			result = cur.fetchall()

		self.db.commit()

		return result

	def remove(self):
		os.remove(self.file)

	def table(self, name):
		return Table(self, name)

	'''
	
	Prepare Values

	'''

	def prepareValues(self, fields, valuesType='insert'):
		
		values = []

		escaped = True if valuesType != 'insert' else False

		for field in fields:
			value = self.prepareValue(field, escaped)

			if valuesType == 'set':
				
				values.append('`{}`={}'.format(field, value))

			elif valuesType == 'where':

				if value == 'NULL':
					values.append('`{}` IS NULL'.format(field));
				else:
					values.append('`{}`={}'.format(field, value));

			else:
				values.append(value);

		if valuesType == 'insert':
			return values;

		if valuesType == 'where':
			return ' AND '.join(values)

		return ', '.join(values)

	'''
	
	Prepare Value

	'''

	def prepareValue(self, v, escaped):

		if not v:
			v = 'NULL'
		elif not isinstance(v, int) and not isinstance(v, float):
			if v == 'CURRENT_TIME':
				v = 'DATE({})'.format(int(datetime.now().timestamp()))
			if type(v) is dict:
				v = json.dumps(v)

			if escaped:
				v = "'{}'".format(v)

		return str(v);


'''

	Table

'''

class Table:

	def __init__(self, sql, name):
		self.sql = sql
		self.name = name

	'''

	Find

	'''

	def find(self, match=False, options=False, one=False):
		fields = '*'
		query = []

		'''
		
			Selector

		'''

		if match and len(match):
			where = []

			for field in match:
				value = match[field]

				if '$like' in value:

					# LIKE
					where.append("`{}` LIKE '{}'".format(field, value['$like']))

				else:
					# Default

					if type(value) is dict:						
						value = "'{}'".format(json.dumps(value))

					elif isinstance(value, str):
						value = "'{}'".format(value)

					where.append('`{}`={}'.format(field, value));

			query.append('WHERE {}'.format(' AND '.join(where)));

		

		'''

			Create Options

		'''

		if options:
			
			if 'skip' in options:
				limit = options['limit'] if 'limit' in options else -1;
				query.append("LIMIT {} OFFSET {}".format(limit, options['skip']))
			elif 'limit' in options:
				query.append("LIMIT {}".format(options['limit']))


			if 'fields' in options and len(options['fields']):
				fields = "`{}`".format('`,`'.join(options['fields']))

		query.insert(0, "SELECT {} FROM `{}`".format(fields, self.name))
		query = ' '.join(query)

		cur = self.sql.db.cursor()
		cur.execute(query)
		result = cur.fetchall()

		columns = list(map(lambda x: x[0], cur.description))

		for idx, row in enumerate(result):
			data = {}
			
			for cX, col  in enumerate(columns):
				v = row[cX]

				if isinstance(v, str) and re.search(r'^DATE', v):
					v = re.sub(r'^DATE\((.+)\)$', r'\1', v)
					v = datetime.fromtimestamp(int(v))

				data[col] = v

			result[idx] = data
		
		if one:
			if len(result):
				result = result[0]
			else:
				result = False

		return result

	'''

	Find One

	'''

	def findOne(self, match=False, options=False):
		if not options:
			options = {}

		options['limit'] = 1

		return self.find(match, options, True)

	'''
	
	Insert Many

	'''

	def insert(self, rows, one=False):
		fields = set()
		values = []

		for row in rows:
			for field in row:
				fields.add(field)

		for row in rows:
			rowData = []
			for field in fields:
				v = row[field] if field in row else 'NULL'
				rowData.append(v)

			values.append(self.sql.prepareValues(rowData))

		query = 'INSERT OR IGNORE INTO `{}` ({}) VALUES({})'.format(self.name, ', '.join(fields), ', '.join(['?' for n in fields]))

		result = []
		cur = self.sql.db.cursor()

		for value in values:
			cur.execute(query, value);
			result.append(cur.lastrowid)
		
		# cur.commit()

		if one:
			return result[0]

		return result

	'''
	
	Insert One

	'''

	def insertOne(self, row):
		return self.insert([row], True)


