def solution(s):
    # O(N^2) 가능
    result = []
    num = 0
    for st in s:
        if st == " ":
            num = 0
            result.append(st)
            continue
        
        if st.isdigit():
            num += 1
            result.append(st)
            continue
        elif num == 0:
            st = st.upper()
            result.append(st)
            num += 1
        else:
            st = st.lower()
            result.append(st)
            num += 1
    
    answer = "".join(result)
    return answer