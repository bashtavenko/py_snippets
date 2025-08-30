"""Recursion bootcamp."""


def gcd(x, y):
    return x if y==0 else gcd(y, x % y)


if __name__=="__main__":
    print(gcd(156, 36))
    print(gcd(50, 6))
