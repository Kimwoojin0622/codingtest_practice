def solution(my_string):
    # A의 아스키코드 65
    tmp = my_string
    result = 0
    
    for s in tmp:
        if ord(s) >= 65:
            tmp = tmp.replace(s, ' ')
    tmp = tmp.strip()
    chk = tmp.split(" ")
    
    for data in chk:
        if data:
            result += int(data)
    
    return result