def solution(l, r):
    result = []
    # step 1. l부터 r까지 for문을 돌린다.
    for num in range(l, r + 1): # O(N) N은 최대 1,000,000
        # step 2. set을 통해 중복을 제거하기 위해 int형 num을 str로 변환한다.
        # ex ) 55 -> ['5'] / 5005 -> ['5', '0']
        int_to_word = str(num)
        int_to_word = list(set(int_to_word))
        # step 3. int_to_word를 인덱스로 쉽게 접근하기 위해 정렬을 한다. (reverse=True 굳이 안해도 됨)
        # O(N log N), N이 1,000,000 이라 괜찮을 것 같다.
        int_to_word.sort(reverse=True)
        
        # step 4. 만약 중복을 제거한 리스트의 길이가 1이라면, ['5']에 속한 num을 result에 집어넣어준다.
        # ex) 5555 중복제거 -> ['5'] / 55 중복제거 -> ['5']
        if len(int_to_word) == 1:
            if int_to_word[0] == '5':
                result.append(num)
        # step 5. 만약 중복을 제거한 리스트의 길이가 2이상이면, int_to_word의 [0]번째 인덱스는 '5', [1]번째 인덱스는 '0'이어야 한다.
        # ex) 5050 중복제거 -> ['5','0'] / 50005 중복제거 -> ['5', '0']
        # 위에서 sort(reverse=True)를 했기 때문에,  int_to_word[0]이 '5'이다
        else:
            if int_to_word[0] == '5' and int_to_word[1] == '0':
                result.append(num)
    
    # step 6. 위에 과정을 거쳤는데도 result에 담긴게 없다면, [-1]을 return 해주도록 한다.
    if result:
        return result
    else:
        return [-1]
