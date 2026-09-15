def solution(citations):
    citations = sorted(citations)
    
    length = len(citations)
    print(citations, length)
    
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
        
    return 0