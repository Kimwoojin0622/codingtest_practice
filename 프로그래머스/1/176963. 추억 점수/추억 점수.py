
def solution(name, yearning, photo):
    # 추억 점수
    
    # name - 그리워하는 사람의 이름을 담은 문자열 배열
      # ["may", "kein", "kain", "radi"]
    # yearning - 각 사람별 그리움 점수를 담은 정수 배열
      # [5, 10, 1, 3]
    # photo - 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열
     # [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
        
    # 문제 : 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성
    
    result = []
    name_score = {}
    for i in range(len(name)):
        name_score[name[i]] = yearning[i]
    
    for p in photo:
        tmp = 0
        for person in p:
            if person in name_score.keys():
                tmp += name_score[person]
            else:
                continue
        result.append(tmp)
    
    return result