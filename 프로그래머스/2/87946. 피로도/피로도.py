from itertools import permutations
def solution(k, dungeons):
    # 던전은 아무리 많아도 8개
    permutation_dungeons = list(permutations(dungeons))
    result = [0] * len(permutation_dungeons)
    
    for i in range(len(permutation_dungeons)):
        tmp = k
        count = 0
        for j in range(len(permutation_dungeons[i])):
            if tmp >= permutation_dungeons[i][j][0]:
                tmp = tmp - permutation_dungeons[i][j][1]
                count += 1
            else:
                break
        result[i] = count
    
    return max(result)