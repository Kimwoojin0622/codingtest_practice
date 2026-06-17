def solution(picture, k):
    result = []
    for data in picture:
        # print(data)
        temp = ''
        # picture의 0번 인덱스부터 문자열 원소를 하나하나씩 꺼낸뒤, k만큼 곱한다.
        # ex) .xx...xx.에서 . 을 꺼낸 뒤 2만큼 곱하면 .. 이 된다. 이걸 temp에 +=
        for element in data:
            temp = temp + (element * k)
        
        # k의 개수만큼 늘린 picture를 k만큼 result에 추가해야한다.
        for _ in range(k):
            result.append(temp)
    
    return result