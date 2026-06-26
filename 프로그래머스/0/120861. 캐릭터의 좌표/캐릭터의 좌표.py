def solution(keyinput, board):
    # board의 크기를 벗어난 방향기 입력은 무시
    # x, y 좌표의 최대값
    x, y = board[0] // 2, board[1] // 2
    
    # 캐릭터 위치
    location = [0, 0]
    
    for data in keyinput:
        if data == 'left' and location[0] > -x:
            location[0] = location[0] - 1
        elif data == 'right' and location[0] < x:
            location[0] = location[0] + 1
        elif data == 'up' and location[1] < y:
            location[1] = location[1] + 1
        elif data == 'down' and location[1] > -y:
            location[1] = location[1] - 1
        
    return location
