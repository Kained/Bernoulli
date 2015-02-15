def clean(text):
	text = text.lower()

	dictionary = {"andover": "n over", 
	"roots": "root", 
	"square root": "squareroot",
	"end": "n",
	" are ": "r" ,
	"each": "e",
	"tx": "dx",
	"girl": "integral",
	"song": "sum",
	"son": "sum",
	"x-square": "x squared",
	"x-squared": "x squared",
	"love": "of",
	"and": "n", "capitalize":"capital I",
   "factor":"vector",".":" dot",
   "me":"mu","psy ":"psi ","psychology get":"psi conjugate",
   "age":"h","@":"at","goes to":"approaches", 
   "divided by":"over", "roh":"rho", "road": "rho", "dvd":"dv",
   "eat":"e","sign":"sine","effects":"of x","e2":"e to", "art": "r", "my": "y"}

	dictionary2 = {"square root": "squareroot", "psychology get":"psi conjugate"}

	pairs = []

	for key in dictionary2.keys():
		try:
			i = text.index(" " + key)
		except:
			try:
				j = text.index(key + " ")
			except:
				pass
			else:
				pairs.append([key, dictionary[key]])
				text = text.replace(key + " ", dictionary[key] + " ")
				text = text.replace(" " + key, " " + dictionary[key])
		else:
			pairs.append([key, dictionary[key]])
			text = text.replace(key + " ", dictionary[key] + " ")
			text = text.replace(" " + key, " " + dictionary[key])


	for key in dictionary.keys():
		try:
			i = text.index(" " + key)
		except:
			try:
				j = text.index(key + " ")
			except:
				pass
			else:
				pairs.append([key, dictionary[key]])
				text = text.replace(key + " ", dictionary[key] + " ")
				text = text.replace(" " + key, " " + dictionary[key])
		else:
			pairs.append([key, dictionary[key]])
			text = text.replace(key + " ", dictionary[key] + " ")
			text = text.replace(" " + key, " " + dictionary[key])

	return [text, pairs]
