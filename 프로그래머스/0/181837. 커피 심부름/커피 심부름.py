def solution(order):
    # anything은 차가운 아메리카노로
    result = []
    for coffee in order:
        if 'latte' in coffee:
            result.append(5000)
        elif 'americano' in coffee:
            result.append(4500)
        else:
            result.append(4500)
    
    return sum(result)