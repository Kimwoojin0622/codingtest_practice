def solution(s):
    length = len(s)
    if length == 4 or length == 6:
        for st in s:
            if not st.isdigit():
                return False
    else:
        return False
    
    return True