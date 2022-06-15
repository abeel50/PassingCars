def countPairs(A, start):
    print(start)
    if start >= len(A):
        return 0
    if A[start] == 0:
        p = A[start + 1:].count(1)
        # print (p)
        return p + countPairs(A, start + 1)
    return 0 + countPairs(A, start+1)

def solution(A):
    # write your code in Python 3.6
    # comb = combinations(range(0,len(A)),2)
    # pairs = 0
    # for i,j in comb:
    #     if A[i] == 0 and A[j] == 1:
    #         # print(i,j, A[i]+A[j])
    #         pairs += 1
    return countPairs(A,0)