from collections import deque
def solution(n, words):
    # O(N^2) 가능
    split = []
    for i in range(0, len(words), n):
        split.append(words[i:i+n])
    
    check = deque([split[0][0][0]])
    double_check = set()

    for j in range(len(split)):
        length = len(split[j])
        for k in range(length):
            # 중복
            if split[j][k] not in double_check:
                double_check.add(split[j][k])
            else:
                return [k+1, j+1]
            
            # 끝말잇기
            check.append(split[j][k][0])
            if check[0] == check[1]:
                check.popleft()
                check.popleft()
                check.append(split[j][k][-1])
            else:
                return [k+1, j+1]
    
    return [0, 0]