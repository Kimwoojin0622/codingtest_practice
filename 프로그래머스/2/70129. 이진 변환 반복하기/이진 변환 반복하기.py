def solution(s):
    is_True = True
    zero_cnt = 0
    cnt = 0
    
    while is_True:
        if s == '1':
            is_True = False
        else:
            # cnt
            cnt += 1
            
            # 0 개수 구하기
            zeros = s.count("0")
            zero_cnt += zeros
            
            # 0 제거
            s = s.replace("0", "")
            
            # 0 제거 후 길이
            change_length = len(s)
            
            # 길이만큼 이진변환
            bi = bin(change_length)[2:]
            s = bi
            
    return [cnt, zero_cnt]