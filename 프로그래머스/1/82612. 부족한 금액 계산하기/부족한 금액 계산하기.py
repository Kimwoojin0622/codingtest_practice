def solution(price, money, count):
    # step 1. price와 count를 활용하여 총 얼마가 필요한지 total로 구한 다음
    total = 0
    for i in range(price, price * count + 1, price):
        total += i
        
    # step 2. total - money를 진행한다.
    tmp = total - money
    
    # step 3. 만약 total - money 가 0보다 작거나 같다면 0을 return 하고,
    if tmp <= 0:
        return 0
    else:
        # 아니면 그 값을 return 한다.
        return tmp
   