def solution(s):
    number_eng = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    
    result = ''
    tmp = ''
    
    for st in s:
        if not st.isdigit():
            tmp += st
            if tmp in number_eng.keys():
                result += str(number_eng[tmp])
                tmp = ''
        else:
            result += st
    
    return int(result)