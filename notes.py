#!/bin/python3


# string formatting
myName = input()
print('It is good to meet you, {}'.format(myName))
# int to string .format(str(29)))

# print
print('Hello', end='')
print('World')
# HelloWorld

print('cats', 'dogs', 'mice')
# cats dogs mice

print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice

# list[start,stop]
spam = ['cats', 'dogs', 'mice']
spam[1:3]
# ['bat', 'rat']

# item in list?
'cat' not in spam
# True

# copy list
spamCopy = spam[:]

# delete list item
del spam[2]

for i, supply in enumerate(supplies):
    print('Index {} in supplies is: {}'.format(str(i), supply))
# Index 0 in supplies is: pens

# list comprehension
a = [1, 3, 5, 7, 9, 11]
[i - 1 for i in a]
# [0, 2, 4, 6, 8, 10]

# set comprehension
b = {"abc", "def"}
{s.upper() for s in b}
# {"ABC", "DEF"}

# dict comprehension
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}
#{'Pooka': 'name', 5: 'age'}

# List comprehension can be generated from a dict
c = {'name': 'Pooka', 'first_name': 'Oooka'}
["{}:{}".format(k.upper(), v.upper()) for k, v in c.items()]
# ['NAME:POOKA', 'FIRST_NAME:OOOKA']

#iterate through a Nested dictionary
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for key in data:
    print(key,'->',data[key])

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])

# cut off last item
my_string[:-1]

# reverse a string
my_string_reversed = my_string[::-1]

# join a string
','.join('12345')

# string into an array
'1,2,3,4,5'.split(',')
# [‘1’, ‘2’, ‘3’, ‘4’, ‘5’]

# array into string
L = [1,2,3]       
" ".join(str(x) for x in L)
# '1 2 3'

def high_and_low(numbers): 
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# int to unicode
x = 52
chr(x)

# remove or replace spaces from a string
s='aaa bbb ccc ddd eee'
s1 = s.replace(' ','')

#  filter values based on conditional logic
list(filter(lambda x: x > 5, range(8)))

# Map applies a function to every element in an iterable.
list(map(lambda x: x**2, range(8)))

# count times x appears in string
word = "Rio de Janeiro"
print(word.count(' '))
#  2

# repeat a string by multiplying
words = "Tokyo" * 3

# subsitute with {} for *any length of n
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# loops
  # range(start,stop,step) 
for i in range(5):
    print('Jimmy Five Times ({})'.format(str(i)))

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
# *
# **
# ***
# ****
# *****

# slice an array/list
# list[start:stop:step]
#  +---+---+---+---+---+
#  | m | o | v | i | e |
#  +---+---+---+---+---+
#  0   1   2   3   4   5 
# -5  -4  -3  -2  -1  
symbols = dict(
   se='┌',  swe='┬',  sw='┐',
  nse='├', nswe='┼', nsw='┤',
   ne='└',  nwe='┴',  nw='┘',
   ns='│',   we='─',
)

def print_json_dict(autofill_dict):
    return json.dumps(autofill_dict, indent = 4, sort_keys=True)
