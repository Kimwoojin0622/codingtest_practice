def solution(array, commands):
    # K번째 수
    
    # array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려고 합니다.
    
    # ex: array -> [1, 5, 2, 6, 3, 7, 4]
    # ex: command -> [2, 5, 3], [4, 4, 1] - i, j, k 순!
    
    # 1. commands를 for문을 돌면서 i, j, k의 값들을 구합니다.
    
    # 2. i가 인덱스보다 +1 많으니, -1을 통해 인덱스와 동일하게 맞춘 뒤, array 배열에서 i-1번째부터 j번째 까지 슬라이싱을 통해 tmp 변수에 저장합니다.
    
    # 3. tmp의 값을 정렬을 진행합니다.
    
    # 4. tmp 리스트에서 k번째 숫자를 구한 뒤, 그 값을 result 리스트에 append 합니다.
      # k도 인덱스와 일치한 값이 아니기 때문에, k-1을 통해 인덱스와 일치시킵니다.
    
    result = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        tmp = sorted(array[i-1:j]) # O(N log N)
        result.append(tmp[k-1])
    
    return result
        
        
    