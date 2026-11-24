from collections import deque
def solution(cards1, cards2, goal):
    # 문자열로 이루어진 배열 cards1, cards2와 원하는 배열 goal이 매개변수로 주어질 때,
    # cards1과 cards2에 적힌 단어들로 goal을 만들 수 있다면 Yes, 없다면 No를 return
    # 단 카드 뭉치의 순서대로 작성이 가능하게끔!
    
    # cards1 - ['i', 'drink', 'water']
    # cards2 - ['want', 'to']
    # goal - ['i', 'want', 'to', 'drink', 'water'] -> Yes
    
    cards1_deque = deque(cards1)
    cards2_deque = deque(cards2)
    goal = deque(goal)
    
    while True:
        if not goal:
            break
            
        tmp = goal.popleft()
        print(goal)
        if len(cards1_deque) != 0 and cards1_deque[0] == tmp:
            cards1_deque.popleft()
        elif len(cards2_deque) != 0 and cards2_deque[0] == tmp:
            cards2_deque.popleft()
        else:
            return 'No'

    return 'Yes'
    
    
    