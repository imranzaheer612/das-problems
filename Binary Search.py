class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1

nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2

sol = Solution()
print(sol.search(nums, target))