"""Exercise 1: Sorting lists of numbers
"""

from typing import List
import time
import math
import random

import matplotlib.pyplot as plt

def naive_sort(numbers_to_sort: List[int]) -> List[int]:
    """Naively sort a list from low to high

    Each pass through the list removes the smallest integer
    and appends it to a new list.  The new list is returned.
    The old list is destroyed in the process.

    Parameters
    ----------
    numbers_to_sort : List[int]
        List of integers to sort.

    Returns
    -------
    List[int]
        Sorted list
    """

    sorted_numbers = []

    # This outer loop is for our passes - if the number of items in
    # the list is 4, then this loop will execute 2 times.
    for iter in range(len(numbers_to_sort)-1):

        # Find the smallest integer for this pass
        smallest_int = max(numbers_to_sort)+1
        smallest_index = None
        for index, x in enumerate(numbers_to_sort):
            if x <= smallest_int:
                smallest_int = x
                smallest_index = index

        # Remove the smallest integer and append to new list
        sorted_numbers.append(smallest_int)
        numbers_to_sort.pop(smallest_index)

    # Finally append the final element in the list.
    sorted_numbers.append(numbers_to_sort.pop())

    # Make sure numbers_to_sort is empty and return.
    assert(len(numbers_to_sort)==0)
    return sorted_numbers


def bubble_sort(numbers_to_sort: List[int]) -> List[int]:
    """Sort a list from low to high using the bubble sort algorithm.

    On each iteration we go through the list swapping pairs of
    integers if they have the wrong ordering.  The list is modified
    in place.

    Parameters
    ----------
    numbers_to_sort : List[int]
        List of integers to sort.
    """

    sorted = False
    while not sorted:

        sorted = True
        for index in range(len(numbers_to_sort)-1):
            if numbers_to_sort[index]>numbers_to_sort[index+1]:
                numbers_to_sort[index+1], numbers_to_sort[index] = numbers_to_sort[index], numbers_to_sort[index+1]
                sorted = False

    return numbers_to_sort


if __name__=="__main__":
    # Check the naive sort works.
    result = naive_sort([5,2,1,6,2,3,9,7,8,11])
    assert(result == [1,2,2,3,5,6,7,8,9,11])

    # Check the bubble sort works.
    result = bubble_sort([5,2,1,6,2,3,9,7,8,11])
    assert(result == [1,2,2,3,5,6,7,8,9,11])

    # Do a timing exercise to check scalability - we
    # expect O(N^2) scaling from our naive algorithm, and
    # somewhere between O(N) and O(N^2) from bubble sort.
    scales_to_check = [10, 20, 50, 100, 200, 500, 1000, 5000]
    duration_python = []
    duration_naive = []
    duration_bubble = []
    for s in scales_to_check:
        x = [random.randint(0,1000) for index in range(s)]
        time_start = time.perf_counter()
        x.sort()
        duration_python.append(time.perf_counter() - time_start)

        x = [random.randint(0,1000) for index in range(s)]
        time_start = time.perf_counter()
        naive_sort(x)
        duration_naive.append(time.perf_counter() - time_start)

        x = [random.randint(0,1000) for index in range(s)]
        time_start = time.perf_counter()
        bubble_sort(x)
        duration_bubble.append(time.perf_counter() - time_start)

    # If we have O(N^2) scaling then time = CN^2 or log(time) = log(C) + 2*log(N).  If we have
    # O(NlogN) scaling then time = CNlog(N).  Let's try to estimate these constants
    # from the data.
    C_naive = sum([d/(s*s) for d,s in zip(duration_naive,scales_to_check)])/len(scales_to_check)
    C_python = sum([d/(s*math.log(s)) for d,s in zip(duration_python,scales_to_check)])/len(scales_to_check)

    # Plot the result.
    plt.loglog(scales_to_check, duration_naive, 'o-', label="Results: Naive")
    plt.loglog(scales_to_check, duration_bubble, 'o-', label="Results: Bubble")
    plt.loglog(scales_to_check, duration_python, 'o-', label="Results: Python builtin")
    plt.loglog([10,5000], [C_naive*(10**2), C_naive*(5000**2)], label=r"$\mathcal{O}(N^2)$")
    plt.loglog([10,5000], [C_python*10*math.log(10), C_python*5000*math.log(5000)], label=r"$\mathcal{O}(N\log{N})$")
    plt.xlabel("N")
    plt.ylabel("Runtime [s]")
    plt.legend()
    plt.show()
