'''

Surfy Words Test

'''

from surfy.words import Words

def test():
	w = Words()
	corpus = 'Surfy is an ecosystem of hardware and software solutions based on artificial intelligence, combining technologies which synthesise basic human senses - vision, hearing and speech, text, geo-positioning, search for new information and intelligence, all of which can be used to increase efficiency and broaden human potential. Surfy is an ecosystem of software. Digity content: 1987, 1ml raw bites, 8,39239, 2937. Redundant Content: Surfy is an ecosystem of software. Surfy is an ecosystem of hardware. Surfy is an ecosystem of hardware. Surfy is an ecosystem of software. Surfy is an ecosystem of hardware.'
	
	print('Digity Index:', w.digity(corpus))
	print('Redundancy Index:', w.redundancy(corpus))
	print(w.remove_punct(corpus))