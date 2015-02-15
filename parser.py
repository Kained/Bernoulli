import sys
import re


string = sys.argv[1]
print string
prepositions = (["of","from","to","over"])
regex = "(of)|(from)|(to)|(over)" # shut up

for s in filter(None, re.split(regex, string)):
	print s

