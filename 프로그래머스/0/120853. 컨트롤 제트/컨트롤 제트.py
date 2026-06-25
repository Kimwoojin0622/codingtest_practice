def solution(s):
    temp = s.split(" ")
    result = 0
    # Z는 0번 인덱스부터 시작하지 않음
    for i in range(len(temp)):
        if temp[i] == 'Z':
            result = result - int(temp[i - 1])
        else:
            result = result + int(temp[i])
    
    return result
