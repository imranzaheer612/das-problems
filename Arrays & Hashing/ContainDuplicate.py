class Solution:

    """
    Time : O(n)
    """
    def withbruteForce(self, nums: list[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print((i, j), end="")
                
                if nums[i] == nums[j]:
                    return True
                
            print("\n")

        return False
        
    """
    Time : O(n)
    """
    def withSort(self, nums: list[int]) -> bool:
        
        nums.sort()
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False
    
    """
    Time : O(n)
    Space : O(n)
    """
    def withHashSet (self, nums: list[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
             
            hashset.add(n)

        return False


# nums = [1, 2, 3, 4]
nums = [1, 2, 3, 4, 1]
sol = Solution()

print(sol.withbruteForce(nums))
print(sol.withHashSet(nums))