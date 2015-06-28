#!/usr/bin/env python

#A non-empty zero-indexed array A consisting of N integers is given.
#A permutation is a sequence containing each element from 1 to N once, and only once.
#given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
def PermCheck(A):
    # write your code in Python 2.7
    Alen = len(A)
    if Alen != len(set(A)):
        return 0
    
    max = A[0]
    for a in A:        
        if a > max:
            max = a
    
    if max != Alen:
        return 0
        
    return 1



    #Alen = len(A)
    #
    #if X > Alen:
    #    return -1
    #
    #path = [0] * X
    #earliest = -9
    #for i in range(0,Alen):
    #    if A[i] <= X and path[(A[i]-1)] == 0:
    #        path.remove(0)
    #        path.insert(A[i]-1, A[i])
    #        earliest = i
    #
    #if path.count(0) == 0:        
    #    return earliest
    #else:
    #    return -1