#!/bin/bash

while read line; 
do 
python parser.py " $line "; 
echo ---------------------------------------------------------
done < test_strings
