 Difference btn prog lang and scripting language.
Prog language – compilation –source code converted to machine readable format called object code. It is executable
Script language – interpretation –source code converted to byte codes which is not executable.
.py(source code) converted to .pyc file (byte code) 

Programming Languages:
1.	General Purpose: Programming languages are often designed to be general-purpose and can be used to create a wide variety of software applications, from system software to applications.
2.	Compilation: Many programming languages are compiled, meaning that the code is translated into machine code (or intermediate code) before it is executed. Examples include C, C++, and Rust.
3.	Performance: Compiled languages often offer better performance because they are translated directly into machine code.
4.	Complexity: They can handle complex systems and are used for building large-scale applications. They often have rich feature sets and strong type systems.
Scripting Languages:
5.	Specialized Purpose: Scripting languages are often designed for specific tasks, such as automating repetitive tasks, interacting with other software, or managing system configurations.
6.	Interpretation: Scripting languages are usually interpreted, meaning that the code is executed line-by-line by an interpreter at runtime. Examples include Python, JavaScript, and Bash.
7.	Ease of Use: Scripting languages are generally easier to write and understand, often prioritizing developer productivity and ease of integration with other systems over raw performance.
8.	Flexibility: They are often used for tasks such as automating system tasks, web development, and data processing. They may offer less strict type systems compared to compiled languages.

In unix, shebang should be the first line in the script file. #!/usr/bin/python (interpreter path)

To run a script =>
>> python <file path>

>>help(module name>   Displays all documentation for that module.
>>help(“keywords”)
>>help(“topics”)

variable - stores piece of data & gives specific name
value = 10 --> value- variable name
 >>> value = 10
>>> value
10
>>> name = "Ramesh"
>>> name
'Ramesh'
>>>
Literals: - constant values
-numeric literal 1,2 etc
-string literal – anything in ‘ ’ or “ “

Named constants:
>>import math
>>math.pi  >>> here , pi is a named constant.
3.1415..
>>pi=50
>>pi
‘50’
	Outside math, ‘pi’ can get any value

commenting the lines in python:
	# This is the Comments
      ''' This is the commenting
	""" This is commenting – used for a huge set of data spanned across multiple lines.

Single quote within a single quote needs to use ‘\’ (escape operator)
>>str1 = ‘sheela\’s book’
Or >>str1 = “sheela’s book”

Print - To print the value, It can use either single quote or double quotes
print ('hello world')
print ("hello world")
hello world
hello world
print ("hello \n world")  #\n is escape character, Next line
hello
  world

print ("hello\tworld") #\t is for tab
hello	world

To define variable and store the values to variable and print it
>>> name1 = "Ramesh"
>>> name2 = "Kumar"
>>> print (name1, name2)
Ramesh Kumar
>>> name = input()
test
>>> print(name)
test-
>>>
>>> name = input('enter the name\n')
enter the name
Ramesh
>>> print(name)
Ramesh
>>>
[[ difference between input() and raw_input()
In python2 , 2 cmds – input() and raw_input()
Raw_input() will take the raw data
Input()- will evaluate the data entered
Eg:
>>> x=10
>>> y=20
>>> expr=raw_input('enter value:')
enter value:x+y
>>> expr
'x+y'
>>>
>>> expr=input('value:')
value:x+y
>>> expr
30
>>> 

>>> newexpr=eval(raw_input('enter value:'))
enter value:x+y
>>> newexpr
30

In python2 eval(raw_input()) is equivalent to input()

In python3 eval(input()) is equivalent to input() in python2
Eg:
>>> x=10
>>> y=20
>>> expr=input('entervlaue:')
entervlaue:x+y
>>> expr
'x+y'
>>> newexpr=eval(input('enter value:'))
enter value:x+y
>>> newexpr
30
>>>
]]

keyword: in used to check the value is with in another value  not applicable to type ‘int’
>>> 'a' in 'ram'
True
>>>
>>> newexpr
30
>>> 3 in newexpr
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    3 in newexpr
TypeError: argument of type 'int' is not iterable
>>>

The order of mathematical operation: first multiplication, division, addition, subtraction
keywords: and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

There are 5 main data types in python as follows:
Numbers - immutable - object stored as numeric value
strings - immutable - object stored as string
lists - * mutable - data stored in the form of a list sequence
Tuples -  immutable - data stored in the form of sequence of immutable
Dictionaries -* mutable - associates one thing to another irrespective of the type of data

Data types are implemented as objects

List:  is collection of elements, separated by comma. In list first index start with 0, list allows you to store more than one variable
starts and ends with square bracket,  list is mutable.
list size is dynamic where as tuple is fixed size in nature
list size is dynamic - we can modify the list by using index update the new element

cmp(list1, list2) -> Compares elements of both lists. == > this is not a list method, it is a built-in function present in python2 I believe. Could not find it in python3.
cmp(...)
    cmp(x, y) -> integer

    Return negative if x<y, zero if x==y, positive if x>y.

len(list) ->Gives the total length of the list.
max(list) -> Returns item from the list with max value.
min(list) ->Returns item from the list with min value.
list(seq) ->Converts a tuple into list.


list has some methods as follows: 
        #append, pop, remove, insert, count, index, sort,  extend, reverse, clear

1)	list.reverse()
the reverse method is used to reverse the order of elements in a mutable sequence. It modifies the sequence in place and does not return a new sequence. This method is available for lists but not for other sequence types like strings or tuples.
If you need a reversed copy of the list while keeping the original list unchanged, use slicing or other methods.
2)	reversed_list = numbers[::-1]
   3) Using reversed() Function: This returns an iterator that yields the elements of the list in reverse order. You can convert it to a list if needed.
numbers = [1, 2, 3, 4, 5] 
reversed_iter = reversed(numbers) 
reversed_list = list(reversed_iter) 
print(reversed_list) # Output: [5, 4, 3, 2, 1]

The list.sort() method sorts the list in place and returns None. It modifies the original list rather than creating a new one.
If you need to retain the original list and create a sorted copy instead, you can use the sorted() function, which works similarly but returns a new sorted list.


Concatenation -
	Strings: Use +, join(), or string formatting methods.
	Lists: Use +, extend(), or list comprehensions.
	Tuples: Use +.

In Python, the join() method is used to concatenate elements of an iterable into a single string, with a specified separator string. Here's a breakdown of the differences between ' '.join() and x.join():
' '.join(iterable)
	Purpose: This syntax uses the string ' ' (a space character) as the separator to join elements of the iterable.
	Example:
python
Copy code
words = ['Hello', 'world', 'Python']
result = ' '.join(words)
print(result)  # Output: "Hello world Python"

	Behavior: The method concatenates the elements of words with a space between each element.
x.join(iterable)
	Purpose: This syntax uses the string x (which can be any string) as the separator to join elements of the iterable.
	Example:
python
Copy code
delimiter = ', '
words = ['apple', 'banana', 'cherry']
result = delimiter.join(words)
print(result)  # Output: "apple, banana, cherry"

	Behavior: The method concatenates the elements of words with a comma and a space as the separator.
Key Points:
9.	Separator String: In ' '.join(), the separator is a space, while in x.join(), x can be any string that you choose as the separator.
10.	Method Call: ' '.join() calls the join method on the string ' ', while x.join() calls the join method on the string x.
11.	Usage: ' '.join() is used when you specifically want a space as a separator, whereas x.join() allows for any custom separator string.
In summary, the difference lies in the separator string used for concatenation. ' '.join() uses a single space as the separator, while x.join() uses whatever string x represents as the separator.

 List and given one example for adding new element.

syntax:
list = ['item1', 'item2', 'item3'] #list with multiple value
>>> list1 = ['ramesh', 'suresh', 'ganesh', 1,2,3,4,5]
>>> list1
['ramesh', 'suresh', 'ganesh', 1, 2, 3, 4, 5]
>>> list1.append('RAM')
>>> list1
['ramesh', 'suresh', 'ganesh', 1, 2, 3, 4, 5, 'RAM']
>>>

# looping the list to print the list
>>> list1
['ramesh', 'suresh', 'ganesh', 1, 2, 3, 4, 5, 'RAM']
>>> for i in list1:
	print(i)

ramesh
suresh
ganesh
1
2
3
4
5
RAM
>>>
>>> list = ['ramesh', 'suresh', 'data', '3', '4', '5']
>>> list[5]
'5'
>>> list[0]
'ramesh'
>>> list[-2]
‘4’
Loop through a list dynamically:
for i in range(len(list1)):
    print(list1[i])

[[[
>> range(10) -> get 10 numbers starting from 0 to 9.
>>range(2,10) -> start from 2 => [2,..,9]
>>range(1,10,2)  step of 2 => [1,3..,9]
>>> for i in range(5):
	print(i)
0
1
2
3
4
>>> for i in range(2,5):
	print(i)
2
3
4
>>> for i in range(1,10,2):
	print(i)
1
3
5
7
9
]]]
 remove, Del the difference between is remove will remove element from the list where as del will remove the complete list.
Del is not a list method. It is a basic method.
Pop will remove the element at the index passed. If no index is passed, then will remove the last element. It will return the removed element.
>>> del(list1)   >>>>>> this removed list1

Append and insert difference between both is Append would append the element at the end of the list where as insert would insert the element with index mentioned
======> Append Append one element at the end of the list
======> insert will insert the element with index mentioned
=======> Using remove you can delete element from a list:
=======> Diff between len & count = len will count no of elements in list where as count will tell how many times particular element from the list(duplicate element)
=======> index – gives the index number of element passed as argument.


list.insert(index, obj)		
>>> l
[0, 1, 2, 3, 4, 5, 'Ramesh']
>>> l.insert(6, 'cisco')
>>> l
[0, 1, 2, 3, 4, 5, 'cisco', 'Ramesh']
>>>

>>> l.append('kumar')
>>> l
[0, 1, 2, 3, 4, 5, 'Ramesh', 'kumar']
>>>
	
>>> l.remove('cisco')
>>> l
[0, 1, 2, 3, 4, 5, 'Ramesh']
>>>

>>> l
[0, 1, 2, 3, 4, 5, 'Ramesh', 'kumar']
>>> del l[6]
>>> l
[0, 1, 2, 3, 4, 5, 'kumar']
>>>
			
>>> a = [0, 1, 2, 3, 4, 5]
>>> del a[-1]
>>> a
[0, 1, 2, 3, 4]
>>> del a[2]
>>> a
[0, 1, 3, 4]
>>>

>>> l
[0, 1, 2, 3, 4, 5, 'kumar', 'kumar', 0]
>>> del l[8]
>>> l
[0, 1, 2, 3, 4, 5, 'kumar', 'kumar']
>>> l.append(0)
>>> l
[0, 1, 2, 3, 4, 5, 'kumar', 'kumar', 0]
>>> del l[-1]
>>> l
[0, 1, 2, 3, 4, 5, 'kumar', 'kumar']
>>>

Append the list - it can append only one element at the end of the list
list.append(obj)
	
list4 = [1, 2, 3, 4, 5]
list4.append('200')
print(list4)

[1, 2, 3, 4, 5, '200']

>>> list1.append("10,20")
>>> list1
[1, 2, 3, 4, 2, 4, 5, '10,20']

>>> l.append('william')
>>> l
['Ramesh', 20, 30, 40, 50, 'william']
>>> l.count(33)
0
>>> l.count(20)   count of the element passed here.
1

>>> list = ['ramesh', 'suresh', 'data' '3', '4', '5']
>>> len(list)
5

>>> l.remove('Ramesh')
>>> l
[20, 30, 40, 50, 'william']
>>> l.reverse()
>>> l
['william', 50, 40, 30, 20]

>>> list1
['10,20', 5, 4, 2, 4, 3, 2, 1]
>>> list1.index('10,20')  -> gives the index of element passed
0
extend() - will extend multiple elements at the end of the list
sysntax:
list.extend(seq)

sample program:
alist = [123,345,'abc','rajanesh',128]
blist = [200, 'ramesh']
alist.extend(blist)
print(alist)

output:
[123, 345, 'abc', 'rajanesh', 128, 200, 'ramesh']

>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.extend([5,6,7])
>>> numbers
[1, 2, 3, 1, 2, 3, 4, 5, 6, 7]

Append and extend:
Using append, only one element can be appended. Using extend, we can append a list of elements to the existing list.(pass an already defined list or pass the arguments within [] separated by comma.)

concat: Concatenation - Adding two list
x = l0+l1

sample program:
-------------
dlist = [123,45,67]
elist = [89, 10]
mst = dlist + elist
print (mst)

output
-------
[123, 45, 67, 89, 10]

count: how many times value appear in the list ?
>>> list = ['Ramesh', 20, 50, 'william', 20, 20, 'Ramesh']
>>> list
['Ramesh', 20, 50, 'william', 20, 20, 'Ramesh']
>>> list.count(20)
3
>>> list.count('Ramesh')
2
>>> list.count('william')
1
>>> list.count('ram')
0

>>> list
['ramesh', 'kumar', 'data']
>>> list[0] = "tst"
>>> list
['tst', 'kumar', 'data']


insert: will insert the element for mentioned index   The difference between insert and append -- append will append end of the list where as insert will go through indexing
syntax: list.insert(index, obj)
        L.index(value, [start, [stop]]) -> integer -- return first index of value.

words = ['Hello', 'world', 'Python'] 
words.insert(1-3, 'nnew')
print(words)
['Hello', 'nnew', 'world', 'Python']

sample program:
-----------
clist = [123, 'ramesh', 'data']
clist.insert(1, 'abcd')
print(clist)

output:
=====
[123, 'abcd', 'ramesh', 'data']

>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.index(2,1)
1
>>> numbers.index(2,2)
4
>>> numbers[4]
2

>>> list = ['Ramesh', 20, 50, 'william', 20, 20, 'Ramesh']
>>> list.index(20)
1
>>> list.index(50)
2
>>> list.index('Ramesh')  gives first occurrence
0
>>> list.index('william')
3

words = ['Hello', 'world', 'Python'] 
x = words.index('Hello', 0,3)
print(x)
0
remove(value) Remove the first instance of a value from the list.
>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.remove(2)
>>> numbers
[1, 3, 1, 2, 3]  
reverse() Reverse the order of the list's items.
>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.reverse()
>>> numbers
[3, 2, 1, 3, 2, 1]

sort() Sort the items in the list.
>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.sort()
>>> numbers
[1, 1, 2, 2, 3, 3]

This method, exceptionally returns a value (from the list) and changes the list itself.
pop() Removes the last item from the list and returns it.
>>> numbers = [1, 2, 3, 1, 2, 3]
>>> numbers.pop()
3
>>> numbers
[1, 2, 3, 1, 2]

len - returns the total number of items difference bet len and count
>>> x = "Ramesh"
>>> len(x)
6
>>>

>>> len([1,2,3,4])   -> length of the string

tuples: is just like list, tuple is immutable, we cannot add or change or delete element from the tuple once u create tuple
	The elements of a tuple have a defined order, just like a list.
You can't find elements in a tuple using indexing.      
	tuples use parentheses whereas lists use square brackets.Like string indices, tuple indices start at 0
	Tuples are faster than lists
	Tuples can be converted into lists, and vice-versa. The built-in tuple function takes a list and returns a tuple with the same elements, and the list function takes a tuple and returns a list

why we need tuple : for security reason keep the data read only some of the functions not to be modified in that case we can go for tuple

tuple = () 		 # no item in the tuple
tuple = (1,2,3)
tuple = 1,2,3 		 #parenthesis are optional
tuple = 2,		 #single-item tuple
tuple = tuple(list1)    #tuple from list
tuple = ([1,2], 3)	 #list inside a tuple

>>> tup1 = (1,2,3,4,5)
>>> tup2 = ('john',88,90)
>>> tup1
(1, 2, 3, 4, 5)
>>> tup2
('john', 88, 90)
>>> tup1[3]
4
example as follows that cannot assign values to tuple.
>>> tup1[3] = 5
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tup1[3] = 5
TypeError: 'tuple' object does not support item assignment
>>>

But we can add it to list as follows:

>>> l = tup1
>>> l
(1, 2, 3, 4, 5)
>>>

functions or methods available in tuple: - count and index -count function will tell how many times the elements are repeated

>>> tuple = ('john', 'john', "test", "test", 100, 100, 200)
>>> tuple
('john', 'john', 'test', 'test', 100, 100, 200)

>>> tuple.count('john')
2
>>> tuple.count('test')
2

>>> tuple.index(200)
6

Delete Tuple Elements - Removing individual tuple elements is not possible. To explicitly remove an entire tuple, just use the del statement

cmp(tuple1, tuple2)  ->  Compares elements of both tuples.==> not present
len(tuple)		-> Gives the total length of the tuple.
max(tuple)		-> Returns item from the tuple with max value.
min(tuple)		-> Returns item from the tuple with min value.


Dictionaries: is similar to the list but dictionaries can store keys and values
Dict is mutable

Dictionaries start and close with flower bracket
Dictionary is a very dynamic datatypes no other programming language contain
In real time we use dictionaries no of ip address hit the server as count here ip is key and count is value

ex:
 dict = {'key':'value','key':'value'}

The dictonary is having information abt book, I can get information by sending the key name.

>>> dict = {'title':'who will cry when you die', 'author':'Robert', 'price':'100$'}
>>> print(dict)
{'author': 'Robert', 'title': 'who will cry when uou die', 'price': '100$'}

>>> print(dict.keys())   ---> To print only keys
dict_keys(['title', 'author', 'price'])
>>>
>>> print(dict.values())  ---> To print only values
dict_values(['who will cry when you die', 'Robert', '100$'])

>>> print(dict['title'])
who will cry when uou die

>>> print(dict['title'])
who will cry when uou die
>>> print(dict['author'])
Robert
>>> print(dict['price'])
100$

>>> age = {'john':21, 'peter':35, 'bob':44} #Here key is john and its value is 21
>>> age
{'peter': 35, 'bob': 44, 'john': 21}
>>> print(age)
{'peter': 35, 'bob': 44, 'john': 21}
>>> age["john"]
21
>>> age
{'peter': 35, 'bob': 44, 'john': 21}
>>> age['ram'] = 32 =================> Newly added
>>> age
{'peter': 35, 'bob': 44, 'john': 21, 'ram': 32}
>>> age['ram'] = 30  ==========>updating dictionary
>>> age
{'peter': 35, 'bob': 44, 'john': 21, 'ram': 30}
>>>

>>> age
{'peter': 35, 'bob': 44, 'john': 21, 'ram': 30}
>>> del age['ram']  ==========> Delete the key from dictionary
>>> age
{'peter': 35, 'bob': 44, 'john': 21}
>>>
dict.clear(); # =======================>remove all entries in dict
>>> age.clear()
>>> age
{}
>>> age
{'williams': 55, 'peter': 35, 'bob': 44, 'john': 21}

>>> age = {'peter': 35, 'peter': 40, 'bob': 44, 'john': 21} ====> Duplicate keys allowed and last assignment wins as follows
>>> age
{'peter': 40, 'bob': 44, 'john': 21}

len(dict) => Gives the total length of the dictionary. This would be equal to the number of items in the dictionary

>>> print(age['bob'])
44
>>> del age['bob']
>>> age
{'williams': 55, 'peter': 35, 'john': 21}
>>>

keys() -- is going to return list of all the values in the given dictonary
eg:
temp.keys()
temp.items() => key,value pairs as a tuple
temp.values()

Print elements of a dict :
>>> x = d1.items()
>>> print(x)
dict_items([('d', 4), ('c', 3), ('a', 1), ('b', 2)])
>>> x
dict_items([('d', 4), ('c', 3), ('a', 1), ('b', 2)])
>>> for i in x:
	print(i)
('d', 4)
('c', 3)
('a', 1)
('b', 2)
>>>

dict.fromkeys() - Create a new dictionary with keys from seq and values set to value
seq = ('name', 'age')
dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)
dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict)
When we run above program, it produces following result −
New Dictionary : {'age': None, 'name': None}
New Dictionary : {'age': 10, 'name': 10}

dict.get(key, default=None) - For key key, returns value or default if key not in dictionary
dict.values() - Returns list of dictionary dict's values

The update() method in Python dictionaries is used to merge another dictionary or an iterable of key-value pairs into the dictionary on which it is called. This method updates the dictionary with elements from another dictionary or iterable, overwriting existing keys with new values.
d1 = {'a': 1, 'b': 2} 
d2 = {'b': 3, 'c': 4} 
d1.update(d2) 
print(d1) # Output: {'a': 1, 'b': 3, 'c': 4}
d = {'a': 1, 'b': 2} 
pairs = [('b', 3), ('c', 4)] 
d.update(pairs) 
print(d) # Output: {'a': 1, 'b': 3, 'c': 4}

string:
A string is a sequence of characters. Strings are basically just a bunch of words.
 Strings Are Immutable - once you have created a string, you cannot change it

string can be in single quotes or double quotes

>>> a = "hello"
>>> b = 'hello'
>>> print(a)
hello
>>> print(b)
hello
>>> print(a+b) - > concatenation using + -> no space separation
hellohello
>>> print(a + b)
hellohello
>>> c = 55
>>> print(a+c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(a+c)
TypeError: Can't convert 'int' object to str implicitly

>>> print(a+str(c)) #convert the c to string
hello55


sleep - when ever we delay some functionality add sleep
time.sleep(3) - delay for 3 seconds

USING for loop

list = [1,2,3,4,5,6,78]

for rem in list:
    print(rem)

output
======
1
2
3
4
5
6
78
Operators:
There are 7 arithmetic operators -> +, -, *, /, % ** //
print("5+2 =", 5+2)
print("5-2 =", 5-2)
print("5/2 =", 5/2)
print("5%2 =", 5%2)
print("5**2 =", 5**2)
print("5//2 =", 5//2)

Returns x to the power of y
3 ** 4 gives 81 (i.e. 3 * 3 * 3 * 3 )

<= (less than or equal to)
Returns whether x is less than or equal to y
x = 3; y = 6; x <= y returns True .

>= (greater than or equal to)
Returns whether x is greater than or equal to y
x = 4; y = 3; x >= 3 returns True .

!= (not equal to)
Compares if the objects are not equal
x = 2; y = 3; x != y returns True .
output
5+2 = 7
5-2 = 3
5/2 = 2.5
5%2 = 1 – modulus (remainder)
5**2 = 25
5//2 = 2 -- floor division - This means that the result of the division is the largest integer less than or equal to the actual division result. The quotient rounded down to the nearest integer.

Other operators : + , *, in, not in, [], [:], %

Repetition: *
>>str1=’hello’
>>str1*3
hellohellohello

slice operator:
>>str1[1:3] -> [(starting index) : (ending index + 1)]
‘el’
>>> str1[:]
'hello'
>>> str1[0:]
'hello'
>>> str1[:5]
'hello'
>>> str1[:10]
'hello'
>>>

Formatting strings : >>>>>>>>>>look in detail
& method format

String methods :
Str1.upper()
Str1.find() - > finds first occurrence
Str1.rfind() ->last occurrence
Str1.split()

>>> str1.upper()
'HELLO'
>>> str1.find('o')
4
>>> str1.find('l')
2
>>> str1.rfind('l')
3
>>> str1.split('e')
['h', 'llo']
>>>
Sets:
Used to quickly access non-duplicate elements (non-sequential)
Like lists – use flower brackets {}
>>> set1={1,2,3,4}
>>> set1
{1, 2, 3, 4}
>>> set2 = {1,2,3,4,2,3,4,5,6,3}
>>> set2
{1, 2, 3, 4, 5, 6}
>>> set3 = set([1,2,3,3,4,4,5,5])
>>> set3
{1, 2, 3, 4, 5}
>>>
No operations with index. We can add and remove elements directly.
>>> set1.add(5)
>>> set1
{1, 2, 3, 4, 5}
>>> set1.remove(4)
>>> set1
{1, 2, 3, 5}
>>>

Collections:

What if I need a dictionary, but I need it to be in order?
---------------------------------------------------------
collections.OrderedDict data structure in Python.

>>> d1
{'d': 4, 'c': 3, 'a': 1, 'b': 2}
>>>
>>> import collections
>>> c1 = collections.OrderedDict(d1)
>>> 
>>> c1
OrderedDict([('d', 4), ('c', 3), ('a', 1), ('b', 2)])

    This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.
    
    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing


if   statement:
a = 10
b = 20
if (a > b):
    print("a is big")
else:
    print("b is big")
    
b is big

a = 40
if a == 20:
   print(" 1st one is", a)
if a == 30:
    print("2nd one is", a)
if a == 40:
    print("3rd one is", a)

I. If -> for one condition matching if can ce used.
sample :
1. age = 50
if age > 10:
    print('True')

2. age = 10
if age > 16:
    print('you are eligible to get license')
else :
    print('you are not eligible to get license')


>>> True if x == 10 else False
True
>>>
II. elif -> To validate more conditions match elif can be used.

1. age = 41
if age <= 15 :
    print('you are eligible to drive light vehicle')
elif age <= 25 :
    print('you are eligible to drive heavy vechile')
elif age <= 40 :
    print('please go for health checkup to get the eligibility for driving heavy vechile trucks')
else :
    print('Not eligible')

The elif statement - would check multiple expressions if one conditions is true

a = 30
if a == 20:
   print(" 1st one is", a)
elif a == 25:
    print("2nd one is", a)

elif a == 30:
    print("3rd one is", a)
elif a == 35:
    print("4rth one is", a)
else:
    print("Nothing matched")

3rd one is 30
>>>
nested if  -  if...elif...else - would check conditions after one condition is success
if expression1:
statement(s)
if expression2:
statement(s)
elif expression3:
statement(s)
else
statement(s)
elif expression4:
statement(s)
else:
statement(s)

var = 100
if var < 200:
print "Expression value is less than 200"
if var == 150:
print "Which is 150"
elif var == 100:
print "Which is 100"
elif var == 50:
print "Which is 50"
elif var < 50:
print "Expression value is less than 50"
else:
print "Could not find true expression"
print "Good bye!"

while Loop: repeatedly executes a target statement as long as a
given condition is true

while expression:
statement(s)

1. To check given number is even or not?

	number = int(input("Enter any number: "))
	if(number%2==0):
	print("The number is even")
	else:
  	print("The No is odd")
	

2. To check given letter is vowel or consonant

x = input("x:")
print("vowel") if x in 'aeiou' else print("consonent")
ss

3. To find the no is greater or not

	num1 = int(input("Enter the number1: "))
	num2 = int(input("Enter the number2: "))
	num3 = int(input("Enter the number3: "))

	if ((num1>num2) & (num1>num3)):
	print(num1,"is the greater among three")
	elif((num2>num3) & (num2>num3)):
	print(num2, "is the greatest among three")
	else:
	print(num3,"is the greatestamong three")

4. To find the factorial of a number example- 3 => 3X2X1 = 6
fact = 1
num = int(input("Enter any number: "))
for i in range(1, (num+1)): # range starts from 0 so 0 multiplies by given no is 0 and the number plus 1 gives that multiplication of given no not up to the no
    fact = fact * i    # i will be starting from 1
print(fact)

Now using while loop:
fact = 1
num = int(input("Enter any number: "))
i = 1
while(i<=num):
    fact = fact * i
    i = i+1
print (fact)

5. To print multiplication table anf any given no
num = int(input("Enter any number: "))
for i in range(1, 11): # multiplication for 10 times so 11
    print(num, "x",i,"=",num*i)

Enter any number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50



III. while statement:
	while statement allows you to repeatedly execute a block of statements as long
as a condition is true. A while statement is an example of what is called a looping
statement. A while statement can have an optional else clause.
The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won't be executed.

random_num = random.randrange(0,100) #randomly it would generate the numbers from 0 to 100
while (random_num != 15):
	print(random_num)
	random_num = random.randrange(0,100)

IV. for loop:

for <variable> in <sequence>:
	<statements>
else:
	<statements>
The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement.
The common construct is to run a loop and search for an item. If the item is found, we break out of the loop using the break statement. There are two scenarios in which the loop may end. The first one is when the item is found and break is encountered. The second scenario is that the loop ends without encountering a break statement. Now we may want to know which one of these is the reason for a loop’s completion. One method is to set a flag and then check it once the loop ends. Another is to use the else clause.
## Prime numbers are the natural numbers greater than 1 with exactly two factors, i.e. 1 and the number itself.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
It finds factors for numbers between 2 to 10. We can add an additional else block which catches the numbers which have no factors and are therefore prime numbers.
sample:
------
1. for i in range(1,5): #Generating sequence of numbers using built in range function and printing the same
    print(i)
output:
1
2
3
4
for node in ['dutA', 'dutB', 'dutC', 'dutD', 'TGEN']:

2. for i in range(5):
	print("hello")
hello
hello
hello
hello
hello

for i in range (5):
    print(i)
0
1
2
3
4

name = "test"
for i in range(6):
    print(name)


2. test = range(1, 5)
for count in test:
    print(count)

1
2
3
4

fruit_list = ['banana', 'orange', 'apple']  
for y in fruit_list:
print(y)


for X in [2,4,6,8,10]:
print(x)

num_list = [[1,2,3], [10,20,30], [100,200,300]]

for x in range(0,3):
for y in range(0,3):
	print(num_list[x][y])



To flatten the nested list x into a single list:-
x = [[1,2,3,4],1,2,3,[10,[1,2,3],20,30],[9,15,25]]
flat_lst = []
for i in range(0,len(x)):
    if isinstance(x[i],list):
        for j in range(0, len(x[i])):
            if isinstance(x[i][j],list):
                for k in range(0,len(x[i][j])):
                    if isinstance(x[i][j],list):
                        flat_lst.append(x[i][j][k])
                    else:
                        flat_lst.append(x[i][j][k])
            else:
                flat_lst.append(x[i][j])   
    else:
        flat_lst.append(x[i])
print(flat_lst)

Another method:
def flat_list(x):
    flat_lst = []

    def flatten(item):
        if isinstance(item,list):
            for i in item:
                flatten(i)
        else:
            flat_lst.append(item)

    flatten(x)
    return flat_lst

print(flat_list(x))
#[1, 2, 3, 4, 1, 2, 3, 10, 1, 2, 3, 20, 30, 9, 15, 25]

Functions in python - functions are user specific.
Functions are reusable pieces of programs
A method is a function that ‘belongs’ to an object and is named obj.methodname,

def say_hello():
# block belonging to the function
print 'hello world'
# End of function
say_hello() # ====> call the function

If user wants to pass a default value to the function,
>>> def add(x=10,y=20):
	sum=x+y
	print(sum)

	
>>> add()
30
>>> add(100,50)
150
>>>

To create our own functions as follows:
1. >>> def example():
	print("Welcome to my function")

>>> example()
Welcome to my function
>>>

2.>>> def addition():
	n1 = int(input("Enter number 1: "))
	n2 = int(input("Enter number 2: "))
	n3 = n1 + n2
	print(n3)

3. >>> def sub():
	n1 = int(input("Enter number 1: "))
	n2 = int(input("Enter number 2: "))
	n3 = n1 - n2
	print(n3)

	
>>> addition()
Enter number 1: 2
Enter number 2: 5
7
>>> sub()
Enter number 1: 5
Enter number 2: 7
-2
>>> sub()
Enter number 1: 5
Enter number 2: 2
3

functions with arguments: Now we will use how to pass the arguments as follows:
argument – value passed in to the function body when it is invoked.
Parameter –values inside the function.


>>> def addition(n1, n2): # passing the data type n1 and n2
	n3 = n1 + n2
	print(n3)
>>> addition(2,4)    

>>function (*arg, **kwarg)
Arg – any number of arguments can be passed for a parameter ( a tuple can be passed as an argument)
Kwargs –argument as a key-value pair (interpreter will create a dictionary)

>>> def new(shop, *items, **pricelist):
	print(name)
	print(items)
	print(pricelist)
>>> new('ABC','a','b','c',a=10,b=20,c=30)
x
('a', 'b', 'c')
{'c': 30, 'a': 10, 'b': 20}
>>>
Modules:-
module: is bundle of functions
package will have multiple modules .modules will have multiple functions , functions have a piece of executable code

The difference between function and module: function is user specific & defined by user, function would be used, called and used within the code.
function could be invoked within the users but modules are used with multiple users

creating modules and importing in our program:
while importing module python interpreter searches for current directory , PYTHONPATH and then default path - /usr/local/lib/python/.
 
To reuse no of functions in program

To create our own module first we need to open a new file and save under python34 file nanme as mymath in case of windows
 /usr/local/lib/python  - incase of unix

create function with different  file names as  3 modules  as follows:
 first create directory called - modules and then create following file

1. def postline():
	print " I am landline phone - 2267"
 save it as post

2. def voipline():
	print " I am voip phone - 8182828"
 save it as voip.py

3. def cellline():
	print " I am cell phone 7338567673
save it as cell.py

so now we have created 3 modules under module directory so to have have relationship with these modules and packages we need to create source code called init - initialization which will have meaning of module and package
Create a file with file name -_init_.py
 now import the files
from modules import postline
from voip import voipline
from cell import cellline

store it with file extension - _init_.py
so now we can import package name called module  which has multiple module

 
>>> import mymath  -> module name is mymath
>>> mymath.addition(22,33)
55
>>> mymath.addition(3,5)
8
>>> mymath.division(10, 5)
2.0
>>> mymath.sub(5,10)
-5
>>>

>>> addition(3,5)  ---------------> Here package name is not mentioned so the sys get confused
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    addition(3,5)
NameError: name 'addition' is not defined
>>>

examples of builtin functions:
pow(2,3)
8
print("hello")
hello
max(47,33,22)
47
min(1,2,3)
1

To use the modules example - math so import the module and use the functions inside the module
The syntax is module name dot which give all functions available

import math
math.sqrt(9)
3.0

dir(_builtins_) give all built in functions
--------
Any file with extension .py is a module
Modules which come as part of interpreter are default modules. Eg : math, sys, os, io, random etc
Modules pre-written – need to install from PYPI.org
Custom made – written by users.

How to install a module: >>>>>>> try this
1)	Download module from pypi.python.org
-check for setup.py file or __init__.py
-run setup.py to install the module
      2)  Package installation
	- pip install <mod name>
	-for getting pip, python get-pip.py - > from command line

Difference btn module and package:
Module – a file with .py extn
Pkg – a directory which contains a lot of .py files
Package is a bundle of python modules of logical relevance
For getting the modifications in an existing package /module
>> reload(<module name>) or remove .pyc files and execute again

If __init__.py is not present, how to import modules in a package ?
>> from phonebook import land  >> phonebook –package, land - module
>> land.landphone()       >>> landphone - function/method


FILE handling: Reading files and writing files in the system

To open the file first we need to create an object or variable and method or function called open and specify the file 

open() - function lets u create object to read, write name and path to open & Append file
r- opens a file for reading
w - opens a new file for writing. If the file already exist, its old contents are destroyed.
a - opens a file for appending data from the end of the file.
'x'       create a new file and open it for writing
rb - opens a file for reading binary data
wb - opens a file for writing binary data.

r+  -Opens a file for both reading and writing. The file pointer placed at the beginning of the file
w+  -Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a+  -Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

File.closed – true/false,
File.name  , file.mode

>>> bo = open('c:/test_python/a.txt', 'w')
>>> bo.write('This is the file I want to use in python')
40
>>> bo.close()
>>> bo = open('c:/test_python/a.txt', 'r')
>>> bo.read()
'This is the file I want to use in python'
>>>

sreadlines() - read complete file in form of list of string, each a line from the file

How to rename or remove a file .. here for renaming we need to import os module
>>> import os
>>> os.rename('c:/test_python/b.txt' , 'c:/test_python/bbb.txt')
>>> os.remove('c:/test_python/bbb.txt')

>>> import os
>>> os.mkdir('test')
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir("newdir") -- to change the current directory to “newdir”
os.rmdir('dirname') -- deletes the directory, which is passed as an argument in the method.
Whe  u open a file,
Read/write mode -> file pointer is at the beginning of the file
Append –file pointer is at the end of the file

File methods:
Read() – read contents from the file ( as string) equal to byte size equal to max as of def buffer size.
For small files.
To find out def buffer size-
>>import io
>>io.DEFAULT_BUFFER_SIZE
8192 –max ‘read’ can read

>>fobj.read(10) – read 10 characters
>>fobj.tell() – gives file pointer position
10L
>>fobj.read(10) – reads next 10 characters, newline treated as one character
>>fobj.readline() –read line by line. retains new line
>>fobj.readlines() – for big files – as a list of strings
>>fobj.seek(offset [,from]) => keep the curser based on the values passed. 
 if from =0 , start from beginning of the file, from=1, use current position as the ref point, from=2, end of file as ref point, offset –how many bytes you want to move
>>fobj.write(“ “) – write contents to file. If u mark it as raw string(r”dsfds”) no newline processed for \n
>>fobj.close()
>>next(fobj) -- Returns the next line from the file each time it is being called.
# Open a file
fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)

for index in range(5):
   line = next(fo)
   print ("Line No %d - %s" % (index, line))

# Close opened file
>>fo.close()
>>file.truncate([size] -- If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position.
>>file.writelines(sequence) -- Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.
# Open a file in read/write mode
fo = open("abc.txt", "r+")
print ("Name of the file: ", fo.name)

seq = ["This is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
line = fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(0,0)
   for index in range(7):
      line = next(fo)
      print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()

Binary files: jpeg,png
Compression type MIMO – multiple input multiple output
Extn - .dat
For binary files, import module ‘codecs’ (coding and decoding)
>> import codecx
>>fobj=codecs.open(“file.dat”, ’rb’, ‘utf-8’)  
For xml files – xmlconfig module

-- how to read from lines starting from a specific word ?
for files in filepath:
    with open(files, 'r') as f:
        for line in f:
            if 'Abstract' in line:                
                for line in f: # now you are at the lines you want
                    # do work

Eg:
>>> def ff(filename):
	with open(filename, 'r') as fobj:
		for line in fobj:
			if 'classic' in line:
				for line in fobj:
					print(line)
fobj.close()
					
>>>ff('C:\\Users\\sonjose\\Documents\\APIC_EM\\notepad\\Python\\python_scripts.txt')   # use \\ to avoid special meaning of ‘\’

5.666666666666667

>>> 17 // 3  # floor division

5
---------------------------------------------------------------
>>> fobj=open(r'C:\Users\sonjose\Documents\APIC-EM\notepad\Python\python_scripts.txt', 'r') -> pass file name as raw string to avoid special meaning of ‘\’
>>> fobj.read()
'http://career.guru99.com/top-25-python-interview-questions/\n\n>>> # Fibonacci series: 1 1 2 3 5 8\n... # the sum of two elements defines the next\n... a, b = 0, 1\n>>> while b < 10:\n...     print(b)\n...     a, b = b, a+b\n...\n\n# Python 3: Fibonacci series up to n\n>>> def fib(n):\n>>>     a, b = 0, 1\n>>>     while a < n:\n>>> 
>>> fobj.tell()
3246
>>> fobj.seek(10,0)
10
>>> fobj.seek(0,0)
0
>>> fobj.read(10)
'http://car'
>>> 
>>> fobj.readline()
'eer.guru99.com/top-25-python-interview-questions/\n'
>>> fobj.readline()
'\n'
>>> fobj.readline()
'>>> # Fibonacci series: 1 1 2 3 5 8\n'
>>> fobj.readlines()
['... # the sum of two elements defines the next\n', '... a, b = 0, 1\n', '>>> while b < 10:\n', '...     print(b)\n', '...     a, b = b, a+b\n', '...\n', '\n', '# Python 3: Fibonacci series up to n\n', '>>> def fib(n):\n', '>>>     a, b = 0, 1\n', '>>>     while a < n:\n', ">>>         print(a, end=' ')\n", '>>>         a, b = b, a+b\n']

Exception Handling: during execution any error comes, to catch the error at the step, exceptions are used
Exceptions can be caught in the program using try and except statements.
try and except should be in same indentation

An exception is a python object that represents an error.
ZeroDivisionError, NameError and TypeErro are examples of exceptions.

try - To execute the code below
Except - catches all error or specific error

try:
operations here
except Exception1:
	if there is exception1, execute this code block
except Exception2:
	if there is exception2, execute this code block
else:
	If there is no exception, then execute this block


Try-finally

Try:
	Operations here. Due to any exception, this may be skipped
Finally:
	This would always be executed

To handle unexpected error, exception handling and assertions are used.
Assertion is a sanity-check that you can turn on or turn off when you are done with ur testing of the program.

Assert Expression [Arguments] -> If it fails, argument is used as the arg for assertion error. An expression is tested, and if the result comes up false, an AssertionError exception is raised.


Raising an exception:
Raise [exception [,args[,traceback]]]
An exception can be a class, object or a string.

Custom Error Messages: Raising exceptions with custom messages can provide more context about the nature of the error, which can be helpful for debugging and logging.

def validate_age(age): 
if age < 0: 
raise Exception("Age cannot be negative")

User defined exceptions:
Creating Custom Exceptions: Although raise Exception is a general way to signal errors, Python allows you to define your own custom exception classes by subclassing the built-in Exception class. This can make error handling more specific and meaningful.

class MyCustomError(Exception): 
def __init__(self, message):	
super().__init__(message) 
def some_function(): 
raise MyCustomError("Something went wrong in my function")

>>> x = 5 + 'Ram'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x = 5 + 'Ram'
TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    x = 5 + "Ram"
except:
    print ("Error occurred")
    
output:
Error occurred
>>>
==================
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

pass: saying to ignore and move on though error occurred

   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

Functions in python:

## Define function ##
def welcome ():
    print("welcome to python")

def add ():
    n1 = int(input("enter first no: "))
    n2 = int(input("enter second no: "))
    n3 = n1 + n2
    print(n3)

## Define function with passing argument ##

def add (n1, n2):
    n1


Global vs. Local variables

Variables defined inside a function body are local variables, and those defined outside are global variables.

local variable can be accessed only inside the function  where as global variable can be accessed throughout the program by all function

Realtime example - it can be used for declaring device names & testbed names or vlan 10 needs to called in all the API
Like mandatory arguments in cisco scripts

globals () & locals () functions
locals  ()  - lists out all local variable accessible within the function
globals()  -" global variables "

Print(locals()) – prints all local variables as dictionary
Print(globals()) – prints all global variables as dictionary

>>> m=100     >> m defined outside function
>>> print(m)
100
>>> def doublemoney():
	global m      >>> m defined as global inside function
	m=m*2
	print(m)

	
>>> doublemoney()    === > m got the defined value
200
>>> 
>>> def newmoney():
	m=m+50
	print(m)

	
>>> newmoney()        >>>>>>>> m is not defined as global inside the function
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    newmoney()
  File "<pyshell#22>", line 2, in newmoney
    m=m+50
UnboundLocalError: local variable 'm' referenced before assignment
>>> 
>>> def newmoney():
	global m       
	m=m+50
	print(m)

	
>>> newmoney()
250
>>>
global dutA, dutB, dutC, dutD, TGEN
sample as follows:
total = 0   
def sum (arg1, arg2):
    total = arg1 + arg2 
    print("Inside funct ans:", total)
    return total

sum (10, 20)
print("outside funct ans:", total)
output as follows:
Inside funct ans: 30   ---> local variable
outside funct ans: 0 --> Global variable

-------------------
-------------------
>>> total = 0
>>> def sum (arg1, arg2):
    total = arg1 + arg2
    print("Inside funct ans:", total)
    return total

>>> sum(10,20)
Inside funct ans: 30
30
>>> total
0
>>> global total
>>> sum(20,30)
Inside funct ans: 50
50
>>> total
0
>>> def sum (arg1, arg2):
	global total
	total = arg1 + arg2
	print("Inside funct ans:", total)
	return total

>>> sum (100,200)
Inside funct ans: 300
300
>>> total
300

class & objects - Classes Are Like Modules
https://www.tutorialspoint.com/python3/python_classes_objects.htm

class is a group of variables and functions together
A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

class is a template, class contains data types and function(it will group the datatypes and functions)
we will define data types and functions  inside the class, to access the function inside the class  using the object
 

object: is instance of class- all the function inside the class  would be accessed by using the object
Objects are Like Import *************
** Each object copy of its class, Each of object is independent on one another

with the help of object only functions inside the class would be called.

class name:
     class variable
  
   member function()
	member variable

 object for the class

object = name()
 object.member_function()



To create a class:
class student:  #  here class is the key word is class, student is the class name, so what ever the variable under student are part of this. self here is whenever object is created  system automatically passes self as object
	def details(self,name, age):   # functions defining name is def
	self.age = age
	self.name = name
	print("the name is {} and the age is {}".format(name,age))

so here above class is created below object will be created as follows:

s1 = student()  # object is created
s1.details("collin",35) # now we can access the function is details from the class
==============
class student:
    def details(self,name,age):
        self.age = age
        self.name = name
        print("the name is {} and the age is {}".format(name, age))
        

>>> s1 = student()
>>> s1.details("collin",35)
the name is collin and the age is 35
>>> s1.name
'collin'
>>> s1.age
35
>>> s1.details


Methods:
=======
Constructor is a special method, It will be invoked while creating an object
synt: def _ _init _ _ (self)
	print "hello"
          def fun total()

	print "hello 2"

_init_ is the key word for constructor
Destroy will remove all the memory allocation by constructor
it is inbuilt in python



 Constructor method: whenever we create the object  constructor function is automatically called. See below example
construcor functions are useful to initialize the initial values
class – It is a user defined prototype for an object, that defines a set of attributes that characterize any object of the class. 
Object –A unique instance of a data structure that is defined by its class. An object comprises of both data members and methods.
One class can make any number of objects with a common behavior.
Class = attributes + methods
Attributes -> are data members (class variables &instance variables) and methods.
Data member – A class variable or instance variable that holds data associated with a class and its objects.
Class variables- shared by all instances of a class. Defined within a class, but outside methods
Instance variables- var defined inside a method and belongs only to the current instance of a class.
Methods -> functions written inside a class
Method(self) -> self arg is mandatory
Self is a temporary place holder for the object.
>>print self in the method will give memory location of the object
Function overloading –Assignment of more than one behavior to a particular function >>>>> get more details
Inheritance – transfer of characteristics of a class to other classes that are derived from it.
Instance – an individual object of a certain class
Operator overloading –Assignment of more than one function to a particular operator.
__init__() – class constructor or initialization method that python calls when u create a new instance of the class.
-first argument to each method is self. When we call the method, python adds self arg, so no need to add it.

-	getattr(obj,name[,default] – to access the attributes of the object
-	hasattr(obj, name,value)
-	delattr(object,name)

class Person: 
def __init__(self, name, age): 
self.name = name 
self.age = age 

person = Person("Alice", 30) 
# Accessing attributes directly 
print(person.name) # Output: Alice 
print(person.age) # Output: 30 
# Accessing attributes using getattr 
print(getattr(person, 'name')) # Output: Alice 
print(getattr(person, 'age')) # Output: 30
print(hasattr(obj, 'msg')) ## True

print(delattr(obj, 'msg')) ## None

Inheritance:

Parent class in parenthesis after a new class name. Child class inherits attributes of its parent class.
- issubclass(sub,sup) – true if ‘sub’ is a subclass of the super class ‘sup’
- isinstance(obj, class) –true if ‘obj’ is an instance of a sub class of ‘class’
__repr__(self) – evaluable string representation. Eg : repr(obj)
__cmp__(self,x) – object comparison. Eg : cmp(obj,x)

class parent1: 
    var1 = "parent1 var1"
    var2 = "parent1 var2"

class parent2:
    var1 = "parent2 var1"

class child(parent1,parent2):
    var3 = " child var3"
    var1 = "child var1"
>>> p1=parent1()
>>> p2=parent2()
>>> c=child()
>>> c.var1           >>>> var1 is overwritten by child
'child var1'
>>> p1.var1
'parent1 var1'
>>> p2.var1
'parent2 var1'
>>> c.var3
' child var3'
>>> c.var2
'parent1 var2'
>>>

__init__ - > constructor
__del__ -> destructor

-Single inheritance – One parent + children

class parent1:
    def __init__(self):
        self.var1 = "parent1 var1"
        self.var2 = "parent1 var2"

class child1(parent1):
    def __int__(self):
        parent1.__init__(self) #without super, needs parent class name

class child2(parent1):
    def __init__(self):
        super(child2,self).__init__() #avoid using parent class name 

>>> c1=child1()
>>> c2=child2()
>>> c1.var1
'parent1 var1'
>>> c2.var1
'parent1 var1'
>>>
Super() :
Case1 : linear/simple inheritance

Parent1    parent2   parent3
    |________|_______|
                        |
                    child
Case2:  
Method resolution order(MRO)
Child (parent3, parent2, parent1)
Only available when we use super()

Case3:
Diamond structure

Method resolution order (MRO):
Var/method with same name across multiple parent classes-
Class child(parent1, parent2):
Here, child will get values from parent1. 
The way of resolving this conflict is known as MRO.

access specifier for a method or variable. 
3 types
-public – no ‘Underscore’ 
-protected – one ‘Underscore’  prefixed
-private – 2 ‘Underscores’  prefixed
Public:
Variable is available beyond parent class and child class
Protected:
_var or _method
Only accessible in parent and child class
Private :
__var
Only available inside the base class and its objects. NOT in child class
class access:
    def __init__(self,a,b,c):
        self.public=a
        self._protected=b
        self.__private=c
>>> obj=access(1,2,3)
>>> obj.public
1
>>> obj._protected
2
>>> obj.__private()       >>> cannot access outside the class
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    obj.__private()
AttributeError: 'access' object has no attribute '__private'
>>> 
How to access a private variable outside a class ?
 ( Name mangling - > object. _<class name><private variable>

>>> obj._access__private
3
>>>
Name mangling in Python is a mechanism used to avoid name conflicts in classes by altering the names of attributes with a double underscore prefix. This technique helps to ensure that attribute names in subclasses do not accidentally clash with names in the base class.
 
### How Name Mangling Works
 
In Python, if you prefix an attribute name with two underscores (`__`), Python performs name mangling to make the attribute name unique. This helps prevent accidental name collisions in subclasses or when dealing with inheritance.
 
Here’s how name mangling transforms attribute names:
 
- If an attribute is named `__attr` in a class `MyClass`, it will be internally mangled to `_MyClass__attr`.
 
### Example
 
Consider the following example to understand name mangling:
 
```python
class Base:
    def __init__(self):
        self.__private = "This is private"
    
    def get_private(self):
        return self.__private
 
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "This is also private in Derived"
 
base = Base()
derived = Derived()
 
print(base.get_private())  # Output: This is private
print(derived.get_private())  # Output: This is private
 
print(base.__dict__)  # Output: {'_Base__private': 'This is private'}
print(derived.__dict__)  # Output: {'_Derived__private': 'This is also private in Derived'}
```
 
### Explanation
 
1. **In the `Base` Class**:
   - `__private` is mangled to `_Base__private`.
   
2. **In the `Derived` Class**:
   - `__private` is mangled to `_Derived__private`.
 
### Accessing Mangled Attributes
 
Although name mangling makes it harder to accidentally access private attributes, they are still accessible if you know the mangled names:
 
```python
print(base._Base__private)  # Output: This is private
print(derived._Derived__private)  # Output: This is also private in Derived
```
 
### When to Use Name Mangling
 
- **Encapsulation**: Name mangling is used to hide implementation details within a class, preventing accidental access or modification by subclasses.
- **Avoiding Conflicts**: It helps in avoiding conflicts between attribute names in parent and child classes.
 
### Limitations
 
- **Not True Privacy**: Name mangling does not provide true encapsulation or security. It merely makes it harder to accidentally access or override attributes.
- **Not a Replacement for Proper Design**: It should not be used as a substitute for proper design principles. Public and protected attributes should be used with thoughtful design.
 
### Conclusion
 
Name mangling is a useful feature in Python to help manage and avoid attribute name conflicts, especially in inheritance scenarios. It helps maintain cleaner and more manageable code but should be used judiciously as part of a well-thought-out class design.

Magic methods – implementation type methods => operator overloading >>>>> Magic methods in Python, also known as dunder methods (short for "double underscore"), are special methods that begin and end with double underscores (`__`). They allow you to define or customize the behavior of objects in various contexts and integrate with Python’s built-in operations and functions.
 
Here’s a look at some common categories and examples of magic methods:
 
### Object Initialization and Representation
 
- **`__init__(self, ...)`**: Initializes a new instance of the class. This is the constructor method.
 
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    ```
 
- **`__repr__(self)`**: Returns a string representation of the object that is meant to be unambiguous and helpful for debugging. Often used in conjunction with `__str__`.
 
    ```python
    class Person:
        def __repr__(self):
            return f"Person(name={self.name!r}, age={self.age!r})"
    ```
 
- **`__str__(self)`**: Returns a string representation of the object that is meant to be readable and user-friendly. This is what `print()` uses.
 
    ```python
    class Person:
        def __str__(self):
            return f"{self.name} is {self.age} years old"
    ```
 
### Attribute Access and Modification
 
- **`__getattr__(self, name)`**: Called when trying to access an attribute that does not exist.
 
    ```python
    class MyClass:
        def __getattr__(self, name):
            return f"Attribute {name} not found"
    ```
 
- **`__setattr__(self, name, value)`**: Called when setting an attribute. Useful for validating or controlling attribute assignment.
 
    ```python
    class MyClass:
        def __setattr__(self, name, value):
            if name == 'age' and value < 0:
                raise ValueError("Age cannot be negative")
            super().__setattr__(name, value)
    ```
 
- **`__delattr__(self, name)`**: Called when deleting an attribute.
 
    ```python
    class MyClass:
        def __delattr__(self, name):
            print(f"Deleting {name}")
            super().__delattr__(name)
    ```
 
### Arithmetic and Comparison Operations
 
- **`__add__(self, other)`**: Defines behavior for the addition operator `+`.
 
    ```python
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
 
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
    ```
 
- **`__eq__(self, other)`**: Defines behavior for equality comparison `==`.
 
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
 
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
    ```
 
- **`__lt__(self, other)`**: Defines behavior for less-than comparison `<`.
 
    ```python
    class Number:
        def __init__(self, value):
            self.value = value
 
        def __lt__(self, other):
            return self.value < other.value
    ```
 
### Container Behavior
 
- **`__len__(self)`**: Returns the length of the object, used by the `len()` function.
 
    ```python
    class MyList:
        def __init__(self, *items):
            self.items = list(items)
 
        def __len__(self):
            return len(self.items)
    ```
 
- **`__getitem__(self, key)`**: Accesses an item using square brackets, e.g., `obj[key]`.
 
    ```python
    class MyContainer:
        def __init__(self, items):
            self.items = items
 
        def __getitem__(self, index):
            return self.items[index]
    ```
 
- **`__setitem__(self, key, value)`**: Sets an item using square brackets, e.g., `obj[key] = value`.
 
    ```python
    class MyContainer:
        def __init__(self):
            self.data = {}
 
        def __setitem__(self, key, value):
            self.data[key] = value
    ```
 
### Context Managers
 
- **`__enter__(self)`** and **`__exit__(self, exc_type, exc_value, traceback)`**: Define behavior for context managers used in `with` statements.
 
    ```python
    class MyContextManager:
        def __enter__(self):
            print("Entering the context")
            return self
 
        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting the context")
            return False  # Propagate exceptions, if any
    ```
 
### Callable Objects
 
- **`__call__(self, ...)`**: Allows an instance of a class to be called as if it were a function.
 
    ```python
    class CallableClass:
        def __call__(self, *args, **kwargs):
            return f"Called with arguments {args} and keyword arguments {kwargs}"
    ```
 
### Summary
 
Magic methods provide hooks into the core language features of Python, allowing you to customize object behavior in a flexible and powerful way. They enable you to define how objects interact with operators, built-in functions, and context managers, making your classes integrate smoothly with Python’s data model.

Data hiding:
 Prefix attribute name with double underscore, those would not be directly visible to outsiders.
Pyhton protects those members by internally changing the name to include the class name. to access,
Object._classname__attrname.
Data hiding is done by access specifiers.



Destroying objects: Garbage collection
The process by which python periodically reclaims blocks of memory that no longer are in use is termed as garbage collection
 A class can use a special method called __del__(), called destructor, that is invoked when the instance is about to be destroyed.
-----------------------------------------
string
long_string = "I'll come to your desk"
print(long_string[0:4]) # will print first four charater
print(long_string[-5:]) #last five character
print(long_string[:-5]) #print everything till last 5 character

output:
I'll
 desk
I'll come to your

Regular expression
re - stands for regular expression
re.match : If anything match at the beginning of the string and return a match object.
re.search: match any where in the string
re.findall- is goign to find all of the matches and return as the list

import re
re.match(pattern, string, flags=0)
match function, search function
re.sub(pattern, repl, string, max=0)- search and replace

pattens- This is the regular expression to be matched.
string - This is the string, which would be searched to match the pattern at the beginning of string.
flags - You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

for match
>>> ma = re.search('trace', 'traceback found')
>>> ma.group()
'trace'
>>> output = "Cisco IOS Software, IOS-XE Software, 5700 Series Wireless LAN Controller Software (CT5760-IPSERVICESK9-M), Version 03.06.05.E.649 EARLY DEPLOYMENT [PROD BUILD]"
>>> match = re.search('IPSERVICESK9', output)
>>> match.group()
'IPSERVICESK9'
>>>
Version 15.2(4.5.09)EC
>>> match = re.search('Version [0-9]+\.[0-9]+\([0-9]+\.[0-9]+\.[0-9]+\)[A-Z0-9]+', ver)
>>> match.group()
'Version 15.2(2.4.34)E1'
>>> ver
'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 15.2(2.4.34)E1, TEST DEV IMAGE ENGINEERING ESTG_WEEKLY'
>>>

example for find all
====================
>>> mail = "ramesh@cisco.com, test@cisco.com"
>>> output = re.search('[\w\.]+@[\w\.]+', mail)
>>> output.group()
'ramesh@cisco.com'
>>> output = re.findall('[\w\.]+@[\w\.]+', mail)
>>> output
['ramesh@cisco.com', 'test@cisco.com']  ## Returned as a list
>>>

str1 = 'one abc@gmail.com twothree pqr@abc.com'
matchobj=re.search(r'\w+@\w+' , str1)
to search including dot need to use square bracket as follows:
matchobj=re.search(r'[\w.]+@[\w.]+]' , str1)

for multiple matches  can use find all as follows:

w+ - any no of word character
>>> output = re.findall('([\w\.]+)@([\w\.]+)', mail)
>>> output
[('ramesh', 'cisco.com'), ('test', 'cisco.com')]  ## returned as Tuple

>>> string
' jessica is 15 years old, and Daniel is 27 years old. Edward is 97, and his grandfather, Oscar, is 102.'

>>> age = re.findall(r'\d{1,3}', string)
>>> print(age)
['15', '27', '97', '102']

>>> names = re.findall(r'[A-Z][a-z]*', string)
>>> print(names)
['Daniel', 'Edward', 'Oscar']
>>>  

re.I -> case sensitive:
==============
>>> str = "we are planning to learn Python"
>>> str
'we are planning to learn Python'
>>> output = re.search('python', str)
>>> output
>>> output.group()
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    output.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> output
>>> output = re.search('python', str, re.I)
>>> output
<_sre.SRE_Match object; span=(25, 31), match='Python'>
>>> output.group()
'Python'
>>>

Search and Replace   -re methods that use regular expressions is sub -- substituting
==================
re.sub(pattern, repl, string, max=0)
>>> phno = "080-393-3939"
>>> phno
'080-393-3939'
>>> output = re.sub('\D', '', phno)  ##D - match no digit or # Remove anything other than digits
>>> output
'0803933939'
>>>

Example for substring match
===========================
>>> output1 = "Cisco IOS Software, IOS-XE Software, 5700 Series Wireless LAN Controller Software (CT5760-IPSERVICESK9-M), Version 03.06.05.E.649 EARLY DEPLOYMENT [PROD BUILD]"
>>> match = re.search('Version ([0-9A-E\.]+)' , output)
>>> match.group(0) ###Gives full match
'Version 03.06.05.E.649'
>>> match.group(1) ### Gives substring match in case more sub string it will go on like group1, group2, group3
'03.06.05.E.649'
>>>

quantifier->  + * ?
+ 1 or more occurrences of the pattern to its left,
* 0 or more occurrence of the pattern to its left
? match 0 or 1 occurrences of the pattern to its left
  
line ="we are all learning python"
matchobj = re.match(r' (.*) (.*) all (.*) (.*)' ,line)
matchobj.group()

\.    dot match any character
=============================
>>> match = re.search('...k', 'traceback found') ##any three character and end with k
>>> match.group()
'back'

. -> any character except for a new line

>>> match = re.search(r'c\.l', 'c.lled piig') ## r' is for raw string
>>> match.group()
'c.l'

\w    lower w -word  any character
====================
\w+ (+ indicates one or more characters)
>>> match = re.search(r':\w', 'blah :cat blah blah')
>>> match.group()
':c'
>>> match = re.search(r':\w\w', 'blah :cat blah blah')
>>> match.group()
':ca'
>>> match = re.search(r':\w\w\w', 'blah :cat blah blah')
>>> match.group()
':cat'
>>>
\W - anything but a charater
\d -- any numbers (decimal digit [0-9])
===============================
\d{1,3} -- it match any digit exam: 123
>>> match = re.search(r':\d\d\d', 'blah :123blah blah blah')
>>> match.group()
':123'
\D -- anthing but a number
\s -- matches a single whitespace character -- space character
===========================================================================
>>> match = re.search(r':\d\s\d\s\d', 'blah :1 2 3 blah blah blah')
>>> match.group()
':1 2 3'

\S -- capital s for non white space character (anything but a space)
===================================================
>>> match = re.search(r':\S+', 'blah blah :kittan123123&a=123&yatta')
>>> match.group()
':kittan123123&a=123&yatta'

+ 1 or more character
=================================
>>> match = re.search(r':\w+', 'blah :kittan123   blah blah blah')
>>> match.group()
':kittan123'
>>> match = re.search(r':.+', 'blah :kittan123   blah blah blah')
>>> match.group()
':kittan123   blah blah blah'
>>>

- 0 or more character
==================================
[...] Matches any single character in brackets.
[^...] Matches any single character not in brackets
re*    Matches 0 or more occurrences of preceding expression.
re+    Matches 1 or more occurrence of preceding expression.

^ Anchor the pattern to the beginning of the string. Only when first.
$ Anchor the pattern to the end of the string. Only when last


str = "+91 - 7338567673", This is my no "  -> want only digit


Ip address match
==================
>>> match = re.match('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', ip)
>>> match.group()
'192.168.1.0'
>>> ip = '192.168.1.92'
>>> match = re.match('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', ip)
>>> match.group()
'192.168.1.92'
>>>

IP validation:
ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)$'
250-255 | 200-249| 199-1 
Mac adress:
============
>>> mac = '00:27:0e:2a:b9:aa'
>>> match = re.match('[0-9a-z]+\:[0-9a-z]+\:[0-9a-z]+\:[0-9a-z]+\:[0-9a-z]+\:[0-9a-z]+', mac)
>>> match.group()
'00:27:0e:2a:b9:aa'

>>> x = re.match('([0-9a-z]+\:){5}[0-9a-z]+', mac,re.I)
>>> match.group()
'00:27:0e:2a:b9:aa'
>>>

modifier:
===========
+ match one or more
? match 0 or 1
* match 0 or more
$ match the end of the string or end of line
^ match the begin of a string or begining of line
| either or
[] range or variance [A-Z]

white space character:
======================
\n  new line
\s space
\t tab
\e escape
\r return

Dont forget:
@@@@@@@@@@@@
. + * ? [] $ ^ () {} | \

++++++++++++++++++++++++++++++++++++++++++
1. what is python ? what are the benefits of using of python ?
Advantage :
	Easy syntax, Readability, object oriented programming - allows u to create data structures that can be re-used
	python is free, cross-platform - it can run on all major operating system
	python is widely supported
	Python offers excellent support for dictionaries

Define list with example
Loop the list  & print it
Define tuple with example  & print it
Define dictionaries with example & print it
Define string with example & print it

2. How python interpreted ?
Python is executed by an interpreter instead of compilation

what are python decorators ?
how are arguments passed by value or by references ?

In Python, the concepts of "passing by value" and "passing by reference" are a bit nuanced because Python uses a model of **pass-by-object-reference** or **pass-by-sharing**. Here's a breakdown of how this works:
 
### Pass-by-Object-Reference (or Pass-by-Sharing)
 
In Python, when you pass an argument to a function, you are actually passing a reference to the object, not the actual object itself. However, this reference is passed by value, meaning that the reference itself is a copy. Here's what this means in practice:
 
- **Mutable Objects**: If you pass a mutable object (like a list or a dictionary) to a function, the function can modify the object in place. Since both the original reference and the function's reference point to the same object, changes made to the object inside the function are reflected outside the function.
 
- **Immutable Objects**: If you pass an immutable object (like an integer, string, or tuple) to a function, you cannot modify the object itself. Any operation that seems to "change" the object actually creates a new object. Since the reference is passed by value, the function cannot affect the original immutable object outside the function.
 
### Examples
 
Here are some examples to illustrate these points:
 
#### Example 1: Mutable Object (List)
 
```python
def modify_list(lst):
    lst.append(4)
 
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```
 
In this case, `modify_list` modifies the list in place. The changes are visible outside the function because `lst` and `my_list` refer to the same list object.
 
#### Example 2: Immutable Object (Integer)
 
```python
def modify_number(num):
    num += 1
 
my_number = 10
modify_number(my_number)
print(my_number)  # Output: 10
```
 
Here, `modify_number` does not change `my_number` because integers are immutable. The operation `num += 1` creates a new integer object and reassigns `num` to this new object. `my_number` remains unchanged.
 
### Summary
 
- **Passing References**: Python passes references to objects, not the objects themselves. This means that the function receives a reference to the same object.
  
- **Mutability**: The behavior you observe depends on whether the object is mutable or immutable:
  - **Mutable Objects**: Changes made inside the function are reflected outside the function.
  - **Immutable Objects**: Changes inside the function do not affect the original object.
 
In essence, while Python's argument passing model might be called "pass-by-reference," it's more accurate to describe it as "pass-by-object-reference" or "pass-by-sharing," where the reference to the object is passed by value.

what are dictionaries and list comprehensions?
A way of creating lists which obey some special patterns or expressions

what is the name space in python ?
In Python, a **namespace** is a container that holds a collection of identifiers (names) and their corresponding objects (values). Namespaces ensure that names used in a program are unique and can be managed without conflict. They provide a way to organize and keep track of variables, functions, classes, and other objects in your code.
 
Here’s a deeper dive into namespaces in Python:
 
### Types of Namespaces
 
1. **Built-in Namespace**: This is created when the Python interpreter starts up and contains names such as `int`, `str`, `print`, and other built-in functions and exceptions. It is always available and can be accessed directly.
 
2. **Global Namespace**: This is created for each module or script. It contains names defined at the level of the module or script, including functions, variables, and classes defined outside of any function or class. Each module has its own global namespace.
 
3. **Local Namespace**: This is created within a function or a method. It contains names that are local to that function or method, including parameters and variables defined within it. Local namespaces are temporary and exist only while the function is executing.
 
4. **Enclosing Namespace**: This refers to the namespaces of any enclosing functions when using nested functions. It acts as an intermediate scope between the local and global namespaces.
 
### How Namespaces Work
 
When you access a name in Python, the interpreter looks for that name in the following order:
 
1. **Local Namespace**: If the name is found here, it is used.
2. **Enclosing Namespace(s)**: If the name is not found locally, Python checks the enclosing namespaces (for nested functions).
3. **Global Namespace**: If the name is still not found, Python checks the global namespace.
4. **Built-in Namespace**: If the name is not found in any of the above, Python checks the built-in namespace.
 
This process is known as the **LEGB Rule** (Local, Enclosing, Global, Built-in).
 
### Examples
 
#### Example of Built-in Namespace
 
```python
print(len)  # Output: <built-in function len>
```
 
Here, `len` is a name from the built-in namespace.
 
#### Example of Global Namespace
 
```python
x = 10  # x is in the global namespace
 
def my_function():
    print(x)  # Accessing x from the global namespace
 
my_function()  # Output: 10
```
 
In this example, `x` is defined in the global namespace and is accessible from within `my_function`.
 
#### Example of Local Namespace
 
```python
def my_function():
    x = 10  # x is in the local namespace of my_function
    print(x)
 
my_function()  # Output: 10
print(x)  # Raises NameError: name 'x' is not defined
```
 
Here, `x` is local to `my_function` and is not accessible outside it.
 
#### Example of Enclosing Namespace
 
```python
def outer_function():
    x = 20  # x is in the enclosing namespace
 
    def inner_function():
        print(x)  # Accessing x from the enclosing namespace
 
    inner_function()
 
outer_function()  # Output: 20
```
 
In this example, `x` is in the namespace of `outer_function`, and `inner_function` has access to it.
 
### Managing Namespaces
 
- **Global Variables**: Use the `global` keyword to modify global variables inside a function.
- **Local Variables**: Defined within a function or a method, and only accessible within that function or method.
- **Nonlocal Variables**: Use the `nonlocal` keyword to modify variables in an enclosing (non-global) scope.
 
### Conclusion
 
Namespaces are fundamental in Python for managing and organizing names and their associated objects. They prevent name collisions and provide a clear structure to code by separating different scopes of names. Understanding how namespaces work helps in writing clear and error-free Python programs.


1. how to run python script
ANS:easypy myJobfile.py

2. python is interpreter or compiler ?
python is an interpreter language


3.how to create module - packages ?
simply create a new.py file and save as  with module name and then import the module name using import command


4. how to define list
A list is an ordered set of elements enclosed in square brackets
list = ['item1', 'item2', 'item3']


5. difference between tuple and dictionary
#list
l = [1,2,3]

# Tuple
t = (1,2,3)

#Dictonaries
d = {'key':'value','key2':'value2'}
A Tuple's values cannot be changed, added, or removed, they are like sticky constant values
A Dictionaries values are like an associative array, meaning you give every item a Key and a Value.

6. how do u define tuple
x = 5,6,2,6
or
x = (5,6,2,6)



8. where we use curly braces {  - > Dictionaries in python and square bracket is list  in python
8) What is the difference between list and tuple?

The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.

11) What are the built-in types python providing?

There are mutable and Immutable types of Pythons built in types 
Mutable built-in types

List
Sets
Dictionaries

Immutable built-in types
Strings
Tuples
Number

In order to convert a number into a string, use the inbuilt function str().  If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().


25) What is module and package in Python?
A Python file with some functions or variables in it ..
You import that file.
And you can access the functions or variables in that module with the . (dot) operator.

In Python, module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.

The folder of Python program is a package of modules.  A package can have modules or subfolders.


What are tuples in Python?
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.


What is the difference between tuples and lists in Python?
The main differences between lists and tuples are - Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.


What are Python's dictionaries?
Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.


How will you create a dictionary in python?
Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

How will you get all the keys from the dictionary?
Using dictionary.keys() function, we can get all the keys from the dictionary object.

print dict.keys()   # Prints all the keys

How will you get all the values from the dictionary?
Using dictionary.values() function, we can get all the values from the dictionary object.

print dict.values()   # Prints all the values


How will you get the length of the string?
len(string) - Returns the length of the string.


\ - escape sequence character in python
Data types class- variables holds the value of different data types
In python - it is object oriented. object including numbers, strings and functions

To Run the python - python program.py
If you want to specify more than one logical line on a single physical line, then you have to explicitly specify this using a semicolon ( ; ) which indicates the end of a logical line/

i = 5
print i

or

i = 5;
print i;

or

i = 5; print i;

Get input from user:
===================
print('your name pls')
name = sys.stdin.readline()
print('hello' , name)



What is module in python?
import re;  statement imports all the names defined in module re.  
from statements can be used to import specific names from a module.

What is package in python?
An import statement can import packages and each import package introduces a namespace.
import folder1.subfolder2.module1
OR
from folder1.subfolder2.module1 import names

To import a package, __init__.py  file must be present in each of the folders, subfolders.

 
Difference between lambda and def :

a. def can contain multiple expressions whereas lamda is a single expression function
b. def creates a function and assigns a name so as to call it later. lambda creates a function and returns the function itself
c. def can have return statement. lambda cannot have return statements
d. lambda can be used inside list, dictionary.

what is lamda ?
	lambda is an expression, not a statement.
	The lambda's body is similar to what we'd put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general than a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles larger tasks.
	>>>
>>> def f(x, y, z): return x + y + z

>>> f(2, 30, 400)
432
	
##in details
15. What are iterators in Python?
Iterators in Python are used to iterate over a group of elements, containers, like list. For a container to support iterator, it must provide __iter__().

18. What is slicing in Python?
Slicing in Python is a mechanism to select a range of items from Sequence types like strings, list, tuple, etc.

Example of slicing:

>>> l=[1,2,3,4,5]
>>> l[1:3]
[2, 3]
>>> l[1:-2]
[2, 3]
>>> l[-3:-1]      # negative indexes in slicing
[3, 4]

>>> s="Hello World"
>>> s[1:3]
'el'
>>> s[:-5]
'Hello '
>>> s[-5:]
'World'
 



================================
python Videos -- preparation
==========================


class ?
name reverse prog
palindram prog
how will you read file


How will you convert a string to a tuple in python?
tuple(s) - Converts s to a tuple.


to convert tupple to string ?
>>> tup = ('data', 'variabl', 'agent')
>>> tup
('data', 'variabl', 'agent')
>>> string = " ".join(tup)
>>> string
'data variabl agent'
>>>




How will you convert a string to a list in python?
list(s) - Converts s to a list.
>>> string = "Ramesh is good boy"
>>> list1 = string.split(" ")
>>> list1
['Ramesh', 'is', 'good', 'boy']
 

how will u convert list to string ?
>>> string = " ".join(list)
>>> string
'surendar is a good programmer'
>>> string = " ".join(list1)
>>> string
'Ramesh is good boy'
>>>

What is an immutable object?
In object-oriented and functional programming, an immutable object is an object whose state cannot be modified after it is created. This is in contrast to a mutable object, which can be modified after it is created.


Immutable class is a class which the state of its instances does not change once it is constructed. Immutable objects are especially useful in concurrent applications. Since they cannot change state, they cannot be corrupted by thread interference or observed in an inconsistent state

1. how sort works in python in case of list

>>> a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
>>> sorted(a)    #### iterable
[1, 2, 3, 6, 8, 9, 23, 45, 78]
>>> a.sort()
>>> a
[1, 2, 3, 6, 8, 9, 23, 45, 78]
>>>
>>> a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
>>> a.sort()    ##########> in pace sort, gives output as none
>>> a
[1, 2, 3, 6, 8, 9, 23, 45, 78]
>>> a.sort(reverse=True)
>>> a
[78, 45, 23, 9, 8, 6, 3, 2, 1]
>>>

when to use list  & set ?
list  are ordered where as set  are unordered
which of data type is good to use as follows ?
Time to access the element in list or set ?

looping & Branching:
 looping - It will iterate based on condition count control loop
 Branching - which will help u to select based on the condition

one way condition: if statement
	x = 10
	if x==10:

	if condition:
	st1 print"x is 10"
if condition:
	st1
	st2

else:
	st3
	st4

multiple condition:


if
	else:
if:
	else

class & objects:
# import the aetest module
from ats import aetest

# define a simple testcase by inheriting aetest.Testcase
class mytestcases(aetest.Testases):  # main Test case one

	@aetest.setup
	def setup(self):
		#pass
		self.a = 1	#

	@aetest.test      ## Decorator are mainly important
	def test_one(self):
		#pass
		self.a += 1

	@aetest.test
	def test_two(self):
		#pass
		self.a += 1

	@aetest.test
	def test_three(self):
		#pass
		self.a += 1

	@aetest.cleanup
	def cleanup(self):
		#pass

class mytestcaseTwo(myTestcase):  ## main testcase two
	pass


if_name_ == '_main_':
	aetest.main()

using steps: while executing to track of status tc's  in each steps with steps is used

class mytestcases(aetest.Testases):

	@aetest.setup
	def setup(self):
	    pass

	@aetest.test      
	def test_one(self,steps):
	    with steps.start('the first baby step') as s:  ## It stores in th variable s
		pass
	    with steps.start('the second baby step') as s: ## It stores in the variable s
		with s.start("crawl one") as ss:	   ## it is sub division of the steps
		pass

		
	@aetest.cleanup
	def cleanup(self):
		#pass



Connect devices:
from ats import aetest
from ats.topology import loader
from ats import tcl
testbed = loader.load('new_mytb.yaml')

>>>
>>> uut = testbed.devices['DUT']
>>> uut.connect()
exp_spawn telnet 10.65.217.172 2028
Trying 10.65.217.172...
Connected to 10.65.217.172.
Escape character is '^]'.

output = uut.execute('show ver')  # Version 15.2(4.5.09)EC

ver = re.search('Version [0-9]+\.[0-9]+\([0-9]+\.[0-9]+\.[0-9]+\)[A-Z0-9]+', output)
print(ver)
ver.group()
>>> ver.group()
'Version 15.2(4.5.09)EC'
uut.execute('show ip int bri')

Debugging in Python:
pdfb - standard python debugger
pdb - python Debugger.
pyexpect -

================================================================
To remove duplicate entries from list

>>> ram = [1,2,3,4,5,5,6,7,6,7,8,8,9,10]
>>> set(ram)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> names  = ['RAMESH', 'ramesh', 'suresh', 'ganesh']
>>> set(names)
{'RAMESH', 'suresh', 'ramesh', 'ganesh'}
>>> names  = ['ramesh', 'ramesh', 'suresh', 'ganesh']
>>> set(names)
{'suresh', 'ramesh', 'ganesh'}
>>>



==================

-> What is Dictionary , Tuple , explain the functionality with examples.
-> Define the proc or function for grepping the status of "show ip int br" o/p.
-> List and give one example for adding new element.
-> Traverse through the Dictionary by elements of that.
-> Explain the Class/Object with example.
-> Using the List Comprehension for defining list
-> How to grep the Interfaces which are in UP state.
-> Define the Function and its call in main program.



1> Regular Expression for IPv4.
2> Difference between Tuple & List.
3> Functions , Modules call and its flow.
4> Class , Instance of Class and explain with example.
5> Inheritance concept.
6> Given one list :
x = [1,2,3,4,5,2,3,6,5,6,6]
Write the python program to give the list except the number "2" from the above given list.
>>> x = [1,2,3,2,2,2,3,4]
>>> list(filter(lambda a: a != 2, x))
[1, 3, 3, 4]

OR
>>> x = [1, 2, 3, 4, 2, 2, 3]
>>> def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)
>>> remove_values_from_list(x, 2)
>>> x
[1, 3, 4, 3]

In Python, the `filter()` function is used to filter elements from an iterable based on a function that returns `True` or `False`. The `filter()` function takes two arguments:
 
1. A function that returns `True` or `False` for each element.
2. An iterable (like a list, tuple, or set) that you want to filter.
 
Here’s the general syntax:
 
```python
filter(function, iterable)
```
 
### Example Usage
 
1. **Basic Example:**
 
   Suppose you have a list of numbers and you want to filter out only the even numbers:
 
   ```python
   def is_even(n):
       return n % 2 == 0
 
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = filter(is_even, numbers)
 
   # Convert filter object to list
   even_numbers_list = list(even_numbers)
   print(even_numbers_list)  # Output: [2, 4, 6]
   ```
 
2. **Using Lambda Functions:**
 
   You can use a lambda function to make the code more concise:
 
   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = filter(lambda x: x % 2 == 0, numbers)
 
   # Convert filter object to list
   even_numbers_list = list(even_numbers)
   print(even_numbers_list)  # Output: [2, 4, 6]
   ```
 
3. **Filtering Strings:**
 
   For a list of strings, you might filter out strings that have more than a certain number of characters:
 
   ```python
   words = ['apple', 'banana', 'cherry', 'date']
   long_words = filter(lambda word: len(word) > 5, words)
 
   # Convert filter object to list
   long_words_list = list(long_words)
   print(long_words_list)  # Output: ['banana', 'cherry']
   ```
 
### Key Points
 
- `filter()` returns an iterator, so you often need to convert it to a list or another collection type to view or use the filtered results.
- If you pass `None` as the function, `filter()` will remove elements that are considered `False` (e.g., `None`, `False`, `0`, empty strings, etc.).
 
   ```python
   items = [0, 1, 2, '', 'text', None, [], [1, 2]]
   filtered_items = filter(None, items)
   print(list(filtered_items))  # Output: [1, 2, 'text', [1, 2]]
   ```
 
This is a basic overview of how `filter()` works. It can be a powerful tool when combined with lambda functions or other custom functions to process and filter data efficiently.

7> Explain about the earlier project with test case automated.
8> Script for connect the Switch and do the basic configuration & grep the show o/p for some command.

1. IPv6 regex

2. a=[[]]*2  = [[],[]]
   a[0].append(10) ==> [[10], [10]]
   a.append(10)
   print a        == [[10], [10], 10]

	a=[[]]*2 creates two references to the same empty list.
	a[0].append(10) modifies this shared list, so both a[0] and a[1] reflect this change.

If you want to create two separate inner lists instead of having them reference the same list, you should use a list comprehension or similar method:
a = [[] for _ in range(2)] 
a[0].append(10)
==> [[10], []] ==> Here, a[0] and a[1] are distinct lists.

3. What is enumerate()

In Python, the `enumerate()` function is used to add a counter to an iterable, such as a list or a tuple. This can be useful when you need to keep track of the index of items while iterating over them. The `enumerate()` function returns an iterator that produces tuples containing the index and the corresponding value from the iterable.
 
### Syntax
 
```python
enumerate(iterable, start=0)
```
 
- `iterable`: The iterable to be enumerated (e.g., a list, tuple, string).
- `start`: The starting index of the counter (optional, default is 0).
 
### Example Usage
 
1. **Basic Example:**
 
   Suppose you have a list of fruits and you want to iterate through the list while keeping track of the index:
 
   ```python
   fruits = ['apple', 'banana', 'cherry']
   for index, fruit in enumerate(fruits):
       print(f"Index {index}: {fruit}")
   
   # Output:
   # Index 0: apple
   # Index 1: banana
   # Index 2: cherry
   ```
 
2. **Starting Index:**
 
   You can specify a different starting index:
 
   ```python
   fruits = ['apple', 'banana', 'cherry']
   for index, fruit in enumerate(fruits, start=1):
       print(f"Index {index}: {fruit}")
   
   # Output:
   # Index 1: apple
   # Index 2: banana
   # Index 3: cherry
   ```
 
3. **Enumerating a String:**
 
   You can also use `enumerate()` with a string:
 
   ```python
   text = "hello"
   for index, char in enumerate(text):
       print(f"Index {index}: {char}")
   
   # Output:
   # Index 0: h
   # Index 1: e
   # Index 2: l
   # Index 3: l
   # Index 4: o
   ```
 
4. **Creating a List of Tuples:**
 
   You can convert the result of `enumerate()` to a list of tuples if needed:
 
   ```python
   fruits = ['apple', 'banana', 'cherry']
   enumerated_fruits = list(enumerate(fruits))
   print(enumerated_fruits)
   
   # Output:
   # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
   ```
 
### Key Points
 
- `enumerate()` is particularly useful when you need both the item and its index in loops, avoiding the need to manually manage the index.
- It is often used in conjunction with loops and other data processing tasks for cleaner and more readable code.
 
Overall, `enumerate()` provides a convenient way to handle indexing within loops and can make code more readable and expressive.

4. Name some modules you worked on. ==> os, re
5. Exception handling
6. Define a class in that def a function and explain concept of local and global variables.
7. Difference between list and dictionary.
8. Different ways to add values to a list and a dictionary.
9. Difference between python 2 and python 3.
10. print 10//4 and 10.0//4.0.  ==> 2 and 2.0

11. a=[1,2,3,4]
    print a[10]        = list index out of range
    print a[10:]       = []


2) Scenario based question in Python :
 
Write a Program in python using framework ?
 
Scenario:
 
Client (PC) --------- Server (Router)
 
We want to connect pc to router and to assign ip address to router port and give some configuration on router interface like
                    
      interface MgmtEth0/RP0/CPU0/0
                      ipv4 address %s %s
                      no shut
                      router static
                      address-family ipv4 unicast
                      223.255.0.0/16 %s
                      223.255.254.254/32 MgmtEth0/RP0/CPU0/0
                      
and check show interface brief command.
 
3) how to match IP address in python using regex ?
5) Did you work on YTool and When ?
6) How you did testing on it ?
7) How many scripts did you write in Netconf/yang (feature wise)?
8) On which platform did you write the Netconf scritps ?

1) Do you know regular expression, what syntax we use to match something?

2) What will be output from below re?

l= ‘abc12345abc’
re.match(“a.*c”,l)  ==> <_sre.SRE_Match object; span=(0, 11), match='abc12345abc'>

re.match(“a.?*c”,l)  ==> sre_constants.error: multiple repeat at position 3

re.match("a.?c",l)  ==> <_sre.SRE_Match object; span=(0, 3), match='abc'>

3) a = [abc,cde,efg,abc,cde,efg,klk,dka,dka,dka]

how to remove duplicate index in above list.

4) 1  2  3  4  5  6  7  8
     3     7     11    15
        10          26
              36

Write a program in python to get 36 results.
x = [1,2,3,4,5,6,7,8]

def sum_of_el(x):
    l = []
    for i in range(len(x)):
        if i%2 != 0:
            continue
        l.append(sum(x[i:i+2]))
    return(l)

def big_lst(x):
    big_list = [x]
    while len(x) > 1:
        x = sum_of_el(x)
        big_list.append(x)
    return big_list

print(big_lst(x))
for i in big_lst(x):
    for j in i:
        print(' '*j, j,'   ',end='')
    print("\n")


5) How to connect a router interface through python programming ?
Import paramiko
Ssh = paramiko.SSHClient()
Ssh.connect(‘hostname’, username = “username”, password = “password”)
Ssh.exec_command(“show interface brief”)


6) INDIA IS A BIG COUNTRY PAKISTAN IS A BIG COUNTRY ?

   hOW TO swap India to pakistan and Pakistan to India in abvoe line ?
x1 = 'INDIA IS A BIG COUNTRY PAKISTAN IS A BIG COUNTRY'
x = x1.split()

x.remove('INDIA')
x.remove('PAKISTAN')
x.insert(0, 'PAKISTAN')
x.insert(5, 'INDIA')
print(" ".join(x))

7) Just tell me how to write in python programming

   1234567 to 1,234,567.
>>> formatted_number = f"{number:,}"  ### The {number:,} syntax in f-strings is a concise way to format numbers with commas as thousands separators.
>>> print(formatted_number)
1,234,567
Or
formatted_number = "{:,}".format(number) print(formatted_number)

8) How to open a file in python ?

9) WAP to open a file and write something in that file ?

10) How to print even and odd index ?

11) What module to import to connecting router interface in python ?

========================================================================

1.	Regular expression Syntax
2.	Difference between re.match and re.search
3.	What is re.sub?
4.	How do you find match IP Address (192.168.1.100) in any given string?
5.	Why do we need classes in Python?
6.	What is use of using try and except in Python?
to handle any unexpected error in your Python programs and to add debugging capabilities in them. Exceptions can be caught in the program using try and except statements.
Exception – unexpected event that happened during the execution of script, which interrupts the normal script flow. Try: except – try –code to be executing. Except – exception name , if that particular exception is hit, it will execute the code under that. Else- if no exceptions are hit. Finally – in any case this will be executed. Except <exceptionname> , arg: - arg – gives more details about the exception. U can print the argument.
7.	What are different types of data types in Python?
8.	Difference between list and tuple?
9.	Difference between for loop and while loop?
What is For Loop?
For loop is used to iterate over elements of a sequence. It is often used when you have a piece of code which you want to repeat "n" number of time.

What is While Loop?
While Loop is used to repeat a block of code. Instead of running the code block once, It executes the code block multiple times until a certain condition is met.
10.How to find duplicate elements in array using for loop in Python?
    1. loop through each element
    2. compare that element to all other elements using another loop. 
	 3. If both elements are same, then print it. 
	 4. for getting the count, use lst.count() and assign it to an array
OR – with one four loop
.	make a copy of the list
.	iterate through each element in list1
.	remove that element from list2
.	if the removed element is still present in list2,
duplicate. Get the count from list1
list1 = [1,2,3,4,5,4,6,5]

print("repeating elements")
for i in range(0, len(list1)):
for j in range(i+1, len(list1)):
       if list1[i] == list1[j]:
        print(list1[i])
			           arr[list1[i]] = list1.count(list1[i])

OR
list1 = [1,2,3,4,5,4,6,5,2,4]

arr ={}
list2 = list1[:]
print("repeating elements")
count = 0
for i in range(0, len(list1)):
    list2.remove(list1[i])
    if list1[i] in list2:
		    arr[list1[i]] = list1.count(list1[i])
			#print(list1[i])
print(arr)

What would I use a dictionary for?
----------------------------------
When you have to take one value and "look up" another value. In fact you could call dictionaries "look up tables."

What would I use a list for?
----------------------------
Use a list for any sequence of things that need to be in order, and you only need to look them up by a numeric index.


http://career.guru99.com/top-25-python-interview-questions/

>>> # Fibonacci series:0 1 1 2 3 5 8
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while b < 10:
...     print(a)
...     a, b = b, a+b
...
‘OR’
>>> a,b = 0,1
>>> while b<10:
	print(a)
	c=a
	a=b
	b=c+b

# Python 3: Fibonacci series up to n
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a < n:
>>>         print(a, end='   ')   == > print(a,end=’---‘) –here separation will be ---  (as a list =>result.append(a)
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

# Python 3: Simple arithmetic
>>> 1 / 2
0.5
>>> 2 ** 3
8
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division
5

# Python 3: List comprehensions
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
['BANANA', 'APPLE', 'LIME']

# List and the enumerate function
>>> list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

# For loop on a list
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
... 
>>> print('The product is:', product)
The product is: 384

# Write the code that calculate the sum of even numbers from x1 till x2

def test(x, y):
    j = 0
    for i in range(x, y, 2):
		j = i + j
    return j

print (test(10,20)) 

#Which types of data are immutable in Python? (Numbers, Tuples, Strings, Booleans)
#Which types of data are mutable in Python? (List)
#Question: What is the Lambda Functions in Python? 
Answer: Lambda Functions in Python can be used to pass a function as an argument or can be used inside another statement. A lambda function has the syntax: lambda variable(s) : expression
#Question: What are Decorators in Python? 
Answer:A decorator in Python is a function that wraps another function (it takes a function as an argument and returns a replacement function) Or another way to explain: The main function is called and its return value passed to the decorator and the decorator then returns a function that replaces the wrapped function. they are functions which modify the functionality of another function.
Two types – function decorators and class decorators
#The following is displayed by a print function call: 
yesterday 
today 
tomorrow 
#Please write an example of a print function. 
Answer: print('yesterday\ntoday\ntomorrow')
The following is displayed by a print function call: 
hello-how-are-you 

#Please write an example of a print function. 
Answer: print('hello' + '-' + 'how' + '-' + 'are' + '-' + 'you')
Question: What does the expression len('') evaluate to? 
Answer: 0

#Question: What are "tuples" 
Answer: Tuples are immutable sequences: they cannot be modified. Tuples use parentheses instead of square brackets: tup = ('test', 5, -0.2)
#Question: What are the rules for legal Python names? 
Answer: 
1. Names must start with a letter or _. 
2. Names must contain only letters, digits, and _.
#Question: What is the dictionary type in Python? 
How to Access Information From Dictionaries and Modify it?
#Question: What are classmethod and staticmethod ?
They are decorators. 
A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.
A static method is also a method which is bound to the class and not the object of the class.
A static method can’t access or modify class state.
It is present in a class because it makes sense for the method to be present in class.
# Eg for break
magicNumber = 26
for x in range(101):
    if x is magicNumber:
        print (x, "is magic number")
        break
    else:
        print (x)

# eg for continue
numberList = [10, 20, 30]

for i  in range(31):
    if i in numberList:
        continue
    print (i)
List Comprehensions:

It can be used to construct lists in a very natural, easy way.
In maths,
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}

Using python,
>>> S = [x**2 for x in range(10)]
>>> V = [2**i for i in range(13)]
>>> M = [x for x in S if x % 2 == 0]
>>> 
>>> print S; print V; print M
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
[0, 4, 16, 36, 64]

compute prime numbers using list comprehensions:
>>> noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]	
>>> primes = [x for x in range(2, 50) if x not in noprimes]
>>> print(primes)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

With strings
>>> words = 'The quick brown fox jumps over the lazy dog'.split()
>>> print(words)
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
>>> 
>>> stuff = [[w.upper(), w.lower(), len(w)] for w in words]
>>> for i in stuff:
...     print(i)
... 
['THE', 'the', 3]
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['FOX', 'fox', 3]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['THE', 'the', 3]
['LAZY', 'lazy', 4]
['DOG', 'dog', 3]
>>> 
>>> stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
>>> for i in stuff:
...     print i
... 
['THE', 'the', 3]
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['FOX', 'fox', 3]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['THE', 'the', 3]
['LAZY', 'lazy', 4]
['DOG', 'dog', 3]

This can be achieved using map() and lambda function	

IMPORTANT MODULES:
--------------------------------

Module sys :
----------------
>>sys.path
>>sys.path.append(“python script path”)


This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
    
    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.
    
    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.
    
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.

For order of precedence, just remember this PEDMAS (similar to BODMAS)

Here are most of the built-in objects considered false:
constants defined to be false: None and False.
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)

Boolean Operations — and, or, not
These are the Boolean operations, ordered by ascending priority:

Operation	Result	Notes
x or y	if x is false, then y, else x	(1)
x and y	if x is false, then x, else y	(2)
not x	if x is false, then True, else False	(3)


+=   === > re – assign

>>> my_list[0:5:2]  == >last one – step index

Sequence Types — list, tuple, range

This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.
The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (repetition) op-erations have the same priority as the corresponding numeric opera-tions. [3]
Operation	Result	Notes
x in s	True if an item of s is equal to x, else False	(1)
x not in s	False if an item of s is equal to x, else True	(1)
s + t	the concatenation of s and t	(6)(7)
s * n or n * s	equivalent to adding s to itself n times	(2)(7)
s[i]	ith item of s, origin 0	(3)
s[i:j]	slice of s from i to j	(3)(4)
s[i:j:k]	slice of s from i to j with step k	(3)(5)
len(s)	length of s	 
min(s)	smallest item of s	 
max(s)	largest item of s	 
s.index(x[, i[, j]])	index of the first occurrence of x in s (at or after index i and before index j)	(8)
s.count(x)	total number of occurrences of x in s	



>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]

You can create a list of different lists this way:
>>>
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]


Create multi-dimensional list -
https://docs.python.org/3/faq/programming.html#faq-multidimensional-list

-Tuple faster than list. Why ?

Tuples are identified by python compiler as one immutable con-stant literal, and hence is built as 1 single entity and stored in hashtable and are fetched when some execution is done on them.
Whereas list are mutable object, so each time some execution is done new objects are created hence arent interpreted just once and hence lists are slower than tuple.


1) Which of the following would NOT change the length of the `foods` list? Assume the `foods` list currently contains 1 item.

Incorrect

Correct answer
foods + ['orange']

Explanation
For lists, the `+` operation will return a new list without modifying the two lists that you are adding together. The `+=` operation will reassign the variable on the left-hand side with the combined value of the two lists. The list type's `append` method will mutate the list by placing the new item at the end of the list. The list type's `pop` method will remove the item at a specified index and return that value, changing the list in the process.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/4/module/168

2) What is the file extension for a Python file?

Correct

Correct answer
.py

Explanation
The standard Python file extension is `.py`.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1682/lesson/2/module/168

3) Which of these `for` loop declarations is NOT valid?

Correct

Correct answer
for x, y in [1, 2, 3]:

Explanation
The loop `for x, y in [1, 2, 3]` is not a valid `for` loop because each item is an integer and you can't unpack an integer into two separate parts to populate the `x` and `y` values. This will raise "TypeError: 'int' object is not iterable".

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/2/module/168

4) Which of these types CANNOT be iterated over?

Correct

Correct answer
float

Explanation
The `float` type is the only one in this list that cannot be iterated over. Strings might seem like they shouldn't be iterable, but you can also think of them as lists of characters.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/2/module/168

5) What does REPL stand for?

Correct

Correct answer
Read Evaluate Print Loop

Explanation
REPL stands for Read Evaluate Print Loop, and it describes how the code that is typed in is executed.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1682/lesson/1/module/168

6) Which of these is a valid list comprehension? `my_list` is equal to `[1, 2, 3]`

Incorrect

Correct answer
[item for item in my_list]

Explanation
The expression `[item for item in my_list]` is the only valid list comprehension. `[for item in my_list]` is close, but invalid. You need to provide a value to the left-hand side of the `for` in a list comprehension. The expression `{item | item in my_list}` is not valid Python.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/4/module/168

7) What value represents nothingness in Python?

Correct

Correct answer
None

Explanation
`None` is the constant that represents nothingness in Python. All of the other options are used by various other languages to represent the same concept.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/2/module/168

8) What would the result of 4 * '1.1' be? (Hint: that is a string, not a float.)

Incorrect

Correct answer
'1.11.11.11.1'

Explanation
When a string is multiplied by an int, it repeats and concatenates the initial value. Knowing this, 4 * '1.1 would basically be '1.1' + '1.1' + '1.1' + '1.1' which would equal '1.11.11.11.1'

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/1/module/168

9) What keyword is used for a secondary condition in an if/else group?

Correct

Correct answer
elif

Explanation
Python uses the unorthodox keyword of `elif` for secondary conditional values that are part of the same if/else group.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/1/module/168

10) How would you create a new variable with the value "test"?

Correct

Correct answer
foo = "test"

Explanation
Assigning a variable in Python is done using the `=` operator and you don't need to specify the data type. The `==` operator checks for equality and will return a boolean. The other two answers show ways of setting variables in other languages.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/3/module/168

11) How would you get every item with an even index (0, 2, 4, etc.) from a list using slicing?

Correct

Correct answer
my_list[::2]

Explanation
The optional, third value of a slice is the "step" value. `my_list[::2]` will gather the items from the beginning of the list to the end of the list skipping every second item. `my_list[:2]` will return the first two items of the list. `my_list[2:]` will return every item after the first two items in the list.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/4/module/168

12) What type of loop would you use to create an infinite loop in Python?

Correct

Correct answer
A "while" loop.

Explanation
Using a `while` loop with a condition that will always return `True` will create an infinite loop. There is no `do...while` loop in Python. The `for` loop iterates over some collection and the collection with have an end.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/2/module/168

13) Which of these would return a float as the result?

Correct

Correct answer
2 / 3

Explanation
In Python 3, integer division (`2 / 3`) will return a float. This operation returns an integer in Python 2. Integer multiplication (`2 * 1`) will return an integer. `3 * str(2.0)` will return a string because the `str(2.0)` is the first thing to be executed. Floor division (`2 // 3`) will return the integer portion of the division without the decimal (`0` in this case).

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/1/module/168

14) How can you run a non-executable Python file?

Correct

Correct answer
python file.py

Explanation
The `python` executable will start the REPL if there are no arguments, but if you pass in a file, then it will be interpreted and executed. There is no need for a subcommand like `exec` or `run` (which don't exist) to run a Python file.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1682/lesson/2/module/168

15) How do you exit the Python REPL?

Correct

Correct answer
enter "exit()"

Explanation
You exit the REPL by either running the `exit` function, by using parenthesis, or by using Ctrl-D. `Ctrl-c` does not exit the REPL. `:q` is used to exit Vim, not Python.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1682/lesson/1/module/168

16) How would you get a lowercase version of a string?

Correct

Correct answer
"SOMETHING".lower()

Explanation
The `lower` method on the str type will allow you to get a lowercase version of the string that you're working on. You call the method using parenthesis. Otherwise, you will return the method itself instead of the lowercase string. `toLower` is not a method on the str type. There is also not a top-level `lower` function that receives a string as an argument.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/1/module/168

17) How would you get the value of the key 'color' from a dictionary called `favorites`? Note: 'color' is a string.

Correct

Correct answer
favorites['color']

Explanation
To read a value from a dictionary, you will use the subscript operator (`[]`) with the exact key, 'color' in this case.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1683/lesson/5/module/168

18) Which of these operations will return True?

Correct

Correct answer
1 in ['a', 1, 'b']

Explanation
Since the value `1` is in the list `['a', 1, 'b']` the expression `1 in ['a', 1, 'b']` will return True. The expression `not 'Bob'` will return False because 'bob' is True and `not True` is False. The expression `2 not in [1, 2, 3]` will return False because `2` is in `[1, 2, 3]`.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/1684/lesson/3/module/168

19) Which of these CANNOT be used as a key in a dictionary?

Correct

Correct answer
[1, 2, 3]

Explanation
Any immutable type can be used as a key in a dictionary. Lists are mutable because you can add or remove items from them. Therefore you cannot use a list as a dictionary key.

Further Reading
https://linuxacademy.com/cp/
courses/lesson/course/1683/lesson/5/module/168


>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]


Copy an Object in Python
In Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new variable that shares the reference of the original object.
Let's take an example where we create a list named old_list and pass an object reference to new_list using = operator.

import copy
copy.copy(x)
copy.deepcopy(x)
A shallow copy creates a new object which stores the reference of the original elements.
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
Let’s continue with example 2. However, we are going to create deep copy using deepcopy()function present in copy module. The deep copy creates independent copy of original object and all its nested objects.
The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
	A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
	A deep copy constructs a new compound object and then, recursively, in-serts copies into it of the objects found in the original.

Doc on formatting:
https://pyformat.info/
udemy notebooks
https://github.com/Pierian-Data/complete-Python-3-Bootcamp
Basic Practice:
http://codingbat.com/python
More Mathematical (and Harder) Practice:
https://projecteuler.net/archives
List of Practice Problems:
http://www.codeabbey.com/index/task_list
A SubReddit Devoted to Daily Practice Problems:
https://www.reddit.com/r/dailyprogrammer
A very tricky website with very few hints and touch problems (Not for beginners but still interesting)
http://www.pythonchallenge.com/

Patterns:
https://codescracker.com/python/program/python-program-print-star-pyramid-patterns.htm 


Questions:

1)	Implement a group_by_owners function that:
•	Accepts a dictionary containing the file owner name for each file name.
•	Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Out-put.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
Iterate thru key and value, then create a new dict with owner as key. Using, dict.get(), define an empty list as value, then add file name to that ist.
def group_by_owners(files):
    result = {}
    for file, owner in files.items():  # use files.iteritems() on Python 2.x
        result[owner] = result.get(owner, []) + [file]  # you can use setdefault(), too
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
# {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}

2)	Write a function that checks if a given word is a palindrome. Character case should be ignored.
-make the word to lower, reverse the word using slice operator, compare words
OR iterate thru the characters using for loop, then compare first and last chars, set res for each iteration. Based on result, determine.
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        w_list =  list(word.lower())
        l = len(w_list)
        new_w = []
        for i in range(1,l+1):
            new_w.append(w_list[-i])
        if str(w_list) == str(new_w):
            return True

print(Palindrome.is_palindrome('Deleveled'))
Or
str1 = "adgghhjkk"

for i in range(len(str1)):
    res = 0
    if (str1[i]) != str1[-(i+1)]:
        print("not palindrome")
        break
else:   
    print("palindrome")
=========================================
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        w_list =  word.lower()
        if w_list == w_list[::-1]:
            return True

print(Palindrome.is_palindrome('Deleveled'))


3)	Compare values of each key in d1 and d2 and print extra value in each key
-	Iterate thru the dict
-	Compare values for same key in both dict, if it is same, update a new dict
-	If list1 < list2, 

d1 = {'a':[1,2,3], 'b':[4,5], 'c':[6], 'd': [7]}
d2 = {'a':[1,2], 'b':[5,6,4], 'c':[6]}
d3 = {}
for i,j in d1.items():
    if d1.get(i) == d2.get(i):
        d3[i] = "same"
    elif d1.get(i) < d2.get(i):
        new_list = []
        for x in d2.get(i):
            if x not in d1.get(i):
                new_list.append(x)
        d3[i] = new_list
    else:
        new_list = []
        for x in d1.get(i):
            if x not in d2.get(i, []):
                new_list.append(x)
        d3[i] = new_list
print(d3)

4) Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

def front_back(str):
  if len(str) >= 2:
    f = str[0]
    l = str[-1]
    mid = str[1:len(str)- 1]
    new_str = l + mid + f
    return new_str
  else:
    return str


5) Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
-	Define an empty string
-	Iterate based on length of the string
-	Concatenate already defined string with slice of string
def string_splosion(str):
  r = ""
  for i in range(len(str)):
    r = r + str[:i+1]
  return r


6) Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
-	Get the string which is to be matched
-	Iterate thru length of the string till len -2
-	Slice string from i to i + 2
-	If that matches initial substring, increment counter
def last2(str):
  s = str[-2:]
  c = 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if s == sub:
      c = c+ 1
  return c
  
7) Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  seq = [1,2,3]
  for i in range(len(nums)):
    new_seq = nums[i:i+3]
    if new_seq == seq:
      return True
  return False

8) Given 2 strings, a and b, return the number of the posi-tions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

def string_match(a, b):
  c = 0
  shorter = min(len(a), len(b))
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      c += 1
  return c

9) Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  res = []
  i = 1
  while i <= len(nums):
    res.append(nums[-i])
    i += 1
  return res
    

10)
str = "print only the words which start with s in this sentence"

for word in str.split():
    if word[0].lower() == 's':
        print(word)

11) divisible by 3
l1 = [x for x in range(1,51) if x%3==0]
print(l1)
12)
str = "print every word in this sentence that has an even number of letters"
	
for word in str.split():
    if len(word)% 2 == 0:
        print word

13)
l1 =[]

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        l1.append("FizzBuzz")
    elif num % 3 == 0:
        l1.append("Fizz")
    elif num % 5 == 0:
        l1.append("Buzz")
    else:
        l1.append(num)
print(l1)

14)
str = "Create a list of the first letters of every word in this string"
l1 = [x[0] for x in str.split()]
print(l1)

15)
def new_fn(word):
    if word[0] not in 'aeiou':
        new_wrd = word[1:]+word[0]+'ay'
    else:
        new_wrd = word+'ay'
    return new_wrd
    
print(new_fn('apple'))

16) String with even letters upper case
def myfunc(str):
    l1 = list(str)
    for i in range(len(l1)):
        if i%2 == 0:
            l1[i]=l1[i].lower()
        else:
            l1[i]=l1[i].upper()
    new_str = "".join(l1)
    return new_str
    
        
print(myfunc("abcdefg"))

17) function that counts the number of times a given pattern appears in a string including overlap.
## str.count(ptn) does not include overlap.

def myfunc(str,ptn):
    i=len(ptn)
    c = 0
    for j in range(len(str)):
        sub_str=str[j:j+i]
        
        if sub_str == ptn :
            c += 1
    return c, str.count(ptn)
    
print(myfunc('ahahahahaa', 'hah'))

18) reverse words in a string

def myfunc(str):
    new_l = []
    op = str.split()
    new_l = op[::-1]
    #for i in range(1, len(op)+1):
    #    new_l.append(op[-i])
    new_str = " ".join(new_l)
    return new_str
    
print(myfunc('I am learning Python'))
        
19) return a string where for every character in the original there are 3 characters 

def myfunc(str):
    
    new_str = ""
    for i in str:
        new_str = new_str + i*3
    return new_str
    
print(myfunc('hello'))

20)write a fun that takes in a list of integers and returns True if it contains 007 in order.
[1,2,4,0,0,7,4] – True
[1,2,0,4,0,3,4,7,3] - True

def myfunc(my_list):

    c = 0
    res = False
    for i in range(len(my_list)):
        if my_list[i] == 0:
            c += 1
            continue
        if c == 2 and my_list[i] == 7:
            res = True
    return res    
        

    
print(myfunc([1,0,2,4,0,3,5,1]))

OR

def myfunc(l1):
    code = [0,0,7,'x']
    for num in l1:
        if num == code[0]:
            code.pop(0)
            
    return len(code) == 1
    
print(myfunc([1,2,4,0,0,7,4]))
print(myfunc([1,2,0,4,0,2,7,4]))

21) Swap variable without using 3rd variable

def fn(x,y):
    x = x+y
    y = x-y
    x = x-y
    return x,y
print(fn(2,3))

22) Return nth element in fibanacci series. 

def fn(n):
    #0,1,1,2,3,5,8,13, 21
    a,b = 0,1
    while a < n - 2: wrong!!
        c = a+b              ## OR a,b = b, a +b
        a = b 
        b = c 
    return b

print(fn(8))

first = 0
second = 1
 
print("\nfibonacci series is:")
print(first, second )
 
for i in range(2, n):
	next = first + second
	print(next)
 
	first = second
	second = next
In a, b = b, a + b, the expressions on the right hand side are evalu-ated before being assigned to the left hand side. So it is equivalent to:
c = a + b
a = b
b = c

23) Sort a list in ascending order without using list functions
1. Take a random value from the list as min
2. compare all elements in the list with that and get the min value
3. append new list with that min value
4. Remove that value from list
5. do the same thing on smaller list

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list

Bubble sort:
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp 
print('Second largest number is:',a[n-2])

24) # Python program to print Pyramid pattern 

1. two for loops
2. first one for rows
3. in each row, print requiredss number of stars
  
def pattern(n): 
     
    # For printing the upper part of pyramid 
    for i in range (1, n+1): 
        for j in range (1, i+1): 
            print("* ",end="") 
        print()
      
    # for printing the middle and lower part of pyramid 
    for i in range (n, 1, -1): 
        for j in range (i, 1, -1): 
            print("* ",end="") 
        print()
  
# Driver program 
pattern(6) 

Input:  n = 6
Output:
       *
       * *
       * * *
       * * * *
       * * * * *
       * * * * * * 
       * * * * *
       * * * *
       * * *
       * * 
       *
OR
def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
        print("* " * i) 
    for j in range(n-1, 0, -1):
        print("* " * j)
# Driver Code 
n = 5
pypart(n)

def pypart(n): 
    for i in range(1, n+1): 
        print(" " * (n-i) + "*" * i + "*" * (i-1)) 

# Driver Code 
n = 6
pypart(n)

     *
    ***
   *****
  *******
 *********
***********

24)
Function to demonstrate printing pattern of alphabets

def pattern(n): 
     
    num = 65  == >      # ASCII value
   			 # For printing the upper part of pyramid 
    for i in range (1, n+1): 
        for j in range (1, i+1): 
            print chr(num),   # explicitly converting to char
            num = num + 1
        print

  
# Driver Code 
n = 5
pattern(n)
	
https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
https://codescracker.com/python/program/python-program-print-star-pyramid-patterns.htm


1)	Difference b/n lists and tuples
Lists –mutable –can be modified
Tuple – immutable – cannot be modified
Lists are used when the we are not sure about how much data we will be handling.
Tuples are used if we are sure about the data we are handling and if we are doing memory intensive operations. When u have fixed amount data or when u know how much data is coming in , use tuple.

Eg – we have database, where we have number, name, age as fixed columns and we don’t know how many rows of data will be there.
In that case we can use columns as tuples and rows in list.
Db = [(1, “abc”, 10), (2, “dfd”, 20), (3, “fdsd”, 30)]
A = [1,2,(4,5)] --- here (4,5) is not mutable
B= ([1,2,3],)  --- this list is still mutable as B[0].append(4)


2)	How multithreading is achieved in Python?
import threading
-python has a construct called Global interpreter Lock(GIL).
GIL makes sure that only one of ur threads can execute at any time.  A thread acquires the GIL, does a little work, then pass the GIL onto the next thread. This happens very quickly and it seems that threads are executing in parallel, but they are just taking turns using the same CPU core. All this GIL passing adds overhead to execution.

Multi-processing – if u have 4 cores, using four cores, u can run processes parallel. Module – multiprocessing.

Eg for threading ? 

3)	Big = x if x > y else y  -- ternary operator => used to show conditional statements. True or false statements. 
4)	What is monkey patching ?
	Means applying a patch to a class or module at run time. Or dynamic modifications at run time. To apply quick fixes during run time.
Eg :
We have a class wriiten in module m:
#m.py
Class Myclass():
         Def f(self):
                 Print(“f()”)
               --------
Write a function outside module
Def monkey_f():
	Print(“monkey_f()”)

>>>m.Myclass.f = monkey_f
>>>obj = m.Myclass()
>>>obj.f()
monkey_f()

5)	When to use dict and list ?
Key , value pair – 
Eg : store names with mail id and emp_id
Emp = { ‘name1’:[‘name1@gmail.com’ ,111] , ‘name2’:[‘name2@gmail.com’ , 112]}
6)	How to randomize items in a list ?
From random import shuffle
X = [1,2,3,]
Shuffle(x)
7)	Write a sorting alg for a numerical dataset.
L = [‘1’, ‘2’, ‘3’, ‘10’]
L.sort() == > applies on asci values
=> [‘1’, ’10, ‘2’…
L =[int(i) for i in L]
L.sort()
	
8)	T1 =(‘a’, ‘b’ , ‘c’)
T2 =(1,2,3)
A0 = dict(zip(t1,t2)
	 {‘a’:1,”b’: 2 ,’c’:3}
A1=range(10) => [0,1,2…9]
A2 = sorted([i for i in A1 if I in A0])  checks for keys to be 1,2 ,3..9 in A0
A3 = sorted([A0[s] for s in A0])  => will sort dict based on values
	[1,2,3]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}  => dict comprehension
A6 = [[i,i*i] for I in A1] => list of lists
9)	Explain split(), sub(), subn() methods in ‘re’
Split() – uses  a regex pattern to split a given string into a list
Sub() – finds all substrings where the regex pattern matches and then replaces them with a different string
Subn() – it is similar to sub() and also returns the new string along with the no.of replacements.

10)	I find the duplicates in a list and create a dict with count?
l = [1,2,3,4,1,2,3,1,2]
a = {x:l.count(x) for x in l if l.count(x) > 1}
	{1: 3, 2: 3, 3: 2}

11)	 Program to find the sum of digits in a number without using recursion. The program output is also shown below.
12)	l=[]
13)	b=int(input("Enter a number: "))
14)	while(b>0):
15)	    dig=b%10
16)	    l.append(dig)
17)	    b=b//10
18)	print("Sum is:")
19)	print(sum(l))
         12)  Program to accept three distinct digits and prints all possible combinations from the digits.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

13 Program to Find the Sum of Digits in a Number
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)

14) Program to find the smallest divisor of an integer. The program output is also shown below.
n=int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])

15) Prime numbers
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


16) Program to sort the list according to the second element in the sublist. 
a=[['A',34],['B',21,1],['C',26],['D',56,6]]
for i in range(0,len(a)):
    for j in range(0,len(a[i])-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
 
print(a)

17) Program to sort a list according to the length of the elements. The program output is also shown below.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    a.append(b)
a.sort(key=len)
print(a)




Requests:
Make a request –
import  requests
r = requests.get(‘https://google.com/events”)
response oblect called ‘r’
r = requests.post(‘https://google.com/post’, data = { ‘key’:’value})
r = requests.put(‘https://google.com/put’, data = { ‘key’:’value})
r = requests.delete(‘https://google.com/delete’)
r = requests.head(‘https://google.com/get’)
r = requests.options(‘https://google.com/get’)

passing parameters in URLs:
payload = {‘key1’ : ‘value1’, ‘key2’: ‘value2’}
r = requests.get(“https://google.com/get’, params = payload)
print(r.url)
>> https://google.com/get?key2=value2&key1=value1

dictionary key whose value is None will not be added to the URL’s query string.

You can also pass a list of items as a value:

>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('https://httpbin.org/get', params=payload)
>>> print(r.url)
https://httpbin.org/get?key1=value1&key2=value2&key2=value3

Response content: 
r.text
>> u'[{"repository":{"open_issues":0,"url":"https://github.com/
When you make a request, Requests makes educated guesses about the encoding of the response based on the HTTP headers.
>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'

You can also access the response body as bytes, for non-text requests:

>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...

There’s also a builtin JSON decoder, in case you’re dealing with JSON data:
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

To check that a request is successful, use r.raise_for_status() or check r.status_code is what you expect.

Custom Headers:
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)

Requests.post:
The data argument can also have multiple values for each key. This can be done by making data either a list of tuples or a dictionary with lists as values.
>>> payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
>>> r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
>>> payload_dict = {'key1': ['value1', 'value2']}
>>> r2 = requests.post('https://httpbin.org/post', data=payload_dict)
>>> print(r1.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
>>> r1.text == r2.text	




True
There are times that you may want to send data that is not form-encoded. If you pass in a string instead of a dict, that data will be posted directly.
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))

Instead of encoding the dict yourself, you can also pass it directly using the json parameter (added in version 2.4.2) and it will be encoded automatically:

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)

Note, the json parameter is ignored if either data or files is passed.

POST a Multipart-Encoded File:
>>> url = 'https://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}


Response Status Codes:

HTTP status codes are standard response codes given by web site servers on the internet. The codes help identify the cause of the problem when a web page or other resource does not load properly.

4xx Client Error - 404 (Not Found), 403 (Forbidden), and 400 (Bad Request).

5xx Server Error - 500 (Internal Server Error), along with 503 (Service Unavailable) and 502 (Bad Gateway).
>>> r = requests.get('https://httpbin.org/get')
>>> r.status_code
200
If we made a bad request (a 4XX client error or 5XX server error response), we can raise it with Response.raise_for_status():

>>> bad_r = requests.get('https://httpbin.org/status/404')
>>> bad_r.status_code
404

>>> bad_r.raise_for_status()
Traceback (most recent call last):
  File "requests/models.py", line 832, in raise_for_status
    raise http_error
requests.exceptions.HTTPError: 404 Client Error
But, since our status_code for r was 200, when we call raise_for_status() we get:

>>> r.raise_for_status()
None

We can view the server’s response headers using a Python dictionary:
>>> r.headers
If a response contains some Cookies, you can quickly access them:
>>> r.cookies['example_cookie_name']
'example_cookie_value'
To send your own cookies to the server, you can use the cookies parameter:
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)

We can use the history property of the Response object to track redirection.

The Response.history list contains the Response objects that were created in order to complete the request. The list is sorted from the oldest to the most recent response.

If you’re using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable redirection handling with the allow_redirects parameter:

>>> r = requests.get('http://github.com/', allow_redirects=False)

>>> r.status_code
301

>>> r.history
[]
If you’re using HEAD, you can enable redirection as well:

>>> r = requests.head('http://github.com/', allow_redirects=True)

>>> r.url
'https://github.com/'

>>> r.history
[<Response [301]>]
You can tell Requests to stop waiting for a response after a given number of seconds with the timeout parameter. Nearly all production code should use this parameter in nearly all requests. Failure to do so can cause your program to hang indefinitely:

>>> requests.get('https://github.com/', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timeout

In the event of a network problem (e.g. DNS failure, refused connection, etc), Requests will raise a ConnectionError exception.

Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.

If a request times out, a Timeout exception is raised.

If a request exceeds the configured number of maximum redirections, a TooManyRedirects exception is raised.

All exceptions that Requests explicitly raises inherit from requests.exceptions.RequestException.



JSON:

import json
blackjack_hand = {8: "Q"}
encoded_hand = json.dumps(blackjack_hand)   --- serialization(encoding)
decoded_hand = json.loads(encoded_hand)   ---- deserialization(decoding)
print(type(encoded_hand))   string
print(type(decoded_hand))  dict

json.dump(data, Fileid)  == > to dump to a file..sames as dump-s

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

Real time use : - using the json library to deserialize the text attribute of the response object of requests.
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


Selenium:

#pip install –U selenium

from selenium import webdriver

driver = webdriver.Chrome(“G:\\selenium\\Chrome\\chromedriver.exe”)  -- > need to specify path of chromedriver.exe.
diver.set_page_load_timeout(30) => if facebook is not responding in 30 s, it will say page load timeout.
driver.get(“http://www.facebook.com”)
driver.maximize_window()
driver.implicitly_wait(20)  wait for any webelement.
driver.find_element_by_id(“email”).send_keys(“Selenium webdriver”)
driver.find_element_by_name(“pass”).send_keys(“Python”)
driver.find_element_by_id(“loginbutton”).click()
driver.get_screenshot_as_file(“G:\\Users\\Python\\Screenshots\\Facebook.png”)  => capture the screenshot and keep it in the dir.
print(driver.title)
assert “Facebook” in driver.title
driver.quit()

For IE,
driver = webdriver.Ie(“G:\\selenium\\IE\\IEdriverServer.exe”)
driver = webdriver.Firefox()


write click, inspect == get webelements
SELENIUM –UDEMY

A suite of tools used to automate browser actions.
Sel IDE, Sel Remote control (RC) or sel 1, Sel Grid and Sel webdriver or sel 2.

Sel IDE – add on to firefox – plugin to record and playback tests.
Sel RC or Sel 1 – acts like http proxy server that interprets cmds sent to ur test scripts into cmds that browser can understand to perform certain actions.
Sel Grid – allows tests to run in parallel on diff machines with diff operating systems and diff browsers.
Sel Webdriver or Sel 2 – Client API used to automate browser actions without the need of additional interpreter like sel RC. To simulate webdriver actions.

Install Pip
#tar –vxzf setuptools.tar.gz
#cd setuptools
#sudo python setup.py install
#sudo easy-install pip

#sudo pip install –U selenium 

Overwrite PYTHONPATH
#open .profile
#echo $PYTHONPATH
#

Difference between asset and verify in sel IDE
Asset will stop execution when it hit a failure
Verify will mark the error and continue execution








DOM – document object model

1)	Exceptions in selenium webdriver
TimeoutException –
NoSuchElementException
ElementNotVisibleException
StaleElementEsception

2)	What is exception test in selenium ?

@Test(expectedException = noSuchElementException.class)
3)	Have u used excelsheet in ur project ?
Excel sheet is used as a Data Source and also contains Data set for data driven testing.
-Data Source 
	-Appln url for all env
	-user name and passwords for diff env
	-test cases to be executed
-data driven test
	-data for different iterations
           4)   how can u redirect browsing from a browser through some proxy ?
           5)    What is POM (Page Object Mobel)? Advtges ?
                  A design pattern to createObject repository for web UI elements. It separated web elements objects and methods.
                  Each web page in the appln should have corresponding page class
                  Page class will find the WebElements of that web page and also contains page methods which perform operations on those web elements.
           Advtgs:
	Keep operations and flows in the UI separate from verification
	Object repo independent of  test cases
	Reusability of code
6) What is a Page factory ?
    Page factory is an inbuilt Page Object model for selenium webdriver which is very optimizes.
    Separation of Page Object Repository and Test methods.
    Page Factory class provides @FindBy annotation to find web elements.
   @FindBy can accept tagName,partialLinktext, name,linkText, id, classname, & xpath as attributes.
7) What are difftypes of WAIT statements in sel web dr ?
      How do u achieve synchronization in WebDriver ?
Sel web driver has different ways to sync the speed of execution od test and  the response from the appln under test. 
            Implicit wait : instructs web driver to wait for sometime by polling the DOM.
Once u have declared implicit wait it will be available for the entire life of web driver instance. By def value will be 0. If u set a longer def, then it will poll the DOM in periodic basis depending on browser/driver implementation. 10- 30 s “NoSuchElementException” is thrown if the element is not found.
           Explicit Wait : Instructs the execution to wait for some time until some condition is achieved.
Conditions : elementToBeClickable, elementToBeSelected, presenceOfElementLocated. Def wt time - 0
10 -30 s
Webdriver waits for a certain condition to be true before proceeding with next commands. Has a timeout. If the condition is true before timeout then webdriver proceeds with the next commands. If the condition is not true in the allocated time, then a “TimeoutException” is thrown.
8) Write a code to wait for a particular element to be visible on a page.
    Write a code to wait for an alert to appear.
WebDriverWait – class
9)What is the use of java script executor ?
   javaScriptExecutor is an interface(class) which provides mechanism to execute javascript through selenium driver. It provides ‘executescript’ & ‘executeAsyncScript’ methods, to run javascript in the context of currently selected frame or window.
Js = (javascriptexxecutor) driver;
Js.executeScript(Script,argumnets);

20)	How to scroll down a page using JavaScript in selenium?
Js.executeScript(“window.scrollBy(0,500)
21)	‘’ ‘’ to a particular element ?
Js.executeScript(“arguments[0].scrollIntoView”, element)

13 ) how to handle keyboard and mouse action using Selenium ?
Handling special keyboard events are done using Advanced User Interactions API.
It contains Actions and the Action Classes that are needed for executing these events.
Commonly used keyboard and mouse events are provided by Action class.
Method:
clickAndHold – clicks without releasing at the current mouse locaton.
dragAndDrop – Performs click-and-hold at the location of the source elements and moves to target
location and then releases mouse.

14 ) How to send ALT/SHIFT/CONTROL key in sel web dr ?
Method : keyDown(modifier_key)
Modifier_key - > keys.ALT, keys.SHIFT, keys.CONTROL
-	Ppperforms a modifier key press, does not release the modifier key. Subsequent interactions may assume its kept pressed.
Method – keyUp(modifier_key)
-	Performs a key release.
15 ) how to take screenshots ?
16 ) how to set the size of browser window using selenium?
 -to maximize a window – window.maximize()
 -to resize the current window to the given dimension – window.getsize()
                                                                                                 Window.setSize(dimension)
 -to set window to a particular size – js.executeScript(“window.resizeTo(x,y)”)
17) how to handle a dropdown in selenium webdriver ? (14 in video)
       How to select a value from dropdown ?


23/04/24s
Print 6 decimal points -  print("{:.6f}".format(float(pos/n)))


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0 ; neg = 0; zer = 0
    n = len(arr)
    if n > 100 or n < 0:
        print("wrong input")
    for i in arr:
        if i < -100 or i > 100:
            print("wrong output")
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
        #print(i)
    #print(n)
    print("{:.6f}".format(float(pos/n)))
    print("{:.6f}".format(float(neg/n)))
    print("{:.6f}".format(float(zer/n)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
                    








d = [{'a':1}, {'b':5}, {'e':10}]
for i in d:
    a,b = next(iter(i.items()))  = get key and value one by one. 
    print(a,b)


l = ['fc1/22', 'fc1/10', 'fc1/20']
l.sort(key=lambda x: int(x.split('/')[1]))   sort the list with lambda doing some operation in each key
print(l)

