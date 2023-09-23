class Solution:
    def searchInsert(self, nums, target) -> int:
        
        # left, right pointers
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid  = (l + r) // 2
            
            # if target is mid
            if target == nums[mid]:
                return mid
            
            # if target is on left side
            elif target > nums[mid]:
                l = mid + 1
            
            # target on right side
            else:
                r = mid - 1

        return l

# Driver Code
test_list = [1,3,5,6]
sol = Solution();
print(sol.searchInsert(test_list, 7))
print(sol.searchInsert(test_list, 5))