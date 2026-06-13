## ★★★
def solution(arr):
    cnt = 0
    
    while True:
        is_Changed = False
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                is_Changed = True
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
                is_Changed = True
        
        if is_Changed == False:
            return cnt
        cnt += 1
        
        
