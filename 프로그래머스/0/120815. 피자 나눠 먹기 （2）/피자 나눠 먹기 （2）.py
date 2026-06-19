def solution(n):
    pizza = 6
    while True:
        if pizza >= n:
            if pizza % n == 0:
                return pizza // 6
        pizza = pizza + 6
