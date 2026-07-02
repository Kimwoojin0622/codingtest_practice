def solution(bin1, bin2):
    # 2진수 -> 10진수
    a = int(bin1, 2)
    b = int(bin2, 2)

    result = bin(a + b).replace('0b','')
    
    return result