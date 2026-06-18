def solution(n):
    # 0이 담긴 n x n 배열 생성
    result = [[0] * n for _ in range(n)]
    
    # 들렸던 곳인지 체크할 temp 생성
    temp = set()
    
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 움직일 말 위치 x, y 선언
    x, y = 0, 0
    
    # 우 하 좌 상 방향을 선택할 di 선언
    di = 0
    
    # element = 1 부터 시작해 n ** 2까지 값을 계속 집어넣는다.
    element = 1
    
    # element가 n ** 2 이전까지 실행, 왜냐하면 n ** 2까지의 숫자를 담아야함
    while element <= (n ** 2):
        result[x][y] = element
        temp.add((x,y))
        
        # 다음 위치 계산
        # ex) 원래 0,0 이면 -> 0,1로 변함
        nx = x + dx[di]
        ny = y + dy[di]
        
        # 다음 위치가 해당 n x n 배열을 넘어가거나, 이미 들렸던 곳이면 방향을 바꿔야함
        if nx < 0 or nx > (n-1) or ny < 0 or ny > (n-1) or (nx, ny) in temp:
            # 우 하 좌 상 방향으로 만들어진 dx, dy를 계속 돌아야함
            di = (di + 1) % 4
            nx = x + dx[di]
            ny = y + dy[di]
        
        x, y = nx, ny
        element += 1

    return result