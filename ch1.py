#               Python Cookbook
#               Chapter 1 - Data Structures and Algorithms

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
