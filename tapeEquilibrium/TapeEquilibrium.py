#!/usr/bin/env python

#A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.
#    Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
#        A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N - 1].
#    The difference between the two parts is the value of:
#        |(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|
#    IE: The absolute difference between the sum of the first part and the sum of the second part.
#Given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.

def TapeEquilibrium(A):    
    ALen = len(A)
    sum = 0
    for i in range(0,ALen):
        sum += A[i]
        
    low = 0
    up = sum
    
    for i in range(1,ALen):
        low = low + A[i-1]
        up = sum - low
        diff = abs(low - up)
        if i == 1:
            min = diff
        if diff < min:
            min = diff
    return min


A = [3, 1, 2, 4, 3]
te = TapeEquilibrium(A)
print('Excepted:\n1')
print('got: ')
print(te)