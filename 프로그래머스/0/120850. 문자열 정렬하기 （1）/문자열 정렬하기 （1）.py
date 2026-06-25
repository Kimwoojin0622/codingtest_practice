def solution(my_string):
    chk_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = []
    for s in my_string:
        if s in chk_num:
            num = int(s)
            result.append(num)
    
    result.sort() # O(N log N)
    return result