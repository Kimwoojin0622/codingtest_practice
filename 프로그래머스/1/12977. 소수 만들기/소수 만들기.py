def solution(nums):
    # O(N^3)
    # 50^3 = 125000
    combi = []
    for i in range(len(nums) - 2): # 0 1 2
        for j in range(i + 1, len(nums) - 1):
            for h in range(j + 1, len(nums)):
                combi.append(nums[i] + nums[j] + nums[h])

    num = 0
    # O(N^2)
    # 10^2 = 1000000
    for data in combi:
        check = 0
        for i in range(2, data):
            if data % i == 0:
                check += 1
                break
        if check == 0:
            num += 1
    
    return num