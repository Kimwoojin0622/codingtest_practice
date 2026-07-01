def solution(id_pw, db):
    id_list = [data[0] for data in db]
    pw_list = [data[1] for data in db]
    
    if id_pw[0] not in id_list:
        return 'fail'
    elif id_pw[0] in id_list and id_pw[1] not in pw_list:
        return "wrong pw"
    else:
        idx = id_list.index(id_pw[0])
        if pw_list[idx] == id_pw[1]:
            return 'login'
        else:
            return 'wrong pw'
            
            
            
