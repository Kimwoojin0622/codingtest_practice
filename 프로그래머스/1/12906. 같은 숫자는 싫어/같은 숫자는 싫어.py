def solution(arr):
    # 같은 숫자는 싫어
    
    # 배열 arr -> [1, 1, 3, 3, 0, 1, 1] -> [1, 3, 0, 1]
    
    # 문제 : 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
    
    # 1. arr의 첫 번째 원소 값을 삽입
    
    # 2. arr의 길이를 구하고, for문을 통해서 첫 번째 원소 값을 삽입을 한 상태이니, 1부터 length까지 도는 for문을 작성
    
    # 3. 이 때, arr의 i번째 값이 현재 answer 리스트에 있는 마지막의 값과 같다면 continue를 하고
    
    # 4. 만약 answer 리스트에 있는 마지막의 값인 answer[-1]의 값과 다르다면 answer에 arr의 i번째 값을 append
    
    # 5. 최종 만들어진 answer 값을 return
    
    answer = [arr[0]]
    
    length = len(arr)
    for i in range(1, length):
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
        
    return answer