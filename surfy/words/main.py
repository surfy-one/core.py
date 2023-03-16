import re
import nltk
# import spacy
# self.ner = spacy.load('en_core_web_sm')

class Words:

	# def __init__(self,):
		

	def remove_punct(self, corpus):

		'''

		Remove Punctuation
		
		'''

		return re.sub(r'[^\w\s]', '', corpus)

	def digity(self, corpus):
		
		'''
		
		Ratio between digits and all words

		'''

		corpus = self.remove_punct(corpus)
		words = corpus.split()
		print(words)
		doc = [i for i in words if not i.isdigit()]

		length = len(words);
		index = (length - len(doc)) / length

		return index

	def redundancy(self, corpus):

		'''
	
		Determination of Text Redundancy

		'''

		sentences = nltk.sent_tokenize(corpus)

		grams = []
		for idx, sent in enumerate(sentences):
			sent = self.remove_punct(sent.lower())
			s = list(nltk.ngrams(sent.split(),5))
			grams += s

		if not grams:
			return 0

		return 1 - len(set(grams)) / len(grams)