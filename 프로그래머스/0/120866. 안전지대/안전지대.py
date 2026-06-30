def solution(board):
    # N의 최대값이 100이므로 O(N^2) 가능
    # 위 아래 좌 우 대각선 칸을 모두 위험지역으로 분류
    # 지뢰가 매설 -> 1 / 지뢰가 없는 지역 -> 0
    land_location = set()
    
    # n * n
    length = len(board)
    total_length = length * length
    
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(length):
        for y in range(length):
            if board[x][y] == 1:
                land_location.add((x, y))
                
                # dx와 dy를 돌면서 상 하 좌 우 대각선 부분 채우기
                for i in range(len(dx)):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if (nx < length and nx >= 0) and (ny < length and ny >= 0):
                        if (nx, ny) not in land_location:
                            land_location.add((nx, ny))
                    
                    # 대각선 부분
                    if i == 0 or i == 1:
                        if nx < length and nx >= 0:
                            left_ny, right_ny = ny - 1, ny + 1
                            if left_ny < length and left_ny >= 0:
                                if (nx, left_ny) not in land_location:
                                    land_location.add((nx, left_ny))
                            if right_ny < length and right_ny >= 0:
                                if (nx, right_ny) not in land_location:
                                    land_location.add((nx, right_ny))
                                    
    # 전체 n * n 길이에서 위험지역 차감
    return total_length - len(land_location)
                        
                    
                
    
