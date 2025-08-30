"""Median related questions.

Median is middle value between smallest and largest numbers.

Median can found by sorting array:
Odd number: n / 2
0, 2, 4, 6, 8 => 4

Even number: Two medians n / 2 - 1 and n / 2
0, 2, 4, 6 => 2, 4

Or by getting smallest and largest values and getting mean of them.

If array is unsorted:
    max-heap to find the k-th largest element
    max-heap and min-heap to find largest and smallest
    Random partitioning (Quick Select)
"""


def get_median_by_sorting(data):
    n = len(data)
    if not n:
        raise ValueError("No data")
    data = sorted(data)
    i = n // 2
    if n % 2==0:  # Even
        return (data[i - 1] + data[(i)]) / 2
    else:  # Odd
        return data[i]
