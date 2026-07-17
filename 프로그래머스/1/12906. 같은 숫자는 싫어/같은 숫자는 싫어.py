# 스택/큐
def solution(arr):
    # 첫 시작은 arr[0]번째 값 부터!
    stack, top = [arr[0]], 0
    
    # arr의 1번째 인덱스부터 for문을 도는데,
    for i in range(1, len(arr)):
        # 만약 arr[i] 번째와 stack의 상위(top)값과 일치하지 않다면 그 값을 stack에 append
        # 그리고 top도 증가
        if arr[i] != stack[top]:
            stack.append(arr[i])
            top += 1
            
    return stack