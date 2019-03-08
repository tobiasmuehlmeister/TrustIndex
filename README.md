## TrustIndex

This is the material part of the master thesis project: "A report on the replicability of the JAP: Validating automatic data extraction with manual tandem coding"

Link to the OSF page: https://osf.io/e9yqj/

The history.wos file contains the search history on Web of Science for the years 2000 - 01.02.2019 of "Journal of Applied Psychology"

## Getting Started

Download the SciSelect.py file, output, and data directory to make things work. Make sure to have a file in the data\ folder and to transfer the name of the file to line 32: **filepath = "data\FILENAME.txt" 

A web of science output file in txt format is needed (sample given below). 
Some modules are required to start (pyfiglet is just for the ASCII title): random, sys, datetime, pyfiglet.

### Example structure of the web of science output
PT J
AU Doe, J
   Does, X
   Did, L
AF Doe, J
   Does, X
   Did, L
TI Title: A really experimental examination of the exhibitional experience from former excluded exhibitioners 
SO JOURNAL OF FOURTY TWO PSYCHOLOGICAL ANSWERS
SN (ISSN)
PD Date of publication
PY Year of publication
VL Volume
IS Issue
BP From page x
EP To page y
DI DOI number
UT Web of science ID
ER
