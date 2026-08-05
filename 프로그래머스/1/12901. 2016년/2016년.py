def solution(a, b):
    weekday = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    tmp = 0
    for i in range(a - 1):
        tmp += days[i]
    
    check_weekday = ((tmp + b) % 7) - 1
    return weekday[check_weekday]