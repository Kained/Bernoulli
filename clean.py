def clean(text):

	text = text.lower()

	dictionary = {"andover": "n over", 
	"roots": "root", 
	"square root": "squareroot",
	"end": "n",
	"are": "r",
	"each": "e",
	"tx": "dx",
	"girl": "integral",
	"song": "sum",
	"son": "sum",
	"x-squared": "x squared",
	"love": "of",
	"and": "n", "capitalize":"capital I",
   "factor":"vector","ed":"e",".":" dot",
   "me":"mu","psy ":"psi ","psychology get":"psi conjugate","":""}

	pairs = []

	for key in dictionary.keys():
		try:
			i = text.index(" " + key)
		except:
			try:
				j = text.index(key + " ")
			except:
				pass
			else:
				continue
		else:
			pairs.append([key, dictionary[key]])
			text = text.replace(key + " ", dictionary[key] + " ")
			text = text.replace(" " + key, " " + dictionary[key])

	return [text, pairs]
