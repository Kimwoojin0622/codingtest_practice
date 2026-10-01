from collections import Counter
def solution(topping):
    # O(N^2) 불가
    result = 0
    brother = Counter(topping)
    sibling = set()
    
    for t in topping:
        sibling.add(t)
        brother[t] = brother[t] - 1
        if brother[t] == 0:
            del brother[t]
        
        if len(sibling) == len(brother):
            result += 1
    return result