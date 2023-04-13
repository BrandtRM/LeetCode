class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        sol = 0

        if end == 0:
            if nums[start] == val:
                return 0
            else:
                return 1
        
        while start < end:
            if nums[start] == val:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                end -= 1
            else:
                start += 1
                sol += 1

            if start == end and nums[start] != val:
                sol += 1
        
        return sol

