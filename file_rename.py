import os
from pprint import pprint

dir = "..\Documents\weather"
os.chdir(dir)
print(os.getcwd())

for file in os.listdir():
	short = file.split("_")
	short = '_'.join(short[1:])
	os.rename(file,short) 
