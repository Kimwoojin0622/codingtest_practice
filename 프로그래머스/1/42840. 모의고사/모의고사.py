def solution(answers):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    correct = [0, 0, 0]
    
    for i in range(len(patterns)):
        chk = 0
        for j in range(len(answers)):
            if chk == len(patterns[i]):
                chk = 0
            if patterns[i][chk] == answers[j]:
                correct[i] += 1
            chk += 1
    
    result = []
    mc = max(correct)
    for i in range(len(correct)):
        if correct[i] == mc:
            result.append(i+1)
    
    return result