def solution(A):
    N = len(A)
    print(len(A))
    result = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] != A[j]:
                result = max(result, j - i)
    return result


print(solution([4, 6, 2, 2, 6, 6, 4]))


N = 10
i = 1
for j in range(i, N):
    print(j)
