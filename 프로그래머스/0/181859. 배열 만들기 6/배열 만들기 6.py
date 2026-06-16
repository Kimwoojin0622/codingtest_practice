def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if arr[i] == stk[-1]:
                stk.pop()
            elif arr[i] != stk[-1]:
                stk.append(arr[i])
    
    if stk:
        return stk
    else:
        return [-1]
    