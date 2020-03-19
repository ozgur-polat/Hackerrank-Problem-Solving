#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        temp=" "*(n-1-i)+"#"*(i+1)
        print(temp)