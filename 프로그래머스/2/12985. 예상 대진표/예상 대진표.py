def solution(N,A,B):
    # 홀수는 +1
    location = [A,B]
    count = 1
    while True:
        for i in range(2):
            if location[i] % 2 == 0:
                location[i] = location[i] // 2
            else:
                location[i] = location[i] // 2 + 1
        if location[0] == location[1]:
            return count
        else:
            count += 1