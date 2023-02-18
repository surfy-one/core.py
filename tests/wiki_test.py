'''

Wiki tests

'''

from surfy.wiki import Wiki

def test():
	print('\n\n##### Starting Wiki Test #####\n\n')
	print('Wiki Class:', Wiki)

	wiki = Wiki()
	page = wiki.page('Eiffel Tower')
	# page = wiki.page('1900 Summer Olympics')
	print(page)
	if not page:
		print('Page Not Found')
		return False

	print(f'\nID: {page.id}')
	print(f'\nTitle: {page.title}')
	print(f'\nContent: {page.content[:250]}...')
	print(f'\nLinks: {page.links[:10]}...')
	print(f'\nSummary: {page.summary}')