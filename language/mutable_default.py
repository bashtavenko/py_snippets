"""
Mutable default arguments are dangerous.
They are evaluated once when the function is defined, not each time the function is called.
"""

def fun_a(a: int, b: list = []):
    b.append(a)
    return b


print(fun_a(1))
print(fun_a(2))
print(fun_a(3))
print(fun_a(4, []))

# [1]
# [1, 2]
# [1, 2, 3]
# [4]
