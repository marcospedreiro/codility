#!/usr/bin/env python
import string

# Perform an in place word reversal of a given string
# Args: string S
# Example: 'we test coders' -> 'ew tset sredoc'
def wordReverse(S):
    S = S.strip()
    chars = list(S)
    chLen = len(chars)
    first = last = 0
    while first < chLen and last < chLen:
        if chars[last] != ' ' and last != chLen-1:
            last += 1
        else:
            if last == chLen-1:
                last += 1
            reverseChars(chars, first, last)
            last += 1
            first = last
    sRev = ''.join(chars)
    return sRev

# Performs an inplace element reversal of a given array within the bounds of
# first, (last-1). If first >= (last-1), or are not in the bounds of A, returns A unchanged
# Example: A = [1, 2, 3, 4], first = 0, last = 2 -> A = [3, 2, 1, 4]
def reverseChars(A, first, last):
    aLen = len(A)
    last -= 1
    if(first > last or first > aLen or last > aLen or first < 0 or last < 0):
        return A
    
    while(first < last):
        temp = A[first]
        A[first] = A[last]
        A[last] = temp
        first += 1
        last -= 1
    return A

testString = 'we test coders'
print(testString)
print(wordReverse(testString))
