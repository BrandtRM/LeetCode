class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        elif len(nums) < 2:
            return len(nums)
        elif nums[0] == nums[len(nums) - 1]:
            return 1

        curr = nums[0]
        k = 0
        i = 1
        while i < len(nums):
            print(nums)
            if nums[i] < curr:
                break
            if nums[i] == curr:
                if i == len(nums) - 1:
                    return len(nums) - k - 1
                elif nums[i + 1] < curr:
                    return len(nums) - k - 1
                k += 1
                j = i

                ## swap with next
                while j + 1 < len(nums):
                    if  nums[j] < nums[j + 1]:
                        temp = nums[j + 1]
                        nums[j + 1] = nums[j]
                        nums[j] = temp
                    
                    j += 1 
            else:
                curr = nums[i]
                i += 1
            
        return len(nums) - k
