def solution(dots):
    # 넓이 = 가로 * 세로
    dots.sort()
    width = abs(dots[0][0] - dots[2][0])
    height = abs(dots[0][1] - dots[1][1])
    
    result = width * height
    
    return result