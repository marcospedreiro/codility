#!/usr/bin/env python

def PermMissingElem(A):
    aLen = len(A)
    N = aLen + 1
    total = (N*(N+1)) / 2
    
    sum = 0
    
    for a in A:
        sum += a
    
    return total - sum

A = [2, 3, 1, 5]
assert(PermMissingElem(A) == 4)