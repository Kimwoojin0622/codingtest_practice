from collections import Counter
def solution(want, number, discount):
    # 10 * 100,000
    want_number = {}
    for i in range(len(want)):
        want_number[want[i]] = number[i]
    
    result = 0
    for i in range(len(discount) - 9):
        chk = Counter(discount[i:i+10])
        if chk == want_number:
            result += 1
    
    return result