#References
https://algs4.cs.princeton.edu/92search/
https://algs4.cs.princeton.edu/lectures/  
[original version](https://algs4.cs.princeton.edu/lectures/99GeometricSearch-2x2.pdf)  
[new version](http://www.cs.princeton.edu/courses/archive/spring13/cos226/lectures/99GeometricSearch.pdf)  
[kdtrees](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/kdtrees.pdf)

Pre-process data to answer queries efficiently

NNS  
Find closest neighbour in terms of squared Euclidean or Manhattan distance

##Simplest 1D case
### Option 1 - linear search
O(n) time, however in some cases it may make sense to pre-process to achieve
better running time

### Option 2 - binary search
* Sort in O(n * log(n)) time, although not necessarily true - we could insert into
O(n) time (shift elements to accommodate new and double array if needed)
* modified binary search, get median, calc distance, go left or right
That would run in O(n) time

Problem with this approach:
* No add / delete support, although we could the balanced BST
* No support for higher dimensions

## 2D case
### KD tree
Alternate node levels for X and Y
Can search by rectangle

Building KD tree: presort on x and y and then partition on median element
to ensure tree is balanced
Then the same partitioning is used in range search
Nearest neighbour - still calculates to each point but eliminates
half of the points
Same idea as in 1d search - find mid, get distance, go left or right

### Other methods
* Interval Search Tree
* Grid
* Quadtree
  Node has four children (NW, NE, SW, SE)
* Approximation
* Greedy

