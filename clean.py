def clean(text):

	text = text.lower()

	dictionary = {"andover": "n over", 
	"roots": "root", 
	"square root": "squareroot",
	"end": "n",
	"are": "r",
	"each": "e"}

	text = text.replace("andover", "n over")
	text = text.replace("roots", "root")
	text = text.replace("square root", "squareroot")

	return text