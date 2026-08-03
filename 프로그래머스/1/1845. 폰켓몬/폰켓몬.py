def solution(nums):
    # 중복 제거
    set_nums = set(nums)
    # N / 2 마리
    inmypocket = len(nums) // 2
    
    # step 1. 만약 set_nums의 길이가 len(nums) // 2보다 작거나 같다면 set_nums의 길이를 출력
    if len(set_nums) <= inmypocket:
        return len(set_nums)
    # step 2. 아니면 inmypocket 출력
    else:
        return inmypocket