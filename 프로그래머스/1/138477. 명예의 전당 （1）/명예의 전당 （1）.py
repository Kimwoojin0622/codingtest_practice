def solution(k, score):
    # O(N^2) 가능
    result = [] # 최솟값 리스트
    tmp = [] # 명예의 전당 리스트
    for i in range(len(score)):
        if len(tmp) < k:
            tmp.append(score[i])
            tmp.sort(reverse=True) # O(n log n)
            result.append(tmp[-1])
        else:
            if score[i] > tmp[-1]:
                tmp[-1] = score[i]
                tmp.sort(reverse=True)
                result.append(tmp[-1])
            else:
                result.append(tmp[-1])

    return result