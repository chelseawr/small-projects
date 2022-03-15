import os
from pprint import pprint

dir = "..\Documents\weather"
os.chdir(dir)
print(os.getcwd())

for file in os.listdir():
	short = file.split("_")
	short = '_'.join(short[1:])
	os.rename(file,short) 
	#name = []
	#for item in short:
	#	if item != 'weather':
	#		name.append(item)

	#name = '_'.join(name)
