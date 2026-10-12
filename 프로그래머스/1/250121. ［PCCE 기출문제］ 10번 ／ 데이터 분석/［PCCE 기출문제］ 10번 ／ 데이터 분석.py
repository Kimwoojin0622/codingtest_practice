from datetime import datetime
def solution(data, ext, val_ext, sort_by):
    # ext와 sort_by의 값은 다음 중 한 가지를 가집니다
    # code, date, maximum, remain
    elements = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3,
    }
    
    tmp = []
    
    i = 0
    for d in data:
        if ext == 'date':
            int_to_date = datetime.strptime(str(d[elements[ext]]), '%Y%m%d')
            if int_to_date < datetime.strptime(str(val_ext), '%Y%m%d'):
                tmp.append(data[i])
        else:
            if d[elements[ext]] < val_ext:
                tmp.append(data[i])
        i += 1
    
    point = elements[sort_by]
    result = sorted(tmp, key = lambda x:x[point])        
        
    return result