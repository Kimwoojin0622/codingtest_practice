def solution(s):
    table = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
    }
    
    tmp_list = []
    tmp = ''
    for data in s:
        if data.isdigit():
            tmp_list.append(str(data))
        else:
            tmp = tmp + data
            if tmp in table.keys():
                tmp_list.append(str(table[tmp]))
                tmp = ''
    
    result = "".join(tmp_list)
    return int(result)