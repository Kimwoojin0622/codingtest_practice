def solution(box, n):
    # 높이의 몫 * 가로의 몫 * 세로의 몫
    result = 1
    for data in box:
        temp = data // n
        result = result * temp
    
    return result