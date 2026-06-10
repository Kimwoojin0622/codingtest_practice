def solution(arr):
    i = 0
    stk = []
    # step 1. 초기값 i가 arr의 길이보다 작을때까지 실행
    # O(N) 최대 100,000
    while (i < len(arr)):
        # step 2. stk가 빈 배열이라면 arr[i]번째를 stk에 추가하고 i + 1
        if len(stk) == 0:
            stk.append(arr[i])
            i = i + 1
        # step 3. stk가 빈 배열이 아니고,
        # step 3-1. 그 중에서 stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더한다.
        elif len(stk) >= 1:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i = i + 1
                # step 3-2. stk의 마지막 원소가 arr[i]보다 크거나 같다면 stk의 마지막 원소를 stk에서 제거한다.
            else:
                stk.pop()
    return stk
            
            