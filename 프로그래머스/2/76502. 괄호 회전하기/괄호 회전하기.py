def solution(s):
    # O(N^2) 가능
    li, result = [t for t in s], 0

    for i in range(-1, len(s)-1): # O(N^2)
        tmp = li[i+1:]+li[:i+1]
        check = []
        for j in range(0, len(tmp)):
            check.append(tmp[j])
            if len(check) >= 2:
                brackets = check[-2] + check[-1]
                if brackets == '[]' or brackets == '{}' or brackets == '()':
                    check.pop()
                    check.pop()
        if not check:
            result += 1
    
    return result