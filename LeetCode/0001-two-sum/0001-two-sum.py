class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N^2)
        output = [0, 0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    output[0] = i
                    output[1] = j
                    return output