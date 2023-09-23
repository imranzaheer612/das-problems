
class Solution:
    
    #If a num is unique replace it, next to the last unique num seen
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1, len(nums)):
            if (nums[r] != nums[r-1]):
                nums[l] = nums[r]
                l += 1
        
        return l


# Driver Code
test_list = [0,0,1,1,1,2,2,3,3,4]
sol = Solution();
print(sol.removeDuplicates(test_list))