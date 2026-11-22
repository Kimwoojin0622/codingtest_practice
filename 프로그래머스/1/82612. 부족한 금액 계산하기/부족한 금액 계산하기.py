def solution(price, money, count):
    # 1. price의 값을 tmp에 저장
    tmp = price
    
    # 2. count번 탑승했을 때, 실제로 내야할 돈인 pay 변수 저장
    pay = 0
    
    # 3. tmp의 값을 계속 price 값만큼 count번 더해서 실제로 내야할 돈은 pay 변수에 저장
    for _ in range(count):
        pay += tmp
        tmp += price
    
    # 4. 만약 실제로 내야할 돈인 pay의 값이 현재 가지고 있는 money 변수보다 크다면, money - pay의 값을 출력하고,
    # 만약 실제로 내야할 돈인 pay의 값이 현재 가지고 있는 money 변수보다 작다면, money로 낼 수 있으니 0의 값을 출력
    if pay > money:
        return pay - money
    else:
        return 0