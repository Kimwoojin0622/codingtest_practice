from collections import Counter
def solution(k, tangerine):
    # tangerine 중복제거
    size_of_tangerine = Counter(tangerine)
    
    # 귤의 size마다 개수 구하기
    size_and_count = []
    for size in size_of_tangerine:
        size_and_count.append([size, size_of_tangerine[size]])
    
    # 사이즈가 큰 순서대로 나열
    size_and_count = sorted(size_and_count, key=lambda x : -x[1])
    
    # box에 담기
    box = 0
    result = 0
    
    for tanger in size_and_count:
        box += tanger[1]
        result += 1
        if box >= k:
            return result