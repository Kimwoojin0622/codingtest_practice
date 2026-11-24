
def solution(name, yearning, photo):
    # 추억 점수
    
    # name - 그리워하는 사람의 이름을 담은 문자열 배열
      # ["may", "kein", "kain", "radi"]
    # yearning - 각 사람별 그리움 점수를 담은 정수 배열
      # [5, 10, 1, 3]
    # photo - 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열
     # [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
        
    # 문제 : 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성
    
    # 1. 최종 값을 담을 result 리스트 선언
    
    # 2. name과 추억점수 yearning을 담기 위한 딕셔너리 name_score 선언
    
    # 3. name의 길이만큼 for문을 돌려서 name : yearning 형식의 키 값을 가진 딕셔너리 생성
    # ex) 김철수 : 15
    
    # 4. 2차원 배열 photo를 for문을 활용해서 각각의 1차원 배열들을 p로 들고옴
    # 그리고 각 배열의 추억 점수를 담기 위한 tmp 변수 선언
    
    # 5. 이후 1차원 배열을 또 for문을 돌면서 photo에 담긴 각 이름들을 person으로 들고옴
    
    # 6. 만약, 이름 person이 name_score key값에 존재한다면 tmp에 값에 name_score에 있는 person의 값을 더합니다.
    
    # 7. 만약, 이름이 name_score안에 없다면 continue
    
    # 8. 각 1차원 배열 당 추억 점수 합계인 tmp를 구했고, 이를 result에 append
    
    # 9. 마지막으로 각 배열 당 추억 점수 합계가 담긴 result를 return
    
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