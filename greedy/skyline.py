"""17.8 Compute the largest rectangle under skyline

6          x     x x
5        x x     x x x
4    x   x x     x x x
3    x   x x x   x x x
2    + + + + + + + + + +   x
1  x + + + + + + + + + +   x
0  x + + + + + + + + + + x x
   0 1 2 3 4 5 6 7 8 9 1 1 12

Largest contained rectangle: 2 x (11 - 1) = 20
The tallest rectangle: 6 x (9 - 7) = 12
Widest: 1 x (11 - 0) = 11

Brute force: take pairs, find minimum and area
Brute force: for each i the furthest left and right we can
go without dropping below A[i], i.e. the largest rectangle
that is supported by building j (pilar)
Don't need to go all the way back, can store indices in the stack.
"""


def calculate_largest_rectangle(heights):
    pillar_indices, max_area = [], 0
    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_area = max(max_area, height * width)
        pillar_indices.append(i)
    return max_area
