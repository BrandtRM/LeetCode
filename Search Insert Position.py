class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while end > start:
            mid = floor((end + start) / 2)
            print(f"{start} {mid} {end}")
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if start == end and nums[start] < target:
            return start + 1

        return start
