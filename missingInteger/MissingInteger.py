#!/usr/bin/env python

#Write a function:
#def solution(A)
#that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer that does not occur in A.
#For example, given:
#  A[0] = 1
#  A[1] = 3
#  A[2] = 6
#  A[3] = 4
#  A[4] = 1
#  A[5] = 2
#the function should return 5.
#Assume that:
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
#Complexity:
#expected worst-case time complexity is O(N);
#expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
#Elements of input arrays can be modified.


# 100% score on codibility
def MissingInteger(A):
    # write your code in Python 2.7
    aLen = len(A)
    if aLen == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    
    countList = [0] * aLen
    for a in A:
        if a > 0 and a < aLen: # ignore invalid values
            countList[a] += 1
    
    for i in range(1, aLen):
        if countList[i] == 0:
            return i
        
    return aLen + 1