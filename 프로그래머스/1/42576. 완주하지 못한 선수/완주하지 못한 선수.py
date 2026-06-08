from collections import Counter

def solution(participant, completion):
    # N이 100,000이기 때문에, N^2는 시간이 초과될 수 있다.
    # step 1. participant의 각 value에 +1씩 -> O(N)
    chk = Counter(participant)
    
    # step 2. completion을 돌면서 value를 -1씩하고, -> O(N-1)
    for s in completion:
        chk[s] = chk[s] - 1
        
    # step 3. 만약, value가 1과 같다면 key값을 return -> O(N) (이건 최악의 경우)
    for s in chk:
        if chk[s] == 1:
            return s
    # 끝