class Solution:

    """
    Complexity : O(n^2)
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # Brute force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print((i, j), end="")
                
                if nums[i] == nums[j]:
                    return True
                
            print("\n")

        return False
        
    """
    Complexity : O(n log n)
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        nums.sort()
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False


nums = [1,2,3,4]
sol = Solution()

print(sol.containsDuplicate(nums))