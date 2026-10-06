def solution(dartResult):
    SDT = {'S':1,'D':2,'T':3}
    
    num = '' # 10점을 위해
    score = []
    for dart in dartResult:
        if dart.isdigit():
            num += dart
        else:
            if dart == '*':
                if len(score) < 2:
                    score[-1] *= 2
                else:
                    score[-1] *= 2
                    score[-2] *= 2
            elif dart == '#':
                score[-1] *= -1
            else:
                score.append(int(num) ** SDT[dart])
            num = ''
            
    return sum(score)