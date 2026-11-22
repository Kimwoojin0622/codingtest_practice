from collections import Counter
def solution(participant, completion):
    # participant (마라톤에 참여한 선수들의 이름이 담긴 배열)
    # completion (완주한 선수들의 이름이 담긴 배열)

    # 문제 : 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성
    
    # 1. 참가를 한 선수들을 담기 위한 check 딕셔너리를 생성
    
    # 2. 참가자 리스트인 participant를 for문으로 돌면서 check 딕셔너리안에 참가자 수 만큼 +1을 진행
      # 만약, 홍길동 / 정약용 / 정약용이 참여를 했을 때는 홍길동이라는 키에는 1의 값을 정약용이라는 키에는 2의 값을 부여
    
    # 3. 완주자 리스트인 completion을 for문으로 돌면서 check 딕셔너리안에 있는 참가자 수 만큼 -1을 진행
      # 만약 홍길동이 완주를 했다면 홍길동 1의 값에서 홍길동 0의 값으로 바뀜
    
    # 4. 마지막으로 check의 값을 확인하면서 만약 1의 값을 가진 키가 있다면, 그 키를 return하는 코드를 작성
      # 1의 값을 가진 키는, 완주를 하지 못한 사람임
      # completion의 길이는 participant의 길이보다 1 작기 때문에, 한 명의 완주를 하지 못한 사람이 존재
    
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