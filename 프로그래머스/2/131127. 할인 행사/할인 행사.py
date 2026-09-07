def solution(want, number, discount):
    # 10 * 100,000
    want_number = {}
    for i in range(len(want)):
        want_number[want[i]] = number[i]
    
    loop = len(discount) - 9
    result = 0
    for i in range(loop):
        count = 0
        today_discount = discount[i:i+10]
        for j in range(len(want)):
            if today_discount.count(want[j]) >= want_number[want[j]]:
                count += 1
                continue
        if count == len(want):
            result += 1
    
    return result