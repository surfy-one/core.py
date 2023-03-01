'''

Wikipedia

'''

import json
from urllib.parse import quote as encode
import requests

class Wiki:

	'''

	Create Wikipedia Global

	'''

	def __init__(self, options=False):

		'''

		Initialisation

		'''

		if not options:
			options = {
				'lang': 'en',
				'redirect': 1
			}

		self.options = options

		if 'lang' not in options:
			self.options['lang'] = 'en'

		if 'redirect' not in options:
			self.options['redirect'] = 1

		self.headers = {}
		if 'ua' in options:
			self.headers['User-Agent'] = options['ua']


	def set_lang(self, lang):

		'''

		Set Global Lang

		'''

		self.options['lang'] = lang

	def page(self, addr, lang=False):

		'''

		Get Page Instance

		'''

		if not lang:
			lang = self.options['lang']

		if isinstance(addr, int):

			# Extract Title From ID

			url = f"http://{lang}.wikipedia.org/w/api.php?action=query&pageids={addr}&format=json"
			url = f"http://{lang}.wikipedia.org/w/api.php?action=query&pageids=1936&format=json"

			x = requests.get(url, headers=self.headers, timeout=30)
			if x.status_code != 200:
				return Page({'status_code': x.status_code}, False)

			data = json.loads(x.text)
			if 'pages' not in data or not data['pages']:
				return Page({'status_code': 404}, False)

			if str(addr) not in data['pages']:
				return Page({'status_code': 404}, False)

			addr = data['pages'][str(addr)]['title']

		addr = str(addr)

		# Get Page

		url = f"https://{lang}.wikipedia.org/w/rest.php/v1/page/{encode(addr)}/bare"
		x = requests.get(url, headers=self.headers, timeout=30)
		if x.status_code != 200:
			return Page({'status_code': x.status_code}, False)
		data = json.loads(x.text)

		if 'httpCode' in data and data['httpCode'] == 404:
			return Page({'status_code': 404}, False)

		page_options = self.options
		page_options['lang'] = lang
		return Page(data, page_options)


class Page:

	'''
	
	Create Wiki Page Instance

	'''

	def __init__(self, data, options):

		'''

		Initialisation

		'''

		if 'status_code' in data:
			self.status_code = data['status_code']
		else:
			self.options = options
			self.data = data
			self.id = data['id']
			self.title = str(data['title'])
			self.key = data['key']
			self.html_url = data['html_url']
			self.redirected = False
			self.status_code = 200

			self.headers = {}
			if 'ua' in options:
				self.headers['User-Agent'] = options['ua']

			self.get_content()

			self.summary = self.get_summary()

	def get_content(self):

		'''

		Get Cotent and Links

		'''

		url = f"https://{self.options['lang']}.wikipedia.org/w/api.php?action=query&format=json&titles={encode(self.title)}&prop=info|extracts|links&explaintext&inprop=url&redirects=1"

		# Request API
		x = requests.get(url, headers=self.headers, timeout=30)
		if x.status_code != 200:
			return False
		data = json.loads(x.text)

		# Page Not Found
		if '-1' in data['query']['pages']:
			return False

		if 'redirects' in data['query']:
			self.redirected = True
			self.redirects = data['query']['redirects']

		pages = data['query']['pages']
		self.id = list(pages.keys())[0]
		page = data['query']['pages'][self.id]
		self.title = page['title']

		# Get Plain Text Content

		self.content = page['extract']

		# Get Links

		links = []

		if 'links' in page:
			for link in page['links']:
				links.append(link['title'])
		self.links = links

		self.url = page['fullurl']

		return True

	def get_summary(self):

		'''

		Get Summary

		'''

		url = f"https://{self.options['lang']}.wikipedia.org/w/api.php?format=json&action=query&redirects=1&titles={encode(self.title)}&prop=extracts&explaintext&exintro"

		# Request API
		x = requests.get(url, headers=self.headers, timeout=30)
		if x.status_code != 200:
			return False
		data = json.loads(x.text)

		# Page Not Found
		if '-1' in data['query']['pages']:
			return False

		pages = data['query']['pages']
		self.id = list(pages.keys())[0]
		page = data['query']['pages'][self.id]

		# Get Plain Text Summary

		return page['extract']
