def solution(babbling):
    # O(N^2) 가능
    able_to_speak = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for bab in babbling:
        tmp = ''
        tmp_list = []
        for i in range(len(bab)):
            tmp += bab[i]
            if tmp in able_to_speak:
                if not tmp_list:
                    tmp_list.append(tmp)
                    tmp = ''
                else:
                    if tmp_list[-1] == tmp:
                        tmp_list.pop()
                        tmp = ''
                    else:
                        tmp_list.append(tmp)
                        tmp = ''
        
        st = "".join(tmp_list)
        if len(st) == len(bab):
            result += 1
            
    return result