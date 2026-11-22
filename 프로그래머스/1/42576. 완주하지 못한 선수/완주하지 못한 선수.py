from collections import Counter
def solution(participant, completion):
    # participant (마라톤에 참여한 선수들의 이름이 담긴 배열)
    # completion (완주한 선수들의 이름이 담긴 배열)

    # 문제 : 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성

    check = {}
    for p in participant:
        if p not in check:
            check[p] = 1
        else:
            check[p] += 1
    
    for c in completion:
        check[c] = check[c] - 1
    
    for person in check.items():
        if person[1] == 1:
            return person[0]