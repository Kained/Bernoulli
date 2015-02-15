def clean(text):

	text = text.lower()

	dictionary = {"andover": "n over", 
	"roots": "root", 
	"square root": "squareroot",
	"end": "n",
	"are": "r",
	"each": "e",
	"tx": "dx",
	"girl": "integral"}

	for key in dictionary.keys():
		text = text.replace(key, dictionary[key])

	return text