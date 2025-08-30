# Common
```
OPS = {
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y
}
```
Result is the last item in stack
Follow operands


# Polish (PN, NPN or prefix) notation
https://en.wikipedia.org/wiki/Polish_notation

Operators proceed operands
```
+ 3 4
* - 5 6 7 => (5 - 6) * 7
```
Go right to left, only need operands (values) stack
once we have an operator, pop twice

# Reversed polish (RPN or postfix) notation
https://en.wikipedia.org/wiki/Reverse_Polish_notation
```3 4 *```

Operators follow operands
Go left to right, only need operands (values) stack
Once have an operator, pop twice


# Infix notation
Regular notation: ```3+5*2-1 -> 12```
More difficult to parse, need two stacks for operands and operators

Parents make it easier (Dijksta calculator)
```(1+((2+3)*(4*5))) = 101```
This is similar to PN or RPN, but evaluation begins at the right parent


