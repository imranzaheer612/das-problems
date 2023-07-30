class Solution:

    """
    Time : O(n^2)
    Space : O(1)
    """
    def withBruteForce(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        nums.sort()
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                print(i, j)
                if nums[j] > target:
                    break
                
                if nums[i] + nums[j] == target:
                    return [i, j]


    """
    Time : O(n)
    Space : O(n)
    """
    def withHashMap(self, nums: list[int], target: int) -> list[int]:

        hash = {}

        for i in range(len(nums)):
            j = target - nums[i]
            if j in hash:
                return [hash[j], i]
            
            hash[nums[i]] = i
    

nums = [3,2,4]
t = 6
sol = Solution()

print(sol.withHashMap(nums, t))