"""Compute the numerical factorial function"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


def compute_iterative_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    if value < 0:
        # not covered
        ValueError("Inputs of 0 or grater!")
    result = 1
    while value != -1:
        result *= value
        value -= 1
    return result


def compute_recursive_factorial(value):
    if value < 1:
        return 1
    else:
        return value * compute_recursive_factorial(value - 1)


def compute_hashmap_recursive_factorial(value):
    dict = {0: 1}
    if value not in dict:
        dict[value] = value * compute_hashmap_recursive_factorial(value - 1)
    return dict[value]



def h(x):
    """Silly function."""
    if 0:   #pragma: no cover
        pass
    if x == 1:
        a = 1
    else:
        a = 2


def main1():
    a = compute_iterative_factorial(10)
    h(3)
    print(a)

def main2():
    b = compute_hashmap_recursive_factorial(14)
    h(1)
    print(b)

if __name__ == "__main__":
    main1()
    main2()
