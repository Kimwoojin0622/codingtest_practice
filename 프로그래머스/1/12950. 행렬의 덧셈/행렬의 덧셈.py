def solution(arr1, arr2):
    # 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과

    # 1. arr1의 첫 번째 리스트의 길이를 length 변수에 저장
    
    # 2. arr1의 전체 길이를 batch 변수에 저장
    
    # 3. 최종 리스트를 담을 result 리스트 생성
    
    # 4. batch 변수를 통해 arr1과 arr2의 전체 개수만큼 도는 for문을 작성하고, tmp의 이름을 가진 리스트 변수 생성
    
    # 5. 전체 개수만큼 도는 동안, 중첩 for 문을 활용해서 arr1과 arr2의 각 원소들의 합을 구합니다.
    
    # 6. i와 j를 활용해서 0행 0열, 0행 1열, 1행 0열, 1행 1열의 값들을 서로 구합니다. 그리고 그 값들을 tmp 변수에 append를 진행합니다.
      # arr1[i][j] + arr2[i][j]의 형식으로 행렬의 덧셈을 구합니다.
    
    # 7. batch가 한 번 끝날때마다 tmp에 저장된 리스트 값을 result 리스트에 append 합니다.
    
    # 8. 최종적으로는 result에 arr1과 arr2를 더한 행렬 형식의 값이 저장되므로, 해당 값을 return 합니다.
    
    result = []
    
    length = len(arr1[0])
    batch = len(arr1)
    
    for i in range(batch):
        tmp = []
        for j in range(length):
            tmp.append(arr1[i][j] + arr2[i][j])
        result.append(tmp)
    
    return result