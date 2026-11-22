def solution(s):
    upper_list = []
    lower_list = []
    for st in s:
        if st == st.upper():
            upper_list.append(st)
        else:
            lower_list.append(st)
    
    up = sorted(upper_list, reverse=True)
    lo = sorted(lower_list, reverse=True)
    
    return "".join(lo) + "".join(up)