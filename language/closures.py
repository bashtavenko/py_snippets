"""Closures."""

increment_by_i = [lambda x: x + i for i in range(10)]

# This creates a list of 10 functions with 'x' parameter

print (increment_by_i[3](4))

# Call third function with param of '4' this returns 13 (9 + 4) rather than 7 (3
# + 4) because functions created in the loop have the same scope and 'i' at the
# end is '9' and that '9' shared between all 10 instances

