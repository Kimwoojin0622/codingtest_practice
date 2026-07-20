def solution(n):
    tmp = []
    # 앞뒤 반전 3진법 만들기
    while True:
        if n >= 3:
            div = n % 3
            tmp.append(div)
            n = n // 3
        elif n < 3:
            tmp.append(n)
            break
    
    # 10진법으로 변환
    length, result = len(tmp) - 1,  0
    for n in tmp:
        cal = n * (3 ** length)
        length -= 1
        result += cal
        
    return result