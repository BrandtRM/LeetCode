class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x)
        left = 0
        right = len(pal) - 1

        while left <= right:
            if left == right:
                return True
            
            if pal[left] != pal[right]:
                return False

            left += 1
            right -= 1
