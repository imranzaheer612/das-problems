class Solution:
    def searchInsert(self, nums, target):
        
        for i in range(len(nums)):
            if (nums[i] >= target):
                return i;
        return i + 1

# Driver Code
test_list = [1,3,5,6]
sol = Solution();
print(sol.searchInsert(test_list, 7))