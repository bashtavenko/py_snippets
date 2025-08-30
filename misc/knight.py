"""Foo."""

G = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}


def calc(start, length):
    if length < 1:
        return 0
    if length==1:
        return 1
    return sum(calc(next, length - 1) for next in G[start])


def calc_1(start):
    return calc_2(start, 1)  # 1424


def calc_2(i, n):
    if n==10:
        return 1
    return sum(calc_2(p, n + 1) for p in G[i])


def calc_3(i, n, cache={}):  # Didn't quite work, 2592 / wtf?
    if n==10:
        return 1
    key = "".format("{0}{1}", i, n)
    if key not in cache:
        cache[key] = sum(calc_3(p, n + 1, cache) for p in G[i])
    return cache[key]


if __name__=="__main__":
    # print calc(1, 10)
    print(calc_3(1, 1))
    # print calc_1(1)
