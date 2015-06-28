#!/usr/bin/env python

#The frog is currently located at position X and wants to get to a position greater than
#or equal to Y. The small frog always jumps a fixed distance, D.
#Count the minimal number of jumps that the small frog must perform to reach its target.
def FrogJmp(X, Y, D):
    orig = (Y-X)/D
    dec = (Y-X)/float(D)
    if dec-orig != 0:
        orig += 1
    return orig

X = 10
Y = 85
D = 30
assert(FrogJmp(X,Y,D) == 3)
