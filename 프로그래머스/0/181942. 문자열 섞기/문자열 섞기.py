def solution(str1, str2):
    # 둘의 길이가 같음
    result = []
    for i in range(len(str1)):
        result.append(str1[i])
        result.append(str2[i])
    
    return "".join(result)