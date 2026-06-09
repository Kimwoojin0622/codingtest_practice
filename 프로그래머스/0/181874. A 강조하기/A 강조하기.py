def solution(myString):
    result = ['A' if s == 'a' or s == 'A' else s.lower() for s in myString]
    return "".join(result)
    
        