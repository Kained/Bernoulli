#!/bin/bash

while read line; do python parser.py " $line "; done < test_strings
