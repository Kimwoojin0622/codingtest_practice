def solution(age):
    # a부터 j까지 리스트에 삽입
    alpha = [chr(i) for i in range(ord('a'), ord('a') + 10)]
    
    result = ''
    for s in str(age):
        s = int(s)
        result = result + alpha[s]
    
    return result