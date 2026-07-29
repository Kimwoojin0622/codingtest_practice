from collections import deque
def solution(cards1, cards2, goal): 
    cards1 = deque(cards1 + ['99'])
    cards2 = deque(cards2 + ['99'])
    
    for data in goal:
        if data == cards1[0]:
            cards1.popleft()
        elif data == cards2[0]:
            cards2.popleft()
        elif data != cards1[0] or data != cards2[0]:
            return "No"
    return "Yes"