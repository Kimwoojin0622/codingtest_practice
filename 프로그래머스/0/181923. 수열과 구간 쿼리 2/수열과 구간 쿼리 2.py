def solution(arr, queries):
    # [s, e, k] 꼴인데, s <= i <= e인 모든 i에 대해서 k보다 크면서 가장 작은 arr[i]를 찾는다.
    # 0 <= i <= 4 0 1 2 3 4 인데, 2보다 크면서 가장 작은건 3
    # 0 <= i <= 3 0 1 2 3 인데, 2보다 크면서 가장 작은건
    result = []
    # step 1. queries에서 하나씩 꺼내와서 data에 저장
    for data in queries: # N 1000
        # step 2. s부터 e까지 범위를 지정해서 새로운 리스트 li로 저장
        s, e, k = data[0], data[1], data[2]
        li = arr[s : e + 1]
        # print(li)
         # step 3. li에서 하나씩 꺼내오면서 k보다 큰 숫자를 min_value[]에 저장하고, min으로 최소값 구하기
        value = []
        for n in li:
            if n > k:
                value.append(n)

        if value:
            min_value = min(value)
        # step 4. 만약 더 작은 값이 없다면 -1
        else:
            min_value = -1
        
        result.append(min_value)
    
    return result
            
   