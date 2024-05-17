#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

if __name__ == '__main__':
    s = int(input().strip())

    for _ in range(s):
        n = int(input().strip())
        res = stepPerms(n)
        print(res)
