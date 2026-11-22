def solution(phone_number):
    length = len(phone_number)
    
    result = ''
    for i in range(0, length-4):
        result += '*'
    
    return result + phone_number[length-4:]