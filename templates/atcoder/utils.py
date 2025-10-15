# Common utilities for CP
import sys
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
INF = 10**18

def chmin(a, b):
    return b if b < a else a

def chmax(a, b):
    return b if b > a else a
