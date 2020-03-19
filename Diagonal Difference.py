#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    for i in range(len(arr)):
        d1+=arr[i][i]
        d2+=arr[i][len(arr)-1-i]

    return abs(d1-d2) 