def solution(food):
    # food[0]은 물, 1칼로리 3개, 2칼로리 4개, 3칼로리 6개
    eating = []
    for i in range(1, len(food)):
        tmp = food[i] // 2
        for j in range(tmp):
            eating.append(str(i))
    answer = "".join(eating)
    
    return answer + "0" + answer[::-1]