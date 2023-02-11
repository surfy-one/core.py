'''

Surfy

'''

class Surfy:

	'''
	
	Global Surfy

	'''

	# Initialisation
	def __init__(self, options):
		self.options = options

	def help(self):

		'''

			Get Surfy Help

		'''

		helper = {
			'SQLite': 'Usefull lib for work with sqlite'
		}

		print(helper)
		