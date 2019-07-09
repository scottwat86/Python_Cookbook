#               Python Cookbook
#               Chapter 1 - Data Structures and Algorithms

#                1.1 Unpacking a SEQUENCE / LIST / ITERABLE into a separate variable

"""
Problem you have an N-element tuple or sequence
that you would like to unpack into a collection of N-variables.

(X_1,X_2,....X_n) -> x,y,...z
"""

p = (4, 5)      # TUPLE
x, y = p        # Tuple unpacking
print(f" x = {x} \n y = {y}")

data = ['ACME', 50, 91.1, (2012,  12,  21) ]  # LIST of various object types
name, share, price, (year, mon, day) = data   # Unpacking list to variables
print(f"""
Name: {name}
Share: {share}
Price: {price}
Date: {mon}-{day}-{year}
""")

# Unpacking iterable with throw away variable _
_, shares, price, _ = data

#               1.2 Upacking iterables of unknown length
"""
Problem: Unpacks ITERABLES with unknown length
"""
from statistics import mean     # Import mean function from statistics module

# Defines function that drops the first / last grade and returns mean of grades
def drop_first_last(grades):
    first, *middle, last = grades
    return (mean(middle))

drop_first_last([1,2,2,2,1] )   # Call function to return "middle" mean of grades

#   Unpacks first var and last tuple variable, remaing is thrown away to  _
name, *_,  (*_, year) = data
print(year)

#   Unpacks ":" delimited string to variables
line = "nobody:*:-2:2:Unpriviliged User:/var/empty:/usr/bin/false"
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

# Imports deque function from collections
from collections import deque

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
