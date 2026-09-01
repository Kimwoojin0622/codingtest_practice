def solution(elements):
    join = elements + elements
    sums = set()
    
    length = len(elements)
    
    for i in range(length):
        total = 0
        for j in range(i, length + i):
            total += join[j]
            sums.add(total)
    
    return len(sums)