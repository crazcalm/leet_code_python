"""
There are 8 prison cells in a row, and each cell is either
occupied or vacant.

Each day, whther the cell is occupied or vacant changes
according to the following rules:

    - If a cell has two adjacent neighbors that are both
      vacant, then the cell becomes occupied.

    - Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and
the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way:
    cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0

Given the initial state of the prison, return the state of
the presion after N days (and N such changes described above).

Example 1:
    Input: cells = [0,1,0,1,1,0,0,1], N = 7
    Output: [0,0,1,1,0,0,0,0]
    Explanation:
        The following table summarizes the state of the
        prison on each day:

        Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
        Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
        Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
        Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
        Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
        Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
        Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
        Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
    Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
    Output: [0,0,1,1,1,1,1,0]
"""

from typing import List


def soltion(cells: List[int], n: int) -> List[int]:
    for _n in range(n):
        tempt = [0] * len(cells)
        for x in range(1, len(cells) - 1):
            if cells[x - 1] == cells[x + 1]:
                tempt[x] = 1
            else:
                tempt[x] = 0

        cells = tempt
    return cells


def solution_2(cells: List[int], n: int) -> List[int]:
    # The trick is to noticed the possible soltions
    # start to repeat after the 14th day.
    days = 14
    if n % 14 != 0:
        days = n % 14

    return soltion(cells, days)


if __name__ == "__main__":

    for days in range(29):
        test_1 = [0, 1, 0, 1, 1, 0, 0, 1]
        print(
            f"Example 1 soltion day ({days}):\n brute force -> {soltion(test_1, days)}\n opimized ----> {solution_2(test_1, days)}\n"
        )
