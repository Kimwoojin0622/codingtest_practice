def solution(number):
    result = 0
    for n in number:
        result = result + int(n)
    
    return result % 9