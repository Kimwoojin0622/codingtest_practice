def solution(my_string):
    chk = []
    for i in range(len(my_string)):
        chk.append(my_string[i:])
    result = sorted(chk)
    
    return result