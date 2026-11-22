def solution(x):
    # 하샤드 수
    # 만약 입력 받은 x가 하샤드 수라면, x의 자리수 합으로 x가 나누어져야 하샤드 수
    # ex) 12는 1+2 = 3이기에, 12는 3으로 나누어 떨어지기 때문에 12는 하샤드 수
    
    st = str(x)
    result = 0
    for s in st:
        result += int(s)
    
    if x % result == 0:
        return True
    else:
        return False