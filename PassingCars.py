
def solution(A):
    zeroCount, pairs = 0,0
    for i in A:
        if i == 0:
            zeroCount+=1
        else:
            pairs += zeroCount
    return -1 if pairs > 1000000000 else pairs