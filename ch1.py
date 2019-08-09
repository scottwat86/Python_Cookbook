#               Python Cookbook
#               https://d.cxcore.net/Python/Python_Cookbook_3rd_Edition.pdf
#               Chapter 1 - Data Structures and Algorithms

###############################################
#                1.1 Unpacking a SEQUENCE / LIST / ITERABLE into a separate variable

"""
Problem you have an N-element tuple or sequence
that you would like to unpack into a collection of N-variables.

(X_1,X_2,....X_n) -> x,y,...z
"""
print('*********')
p = (4, 5)      # TUPLE
x, y = p        # Tuple unpacking
print('x = ' + str(x),'\ny = ' + str(y)+ '\n')

print('\n*********')
data = ['ACME', 50, 91.10, (2012, 12, 21), 'junk']  # LIST of various object types
name, share, price, (year, mon, day), _ = data   # Unpacking list to variables
print(f"""
Name: {name}
Share: {share}
Date: {mon}-{day}-{year}
Price: $%.2f
""" % price)


###############################################
# 1.2 Unpacking Elements from Iterables of Arbitrary Length
"""
Problem: Unpacks ITERABLES with unknown length
"""
print('\n*********')
grades = sorted([70, 77, 88, 99, 100, 50])
low, *middle, high = grades
print(f'Low Score: {low}\nHigh Score: {high}')

print('\n*********')
from statistics import mean     # Import mean function from statistics module

# Defines function that drops the first / last grade and returns mean of grades
print('\n*********')
def drop_first_last(grades):
    first, *middle, last = grades
    return (mean(middle))

drop_first_last([1,2,2,2,1] )   # Call function to return "middle" mean of grades

#   Unpacks first var and last tuple variable, remaing is thrown away to  _
print('\n*********')
name, *_,  (*_, year) = data
print(year)

#   Unpacks ":" delimited string to variables
print('\n*********')
line =  'user_name:*:-2:-1:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh= line.split(":")
print(f"""
{uname}      nobody
{fields}       ['*', '-2', '2', 'Unpriviliged User']
{homedir}   /var/empty
{sh}            /usr/bin/false
""")

###############################################
#               1.3 Keeping the Last N Items
"""
You want yo keep a limited history of the last few items seen during iterations or during some
other kind of processing.
"""
print('\n*********')
# Imports deque function from collections
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(f'Queue: {q}')

print('\n*********')
# defines function with lines, patterm, history defaulted to 5 as input
def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

        # Example of use on a file
if  __name__ == '__main__':
    with open("somefile.txt") as f:
        for line, prevlines in search(f, "python", 10):
            for pline in prevlines:
                print(pline, end="")
                print(line, end="")
                print('-'*20)

###############################################
# 1.4 Finding the Large or Smallest N Items
# priority queue algorithm
print('\n*********')
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('Largest 3: ', heapq.nlargest(3, nums))
print('Smallest 3:', heapq.nsmallest(3, nums))

print('\n*********')
# import heapq

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
  {'name': 'FB', 'shares': 200, 'price': 21.09},
  {'name': 'HPQ', 'shares': 35, 'price': 31.75}]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f'Cheap Stock: {cheap}')
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(f'Expensive Stock: {expensive}')


###############################################
# 1.5 Priority Queue that sorts by priority and always returns highest priority

import heapq
class PriorityQueue:
    """
    Class implements a priority queue of a list using heapq

    # EXAMPLE
        class Item:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return 'Item({!r})'.format(self.name)

        INSTANTIATE PRIORITYQUEUE OBJECT
        q = PriorityQueue() #

        ASSEMBLING PRIORITY QUEUE ELEMENT
        q.push(Item('foo'), 1)
        q.push(Item('bar'), 5)
        q.push(Item('spam'), 4)
        q.push(Item('grok'), 1)

        POPPING HIGHEST PRIORITY FIRST
        print(q.pop())      # Item('bar')
        print(q.pop())      #Item('spam')
        print(q.pop())      # Item('foo')
        print(q.pop())      # Item('grok')   -> grok was added last and was popped last

    """

def __init__(self):
     """ Init Method intialized local variables """
     self._queue = []
     self._index = 0  # Differentiates between objects with same priority

def push(self, item, priority):
    """ Push Method takes self, item, priority as input and adds to sorted queue"""
    # (-)priority to reverse with highest priority first
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1

def pop(self):
    """ Pop Method takes in self as input and returns the highest priority item in the queue """
    return heapq.heappop(self._queue)[-1]

###############################################
#    1.6 Mapping Keys to Multiple Values in a Dictoionary aka MULTIDICTIONARY

# Simple Method
# Use [list] if you want to preserve the insertion order
# Use {set} to eliminate duplicates and order isn't important
d = {
                'a': [1, 2, 3],
                'b': [4, 5]
      }

e = {
        'a': {1, 2, 3},
        'b': {4, 5}
       }

# More Sophisticated Method
# CAUTION - defaultdict creates items that don't exist if access is attempted
# defaultdict makes it easier to initialize the first value as you don't need to verify that it exists
from collections import defaultdict

pairs = [('yellow', 1), ('yellow', 3), ('blue', 4), ('red', 1), ('blue', 2)]

# list argument passed indicates the object
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

d['orange'].append(9)
d.items()  #dict_items([('yellow', [1, 3]), ('blue', [4, 2]), ('red', [1]), ('orange', [9])])
d['yellow'][1] #3

# set argument
s = defaultdict(set)
for key, value in pairs:
    s[key].add(value)

s.items()  #dict_items([('yellow', {1, 3}), ('blue', {2, 4}), ('red', {1})])
s['yellow'].pop() #1


###############################################
#    1.7 Keeping Dictionairiers in Order
# OrderedDict are useful for mapping/serialize/encoding dict into a different format -> JSON / YAML
# OderedDict are implemented with double link lists
# as a result they are more than TWICE THE SIZE of regular dictionaries
# -> MEMORY TRADE OFF with large data sets
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# OUTPUT    "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

#  1.8 Calculating with Dictionary Values
# NOTE zip() creates an iterator than can only be consumed once
prices =   {
                    'ACME': 45.25,
                    'AAPL': 612.78,
                    'IBM': 205.55,
                    'HPQ': 37.20,
                    'FB': 10.75
                }

min_price = min(zip(prices.values(), prices.keys()))  # swaps values for keys to find min price
min_price  # = (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys())) # swaps values for keys to find max price
max_price # = (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
prices_sorted # [(10.75, 'FB'), (37.2, 'HPQ'), (45.25, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# KEY ONLY
min(prices, key=lambda k: prices[k])  #'FB'
# VALUE ONLY
min_value = prices[min(prices, key=lambda k: prices[k])] # 10.75


###############################################
# 1.9 Finding Commonalities in Two Dictionaries

a = { 'x': 1, 'y': 2, 'z': 3 }

b =  {'w': 10, 'x': 11, 'y': 2}

# Find keys in common
a.keys() & b.keys() # {'x', 'y'}

# & bitwise comparison

# Find keys in a that are not in b
a.keys() - b.keys() # {'z'}

# Find (key, value) pairs in common
a.items() & b.items() # {('y', 2)}

# Filtering dictionary contents
c = {key:a[key] for key in a.keys() - {'z', 'w'}} # {'x': 1, 'y': 2}

# keys() method return keys-views which support common SET operations eg union, intersection,
# items() method returns items-view (key, value) pairs; which also support similar SET operations
# values() DOES NOT SUPPORT set operations


###############################################
# 1.10 Removing Duplicates from a Sequence while Maintaining Order
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item) # LISTS -> remove this line
        if val not in seen: #  LISTS -> val is replaced with item
            yield item
            seen.add(val) #LISTS -> val is replaced with item

# a = [1, 5, 2, 1, 9, 1, 5, 10]
# list(dedup(a)) #[1, 5, 2, 9, 10]

a = [{'x': 1, 'y':2}, {'x':1, 'y':3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: (d['x']))) # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# Converting LIST to SET accomblished dedup but at the cost of losing the Order

# By using a generator dedupe() can be used to remove duplicate lines from a file

# Input 1\n1\n2\n2\n3\n3\n4\n
with open('test.txt', 'r') as f:
    for line in dedupe(f):
        print(line) # Output 1\n2\n3\n4\n

##################################
# 1.11 Naming a Slice
# General Rule Code with hardcoded index values lead to readability and maintenance problems
record = '..........................100             .................513.25   ...............'
SHARES = slice(26,30) # creates a slice object to be used later
PRICE = slice(60,67)
cost = int(record[SHARES]) * float(record[PRICE]) # 1325.0

string = '0123456'
a = slice(1,50,4)
b = slice(1,5,4)
a.start #1
a.stop #50
a.step #4
a.indices(len(string)) #(1, 7, 4) limited to end at 7 per string length
b.indices(len(string)) #(1, 5, 4)

##################################
# 1.12 Determing the Most Frequently Occuring Items in a Sequence
