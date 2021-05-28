#!/bin/python3
import re

'''
    uses regular expressions to replace occurances of "you" or "u"
    with "your client" for a fictional law firm.
      Chelsea May - 2021
''' 

def autocorrect(text):  

    # copy original string
    corrected = text
    
    reg = r'(\byou+\b)|(\bu\b)'
    textFound = re.search(reg, text)
    if textFound:
      corrected = re.sub(reg, 'your client', text) 
        
    return corrected            
             