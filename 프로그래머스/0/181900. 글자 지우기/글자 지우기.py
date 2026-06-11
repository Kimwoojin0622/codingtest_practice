def solution(my_string, indices):
    # my_string에서 indices와 반대인 인덱스들을 리스트에 담고 이들을 result에 출력
    rep_indices = [i for i in range(len(my_string)) if i not in indices]
    
    result = []
    for n in rep_indices:
        result.append(my_string[n])
    
    return "".join(result)
    