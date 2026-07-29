def solution(cards1, cards2, goal): 
    cards1 = cards1 + ['99']
    cards2 = cards2 + ['99']
    
    i, j = 0, 0
    for data in goal:
        if data == cards1[i]:
            t = cards1[i]
            i += 1
        elif data == cards2[j]:
            t = cards2[j]
            j += 1
        elif data != cards1[i] or data != cards2[j]:
            return "No"
    return "Yes"
                