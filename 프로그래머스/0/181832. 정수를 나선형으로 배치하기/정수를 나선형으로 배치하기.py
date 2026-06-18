def solution(n):
    result = [[0] * n for _ in range(n)]
    temp = set()
    
    # 움직이는 방향
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 움직일 x, y 변수와 result[x][y]에 들어갈 값 num 선언
    x, y, num = 0, 0, 1
    # 움직일 방향 di 선언
    di = 0
    
    while num <= (n ** 2):
        result[x][y] = num
        temp.add((x,y))
        
        nx = x + dx[di]
        ny = y + dy[di]
        
        if nx < 0 or nx > (n - 1) or ny < 0 or ny > (n - 1) or (nx, ny) in temp:
            di = (di + 1) % 4
            nx = x + dx[di]
            ny = y + dy[di]
        
        x, y = nx, ny
        num += 1
    
    return result