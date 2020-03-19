#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    fiveSum=[]
    for i in arr:
        temp = arr.copy()
        temp.remove(i)
        tempSum=0
        for j in temp:
            tempSum+=j
        fiveSum.append(tempSum)
    print(str(min(fiveSum))+" "+str(max(fiveSum)))