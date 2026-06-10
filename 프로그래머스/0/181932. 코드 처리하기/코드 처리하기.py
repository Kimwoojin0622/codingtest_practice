def solution(code):
    mode = 0
    ret = ''
    # step 1. 리스트 처음부터 끝까지 for 문으로 돌린다. len() 써서, 시작할 때 mode는 0임
    for i in range(len(code)):
        # step 2. mode == 0
        # step 2-1. 만약 code[i]가 1이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[i]를 추가한다.
        if mode == 0:
            # step 2-2. 근데 code[i]가 == 1이면 mode를 0에서 1로 바꾼다.
            if code[i] == '1':
                mode = 1
            else:
                if i % 2 == 0:
                    ret = ret + code[i]
        # step 3. mode == 1
        # step 3-1. 만약 code[i]가 1이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[i]를 추가
        elif mode == 1:
            if code[i] == '1':
                mode = 0
            # step 3-2. code[i]가 == 1이면 mode를 1에서 0으로 바꾼다.
            else:
                if i % 2 != 0:
                    ret = ret + code[i]
    # step 4. ret이 만들어졌는데 빈 문자열이면 EMPTY를 return
    if ret:
        return ret
    else:
        return 'EMPTY'

    
        
    

        
        
        
        
    