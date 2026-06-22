def solution(emergency):
    sorted_emergency = sorted(emergency)
    priority = len(sorted_emergency)
    
    result = [0] * priority
    for n in sorted_emergency:
        idx = emergency.index(n)
        result[idx] = priority
        priority = priority - 1

    return result