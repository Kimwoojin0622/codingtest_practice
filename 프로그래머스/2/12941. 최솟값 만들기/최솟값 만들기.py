def solution(A, B):
    sort_A = sorted(A)
    sort_B = sorted(B, reverse=True)
    
    result = 0
    for i in range(len(sort_A)):
        result += sort_A[i] * sort_B[i]
    
    return result