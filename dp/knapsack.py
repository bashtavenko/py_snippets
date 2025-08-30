"""16.6 The Knapsack.

Make decisions. What if an item is chosen (provided that it fits into knapsack) or NOT chosen?
Check both options and get the max.

If capacity is 5, the optimum solution is 2 + 3 = $220
Greedy won't work because the highest cost per pound is
item 1 and the next one is item 2 which will end up being
1 + 2 = $160
                            Capacity is 5 lb
Item Value Weight              0  1  2   3   4   5
1     $60   1            1     0  0  60  60  0   60
2     $100  2            1-2   0  0  100 0   0   160
3     $120  3            1-3   0  0  0   0   0   220

220 because with current item it is
$220 ($120 + $100) and without it $160
$100 is because item 3 has weight of 3 and without it
we should look at 5 - 3 = a[2][2]

                             Capacity is 5 lb
Item Value Weight              0  1  2  3  4  5
1     $60   5            1     0  0  0  0  0  60
2     $50   3            1-2   0  0  0  50 50 60
3     $70   4            1-3   0  0  0  50 70 70
4     $30   2            1-4   0  0  30 50 70 80
80 is because with current item it is
$80 ($50 + $30) and without it $70
$50 is a[4][3] = 50
"""
import collections

Item = collections.namedtuple('Item', ('value', 'weight'))


def optimum_subject_to_capacity(items, capacity):

  def select(k, weight_left):
    """Returns optimum value for the given k and capacity."""
    if k < 0:
      # No items can be chosen.
      return 0

    if V[k][weight_left] == -1:
      without_current_item = select(k - 1, weight_left)  # It is not concern of this recursion
      with_current_item = (0 if weight_left < items[k].weight else (
          items[k].value + select(k - 1, weight_left - items[k].weight))) # This value + previous
      V[k][weight_left] = max(without_current_item, with_current_item)

    return V[k][weight_left]

  # If we have 5 items and capacity of 7, we will have 5 rows x 7 columns
  # matrix initially filled with -1 so that V[0][2] is the value of the first item
  # if capacity is 2.
  V = [[-1] * (capacity + 1) for _ in items]
  result = select(len(items) - 1, capacity)
  return result
