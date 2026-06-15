def solution(myString, pat):
    length, cnt = len(pat), 0
    for i in range(len(myString)):
        chk = myString[i : length]
        if chk == pat:
            cnt += 1
        if length == len(myString):
            break
        length += 1
    return cnt
        
            
            