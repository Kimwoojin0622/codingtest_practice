def solution(quiz):
    result = []
    for data in quiz:
        temp = data.split(" ")
        # temp[0] 와 temp[2]를 temp[1] == +,-로 계산했을 시, temp[4]이 나온다면, treu
        if temp[1] == '-':
            if int(temp[0]) - int(temp[2]) == int(temp[4]):
                result.append('O')
            else:
                result.append('X')
        elif temp[1] == '+':
            if int(temp[0]) + int(temp[2]) == int(temp[4]):
                result.append('O')
            else:
                result.append('X')
    return result