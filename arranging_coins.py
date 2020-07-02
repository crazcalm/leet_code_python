"""
You have a total of n coins that you want to form in a staircase shape,
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be
formed.

n is a non-negative integer and fits within the range of 32-bit
signed integer.

Example 1:
    n = 5

    The coins can form the following rows:
    x
    xx
    xx

    Because the 3rd row is incomplete, we return 2.


Example 2:
    n = 8

    x
    xx
    xxx
    xx

    Because the 4th row is incomplete, we return 3.
"""


def arrange_coins(n: int) -> int:
    count = 0
    start_point = n + 1  # +1 to compensate for the range()
    for x in range(1, start_point):
        if n - x >= 0:
            count += 1
            n -= x
        else:
            break

    return count


if __name__ == "__main__":
    print(f"n=5 -> {arrange_coins(5)}")
    print(f"n=8 -> {arrange_coins(8)}")
