def solution(n, arr1, arr2):
    tmp = []
    for i in range(n):
        t = bin(arr1[i] | arr2[i])[2:].zfill(n)
        tmp.append(t.replace("0b",""))
    
    result = []
    for t in tmp:
        st = ''
        for s in t:
            if s == '1':
                st += '#'
            else:
                st += ' '
        result.append(st)
    
    return result