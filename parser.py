import sys
import re

def parse(string):
   prepositions = (["of","from","to","over"])
   st=[]

   for s in string.split():
   	st.append(s)
   	
   for i in range(0,st.count("the")):
   	st.remove("the")

   for s in st:
      if s =="sum":
   		st[st.index("sum")] = "\\sum "
      if s =="infinity":
         st[st.index("infinity")] = "\\infty "
      if s =="integral":
         st[st.index("integral")] = "\\int "
      if s =="gradient":
         st[st.index("gradient")] = "\\del "
      if s =="from":
         st[st.index("from")] = "_"
      if s =="to":
         st[st.index("to")] = "^"
      if s =="of":
         st[st.index("of")] = "{"
      if s =="negative":
         st[st.index("negative")] = "-"

      if s =="over":
         st[st.index("over")] = "\\over "
      if s =="curl":
         st[st.index("curl")] = "\\del\\cdot "
      if s =="equals":
         st[st.index("equals")] = "="
      if s =="vector":
         st[st.index("vector")] = "\\vec "
      if s =="cross":
         st[st.index("cross")] = "\\times "
      if s =="psi":
         st[st.index("psi")] = "\\psi "
      if s =="theta":
         st[st.index("theta")] = "\\theta "
      if s =="epsilon":
         st[st.index("epsilon")] = "\\epsilon "

      if s =="minus":
         st[st.index("minus")] = "-"
      if s =="zero":
         st[st.index("zero")] = "0"
      if s =="one":
         st[st.index("one")] = "1"
      if s =="two":
         st[st.index("two")] = "2"
      if s =="three":
         st[st.index("three")] = "3"
      if s =="four":
         st[st.index("four")] = "4"
      if s =="five":
         st[st.index("five")] = "5"
      if s =="six":
         st[st.index("six")] = "6"
      if s =="seven":
         st[st.index("seven")] = "7"
      if s =="eight":
         st[st.index("eight")] = "8"
      if s =="nine":
         st[st.index("nine")] = "9"
      if s =="squared":
         st[st.index("squared")] = "^2"
      if s =="cubed":
         st[st.index("cubed")] = "^3"
      if s =="d":
         i=st.index("d")
         if st[i+1][0] == "d":
           st[i] = "\\frac{d}{" + st[i+1] + "}" 
           del st[i+1]
      if s =="is":
         st[st.index("is")] = "="
      if s =="tau":
         st[st.index("tau")] = "\\tau "

   string_output = ""
   for s in st:
      string_output+=s

   return string_output+(string_output.count("{")-string_output.count("}"))*"}"