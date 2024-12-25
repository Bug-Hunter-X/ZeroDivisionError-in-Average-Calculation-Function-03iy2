# Python ZeroDivisionError Bug

This repository demonstrates a common error in Python: the ZeroDivisionError that occurs when attempting to calculate the average of an empty list.

The `bug.py` file contains the buggy code, which fails to handle the empty list case. The `bugSolution.py` file provides a corrected version that gracefully handles empty inputs.

## Bug Description

The `calculate_average` function does not check if the input list is empty before performing the division. This leads to a `ZeroDivisionError` when called with an empty list.

## Solution

The solution involves adding a conditional statement to check if the list is empty. If it is empty, the function returns 0; otherwise, it proceeds with the calculation.