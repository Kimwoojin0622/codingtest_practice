def solution(phone_number):
    result = ''
    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            result += '*'
        else:
            result += phone_number[i]
    
    return result