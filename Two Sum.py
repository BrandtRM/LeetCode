class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = [0,0]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sol[0] = i
                    sol[1] = j
                    return sol
