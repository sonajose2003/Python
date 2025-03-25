######### OCT 1st ##########################
"""
sqrs = [x**2 for x in range(10) if x % 2 == 0]
print(sqrs)
matrix = [[1,2,3],[4,5,6]]
nested_lst = [num for row in matrix  for num in row]
print(nested_lst)
words = ['abc','efg','xyz']
caps = [word.upper() for word in words]
print(caps)
with_map = list(map(lambda x:x.upper(),words))
print(with_map)
with_dict = {x: x**2 for x in range(10)}
print(with_dict)
num = [1,2,3,None,4]
error_handle = [x**2 for x in num if isinstance(x,int)]
print(error_handle)
"""
########## OCt 2nd ############
num = [1,2,3,4,5,6]
ev_num = list(filter(lambda x: x %2 == 0, num))
print(ev_num)

num = [1,2,3,4,5,6, None, '']
rem_none = list(filter(None,num))
print(rem_none)

# Get squares of even numbers using map and filter
numbers = [1, 2, 3, 4, 5, 6]
sq = list(map(lambda x: x**2, filter(lambda x: x % 2== 0,numbers)))
print(sq)

######## Oct 7th ########
add = lambda x,y : x + y
res = add(5, 3)
print(res)

data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sort_tup_with_fruit = sorted(data, key = lambda x : x[1])
print(sort_tup_with_fruit)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = list(filter(lambda x: x%2 !=0, numbers))
print(odd_num)

numbers = [1, 2, 3, 4, 5]
sq_num = list(map(lambda x : x**2,numbers))
print(sq_num)

##reduce a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y : x+y, numbers, 2)
print(sum)

numbers = [10, -5, 0, 3, -1]
cond_exp = list(map(lambda x : '+' if x > 0 else '-' if x < 0 else '0', numbers))
print(cond_exp)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
#comb_tup = list(zip(names, ages))
comb_tup = list(map(lambda x, y : (x,y), names,ages))
print(comb_tup)

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 95},
    {'name': 'Charlie', 'grade': 90}
]
high_grade = max(students, key = lambda x: x['grade'])
print(high_grade)
#enumerate for tomorrow

numbers = [1, 2, 3, 4, 5]
cubes = [(lambda x:x**3)(x) for x in numbers]


cub = lambda x:x**3
cubes = [cub(x) for x in numbers]  ### OR ## [(lambda x:x**3)(x) for x in numbers]  OR cubes = [x**3 for x in numbers]
print(cubes)

import tkinter as tk

def create_gui():
    root = tk.Tk()
    button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked!"))
    button.pack()
    root.mainloop()

# create_gui()

## OCT 8th ####

from itertools import groupby

data = [('apple', 1), ('banana', 2), ('apple', 3), ('banana', 1)]
# Group by the first element of the tuple

grp = (sorted(data, key = lambda x : x[0]),data)

print(grp)

import re
y = "32343"
x = "....11235457889998089"
pp = re.compile(r'([0-9a-zA-Z])\1'+y)
m = re.search(pp,x)
if m:
    print(m)
    #for i in m:
    #    print(i)
else:
    print("-1")

x = re.findall(r'<.*?>', '<tag>content</tag>') 
print(x)

text = "Yes, please or No, thanks."
pattern = r'?(Yes, )please|thanks'
#pattern = r'(?(?=Yes)please|thanks)'
#pattern = r'(?<=Yes, )please|(?<=No, )thanks'

m = re.findall(pattern, text)
print(m)


## reverse a list
list_ = [1,2,3,4,5]
new_list = []
for i in list_:
    new_list.insert(0,i)
print(new_list)

l = [1,2,3,4]
new_list = []
n = [new_list.insert(0,x) for x in l]
print(new_list)

#palindrome
def check_palindrome(string):
    new_list = []
    for i in range(0,len(string)):
    #for i in str:
        #new_list.insert(0,i)
        print(i)
        new_list.append(string[len(string)-1-i])
    print(new_list) 
    if string == ''.join(new_list):
        print(f"String {string} is a palindrome")
    else:
        print(f"Sring {string} is not a palindrome")

string = "radar"
check_palindrome(string)


##decorator example
def dec_ex(func):
    
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
    
@dec_ex
def greet():
    print("hello")
        
greet()

        
##Static method example:

class MathOperations:
    @staticmethod
    def add(x, y):  ==> can pass any attribute, not dependent on the class/instance variables.
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)  

##class method example
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  

##Annotation example :

def xx(name: str) -> str:  ==> Function Annotations
    print(name)
    
xx("ASSAEA")

Name: str = 'xad' ==> variable annotation

##remove first occurrence of  keys with duplicate values in dict 
d = {'a':1,'b':2,'c':3,'d':2, 'e':3}
k_list = list(d.keys())
v_list = list(d.values())

dups = {x for x in v_list if (v_list.count(x) > 1)}
new_dict = d.copy()
for k,v in new_dict.items():
    if v in dups:
        d.pop(k)
        dups.remove(v)
print(d)

Or  using dict comprehensions ->

dups = {x for x in list(d.values()) if list(d.values()).count(x) > 1}  #==> set

d = {k:v for k,v in d.items() if v not in dups or dups.remove(v)}
print(d)

# #find max using ternary operator -It allows us to write concise conditional expressions on a single line.
# a = 10
# b = 5

# res = a if a > b else b
# print(res)
