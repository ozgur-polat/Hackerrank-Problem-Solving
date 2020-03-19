#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if(i<0):
            neg+=1
        elif(i>0):
            pos+=1
        else:
            zer+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))