def solution(elements):
    double = elements + elements
    length = len(elements)
    tmp = set()
    
    for i in range(length):
        total = 0
        for j in range(i, length+i):
            total += double[j]
            tmp.add(total)
    
    return len(tmp)