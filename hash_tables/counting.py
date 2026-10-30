items = ["apple", "orange", "apple", "pineapple", "tomato", "tomato", "bread"]

d = {}
for i in items:
    d[i] = d.get(i, 0) + 1
print(d)
