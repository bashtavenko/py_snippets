# Things that I often forget in Python while switching from Java.
import itertools

# str
# 'ABRA KED' + '\xFE' + '47')

# conversions
# int('1')
# str(1)

# Ranges
# (start:stop:step)
# stop - stop BEFORE this, last one
# This is half-open slice
# range (n, m) contains m-n elements
range(3)  # from zero up to the number(not including, 0, 1, 2
range(1, 5)  # from number to number not including, 1, 2, 3, 4
range(2, -1, -1)  # From number down not including, 2, 1, 0

# Slicing
# Just like ranges but with ':' instead of ','
#  [start:stop:step]
# stop - stop BEFORE this, last one
# a[-1]  - last one
# a[::-1] - reverse list
# Can filter list with boolean
# my_list = [1, 2, 3, 4, 5]
# bool_list = [True, False, True, False, True]
# [1, 3, 5]
# Also [False:]
# [2, 3, 4, 5]

# List comp
[i for i in [1, 2, 3]]  # => [1, 2, 3]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# List stuff
a = list("abc")  # list from str
"".join(["a", "b", "c"])  # list str to str
# l.append(a) add one
# l.extend(bunch) add more

# Double for
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
[(i, j) for i in range(2) for j in range(3)]

# Ternary
"yahoo!" if 3 > 2 else "whatever"  # 'yahoo!'

# Some Python idioms
# for i in range(1 << size):  # Fancy way of shifting left
# 0 <= next_x < len(a)
# next = l1 or l2
# for _ in range(1, start):
# ~i == - i - 1
# b = next((x for x in a if x % 2 == 0), None)


# Itertools
# Running sum  1,2,3,4,5 --> 1 3 6 10 15
itertools.accumulate()
# Iterator slice. Can get iterator with sequence = iter(a)
# itertools.islice(sequence, k)
# itertools.groupby(s)

# Functools
# reduce(operator.mul, data)
# Returns value of two numbers for each iterable
# 0, 1, 2, 3, 4
# 1, 2, 3, 4
# 3, 3, 4
# 6, 4
# 10

# Conversion and checks
# .isdigit
# .isalnum

# Misc snippets
for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
    print(x, y)

# Histogram
hist = {}
t = [1, 2, 4]
for x in t:
    hist[x] = hist.get(x, 0) + 1
# Check for key => if "key1" in d


# IO
import io

with io.open("spam.txt", "w") as file:
    file.write("Spam and eggs!")

output = io.StringIO()
output.write("First line.\n")

# Intersect lists
requesters = [1, 2, 3]
BOTS = [4, 5]
any(id in requesters for id in BOTS)  # False

# Idioms
# a[next_even], a[next_odd] = a[next_odd], a[next_even]
# ~i == - i - 1
# useful in negative slicing a[~i]

# OR in assignment
# tail.next = l1 or L2
# AND in check
# ... and vals


# Duplicate elimination in list
[(i, x) for i, x in enumerate(a) if (i==0 or x!=a[i - 1])]
