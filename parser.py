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
         i=0
         j=0
         for str in st:
            i+=str.count("{")
            j+=str.count("}")
            k=i-j # close all
         if k<0:
            k=0
         st[st.index("of")] =k*"}"+ "{"
      if s =="negative":
         st[st.index("negative")] = "-"

      if s =="over":
         i=0
         j=0
         for str in st:
            i+=str.count("{")
            j+=str.count("}")
            k=i-j-1 # close all but one
         if k<0: 
            k=0    
         st[st.index("over")] = "\\over " + (k)*"}"
      if s =="curl":
         st[st.index("curl")] = "\\del\\cdot "
      if s =="equals":
         st[st.index("equals")] = "={"
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
           st[i+1] = ""
      if s =="is":
         i=st.index("is")
         if st[i+1] == "equal":
            st[i+1:i+3] = ""
         st[i] = "={"
      if s =="tau":
         st[st.index("tau")] = "\\tau "
      if s =="squareroot":
         st[st.index("squareroot")] = "\\sqrt "
      if s =="alpha":
         st[st.index("alpha")] = "\\alpha "
      if s =="double":
         i = st.index("double")
         if st[i+1] == "dot":
            st[i-1]="\ddot " + st[i-1]
            st[i] = ""
            st[i+1] = ""
      if s =="beta":
         st[st.index("beta")] = "\\beta "
      if s =="squareroot":
         st[st.index("squareroot")] = "\\sqrt "
      if s =="gamma":
         st[st.index("gamma")] = "\\gamma "
      if s =="unit":
         i=st.index("unit")
         if st[i+1] == "vector":
            st[i+2] = "\\hat "+st[i+2]
         st[i] = ""
         st[i+1] = ""
      if s =="hat":
         i=st.index("hat")
         st[i-1] = "\\hat "+st[i-1]
         st[i] = ""
      if s =="gamma":
         st[st.index("gamma")] = "\\gamma "

      if s=="capital":
         i=st.index("capital")
         st[i+1] = st[i+1][0].upper()
         st[i] = ""
      if s=="sub":
         st[st.index("sub")] = "_"
      if s=="point":
         st[st.index("point")] = "."
      if s=="dot": # This is why we unit test
         st[st.index("dot")] = "\cdot "
      if s=="times":
         st[st.index("times")] = "*" # personal preference, be quiet
      if s=="first":
         i=st.index("first")
         if st[i+1] == "derivative": # first derivative of y with respect to/ in terms of x
            if (st[i+5] == "respect") | (st[i+6] == "terms"):
               st[i] = "\\frac{d "+ st[i+3]  +"}{d"+st[i+7]+"}"
               st[i+1:i+7] = ""
            else: # assume in terms of x 
               st[i] = "\\frac{d}{dx}"
               st[i+1:i+3] = ""      
      if s=="second":
         i=st.index("second")    
         if st[i+1] == "derivative": 
            if st[i+5] == "respect":    
               st[i] = "\\frac{d "+ st[i+3]  +"}{d"+st[i+7]+"}"
               st[i+1:i+8] = ["","","","","","",""]  
            if st[i+5] == "terms":                     
               st[i] = "\\frac{d "+ st[i+3]  +"}{d"+st[i+7]+"}"
               st[i+1:i+8] = ["","","","","","",""]
            else: 
               st[i] = "\\frac{d}{dx}"    
               st[i+1:i+3] = ""
      if s=="third":
         i=st.index("third")    
         if st[i+1] == "derivative":
            if (st[i+5] == "respect") | (st[i+5] == "terms"):    
               st[i] = "\\frac{d "+ st[i+3]  +"}{d"+st[i+7]+"}"
               st[i+1:i+7] = ""  
            else: 
               st[i] = "\\frac{d}{dx}"    
               st[i+1:i+3] = ""     
      if s=="conjugate":
         st[st.index("conjugate")] = "^*"
      if s=="absolute":
         i=st.index("absolute")
         if st[i+1] == "value":
            st[i] = "\\abs{"
            st[i+1] = ""
      if s=="not":   
         st[st.index("not")] = "_0 "     
      if s=="sine":
         st[st.index("sine")] = "\\sin "
      if s=="cosine":
         st[st.index("cosine")] = "\\cos "
      if s=="tangent":
         st[st.index("tangent")] = "\\tan "
      if s=="arcsine":
         st[st.index("arcsine")] = "\\arcsin "
      if s=="arccosine":
         st[st.index("arccosine")] = "\\arccos "
      if s=="arctangent":
         st[st.index("arctangent")] = "\\arctan "
      if s=="secant":
         st[st.index("secant")] = "\\sec "
      if s=="cosecant":
         st[st.index("cosecant")] = "\\csc "
      if s=="cotangent":
         st[st.index("cotangent")] = "\\cot "
      if s=="arcsecant":
         st[st.index("arcsecant")] = "\\arcsec "
      if s=="arccosecant":
         st[st.index("arccosecant")] = "\\arccsc "
      if s=="arccotangent":
         st[st.index("arccotangent")] = "\\arccot "
      if s=="limit":
         st[st.index("limit")] = "\\lim "
      if s=="as":
         st[st.index("as")] = "_{ "
      if s=="approaches":
         st[st.index("approaches")] = "\\rightarrow "
      if s=="root": 
         i=st.index("root")
         if st[i-1] == "second":
            st[i-1] = "\\sqrt[2]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif (st[i-1] == "third")|(st[i-1]=="cube"):
            st[i-1] = "\\sqrt[3]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "fourth":
            st[i-1] = "\\sqrt[4]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "fifth":
            st[i-1] = "\\sqrt[5]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "sixth":
            st[i-1] = "\\sqrt[6]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "seventh":
            st[i-1] = "\\sqrt[7]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "eighth":
            st[i-1] = "\\sqrt[8]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
         elif st[i-1] == "ninth":
            st[i-1] = "\\sqrt[9]{"
            st[i] = ""
            if st[i+1] == "of":
               st[i+1] = ""
      if s=="product":
         st[st.index("product")] = "\\prod " 
      if s=="less":
         i=st.index("less")
         if st[i+1] == "than":
            if st[i+3] == "equal":
               st[i] = "\\leq "
               st[i+1:i+5] =""
            else:
               st[i] = "<"
               st[i+1:i+3]=""
      if s=="greater":
         i=st.index("greater")
         if st[i+1] == "than":
            if st[i+3] == "equal":
               st[i] = "\\geq "
               st[i+1:i+5] =""
            else:
               st[i] = ">"
               st[i+1:i+3]=""

   string_output = ""
   for s in st:
      string_output+=s

   string_output+=(string_output.count("{")-string_output.count("}"))*"}"
   print string_output #only for testing
   return string_output


parse(sys.argv[1]) #ONLY FOR TESTING
