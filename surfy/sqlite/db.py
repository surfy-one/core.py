'''

SQLite

'''

# Import Libs
import os
import sqlite3
import re
from datetime import datetime
import json


class SQLite:

	'''

	Create DB

	'''

	def __init__(self, file) :
		self.file = file
		self.db = sqlite3.connect(file, check_same_thread=False)

	def query(self, query):

		'''

		Simple Query


		'''

		cur = self.db.cursor()

		cur.execute(query)

		result = True
		if re.search('^SELECT', query):
			result = cur.fetchall()

		self.db.commit()

		return result

	def remove(self):

		'''

		Remove DB

		'''

		os.remove(self.file)

	def table(self, name):

		'''

		Returns Table Instance

		'''

		return Table(self, name)

	def prepare_values(self, fields, values_type='insert'):

		'''

		Prepare Values

		'''

		values = []

		escaped = values_type != 'insert'

		for field in fields:
			if values_type != 'insert':
				value = fields[field]
			else:
				value = field

			value = self.prepare_value(value, escaped)

			if values_type == 'set':

				values.append(f'`{field}`={value}')

			elif values_type == 'where':

				if value == 'NULL':
					values.append(f'`{field}` IS NULL')
				else:
					values.append(f'`{field}`={value}')

			else:
				values.append(value)

		if values_type == 'insert':
			return values

		if values_type == 'where':
			return ' AND '.join(values)

		return ', '.join(values)

	def prepare_value(self, value, escaped):

		'''

		Prepare Value

		'''

		if isinstance(value, bool):
			value = 1 if value else 0
		elif not value:
			value = 'NULL'
		elif not isinstance(value, int) and not isinstance(value, float):
			if value == 'CURRENT_TIME':
				value = f'DATE({int(datetime.now().timestamp())})'
			if isinstance(value, dict):
				value = json.dumps(value)

			if escaped:
				value = f"'{value}'"

		return str(value)

	def get_json(self, value):

		'''

		Extract JSON

		'''

		if not isinstance(value, str):
			return value

		try:
			value = json.loads(value)
		except ValueError:
			return value

		return value

class Table:

	'''

	Table Class

	'''

	def __init__(self, sql, name):
		self.sql = sql
		self.name = name

	def find(self, match=False, options=False, one=False):

		'''
	
		Find in Table

		'''

		fields = '*'
		query = []

		# Selector

		if match and len(match):
			where = []

			for field in match:
				value = match[field]

				if isinstance(value, dict) and '$like' in value:

					# LIKE
					where.append(f"`{field}` LIKE '{value['$like']}'")

				else:
					# Default

					if isinstance(value, dict):
						value = f"'{json.dumps(value)}'"

					elif isinstance(value, str):
						value = f"'{value}'"

					elif isinstance(value, bool):
						value = 1 if value else 0

					where.append(f'`{field}`={value}')

			query.append(f"WHERE {' AND '.join(where)}")

		# Create Options

		if options:

			if 'skip' in options:
				limit = options['limit'] if 'limit' in options else -1
				query.append(f"LIMIT {limit} OFFSET {options['skip']}")
			elif 'limit' in options:
				query.append(f"LIMIT {options['limit']}")


			if 'fields' in options and len(options['fields']):
				fields = f"`{'`,`'.join(options['fields'])}`"

		query.insert(0, f"SELECT {fields} FROM `{self.name}`")
		query = ' '.join(query)

		cur = self.sql.db.cursor()
		cur.execute(query)
		result = cur.fetchall()

		columns = list(map(lambda x: x[0], cur.description))

		for idx, row in enumerate(result):
			data = {}

			for cid, col  in enumerate(columns):
				value = row[cid]

				if isinstance(value, str) and re.search(r'^DATE', value):

					value = re.sub(r'^DATE\((.+)\)$', r'\1', value)
					value = datetime.fromtimestamp(int(value))

				else:
					value = self.sql.get_json(value)

				data[col] = value

			result[idx] = data

		if one:
			if len(result):
				result = result[0]
			else:
				result = False

		return result

	def find_one(self, match=False, options=False):

		'''

		Find One in Table

		'''

		if not options:
			options = {}

		options['limit'] = 1

		return self.find(match, options, True)

	def insert(self, rows, one=False):

		'''
		
		Insert Many Into Table

		'''

		fields = set()
		values = []

		for row in rows:
			for field in row:
				fields.add(field)

		for row in rows:
			row_data = []
			for field in fields:
				value = row[field] if field in row else 'NULL'
				row_data.append(value)

			values.append(self.sql.prepare_values(row_data))

		placeholders = ', '.join(['?' for n in fields])
		fields = ', '.join(fields)
		query = f"INSERT OR IGNORE INTO `{self.name}` ({fields}) VALUES({placeholders})"

		result = []
		cur = self.sql.db.cursor()

		for value in values:
			cur.execute(query, value)
			result.append(cur.lastrowid)

		self.sql.db.commit()

		if one:
			return result[0]

		return result

	def insert_one(self, row):

		'''
		
		Insert One Into Table

		'''

		return self.insert([row], True)

	def update(self, match, update, options=False):

		'''

		Update Row in the Table

		'''

		if not update:
			return False

		query = []

		# Selector

		if match and len(match):
			where = []

			for field in match:
				value = match[field]

				if isinstance(value, dict) and '$like' in value:

					# LIKE
					where.append(f"`{field}` LIKE '{value['$like']}'")

				else:
					# Default

					if isinstance(value, dict):
						value = f"'{json.dumps(value)}'"

					elif isinstance(value, str):
						value = f"'{value}'"

					where.append(f'`{field}`={value}')

			query.append(f"WHERE {' AND '.join(where)}")

		# Create Options

		if options:

			if 'skip' in options:
				limit = options['limit'] if 'limit' in options else -1
				query.append(f"LIMIT {limit} OFFSET {options['skip']}")
			elif 'limit' in options:
				query.append(f"LIMIT {options['limit']}")


		# Update
		updates = self.sql.prepare_values(update, 'set')

		query.insert(0, f"UPDATE `{self.name}` SET {updates}")
		query = ' '.join(query)

		cur = self.sql.db.cursor()
		cur.execute(query)

		self.sql.db.commit()

		return True

	def update_one(self, match, update=False, options=False):

		'''

		Update One Row of the Table

		'''

		if not update:
			return False

		if not options:
			options = {}

		options['limit'] = 1

		return self.update(match, update, options)
