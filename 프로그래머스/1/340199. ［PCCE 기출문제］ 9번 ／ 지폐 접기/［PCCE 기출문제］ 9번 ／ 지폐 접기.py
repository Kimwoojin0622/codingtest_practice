def solution(wallet, bill):
    answer, is_True = 0, True
    while is_True:
        if max(bill) <= max(wallet) and min(bill) <= min(wallet):
            break
        else:
            idx = bill.index(max(bill))
            bill[idx] = bill[idx] // 2
            answer += 1
    return answer