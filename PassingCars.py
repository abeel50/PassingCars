from itertools import combinations

def solution(A):
    # write your code in Python 3.6
    comb = combinations(range(0,len(A)),2)
    pairs = 0
    for i,j in comb:
        if A[i] == 0 and A[j] == 1:
            # print(i,j, A[i]+A[j])
            pairs += 1
    return pairs