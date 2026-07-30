def solution(n, arr1, arr2):
    tmp = [] # | 연산 담기
    for i in range(n):
        t = bin(arr1[i] | arr2[i])
        if len(t) == n+2:
            tmp.append(t.replace("0b", ""))
        else:
            diff = (n + 2) - len(t)
            tmp.append(t.replace("0b", "0" * diff))
    
    result = []
    for data in tmp:
        shap = ''
        for s in data:
            if s == "1":
                shap += "#"
            else:
                shap += " "
        result.append(shap)
    
    return result