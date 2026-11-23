def solution(s):
    s_list = []
    
    i = 0
    for st in s:
        if st == " ":
            s_list.append(" ")
            i = 0
        elif i % 2 == 0:
            s_list.append(st.upper())
            i += 1
        else:
            s_list.append(st.lower())
            i += 1
    
    return "".join(s_list)