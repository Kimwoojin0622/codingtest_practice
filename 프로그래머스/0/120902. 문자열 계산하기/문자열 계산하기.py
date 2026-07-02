def solution(my_string):
    tmp = my_string.split(" ")
    result = int(tmp[0])
    for i in range(1, len(tmp) - 1):
        if tmp[i] == '+':
            result += int(tmp[i + 1])
        elif tmp[i] == '-':
            result -= int(tmp[i + 1])
        else:
            continue
        
    
    return result