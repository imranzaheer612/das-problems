
class Solution:
    
    #best
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1, len(nums)):
            if (nums[r] != nums[r-1]):
                nums[l] = nums[r]
                l += 1
        
        return l

    # working sol
    def removeDuplicates_1(self, nums) -> int:
        if len(nums)==1:
            return 1
        
        x = nums[0]
        i = 0
        while i < len(nums)-1:
            if x == nums[1+i]:
                del nums[1+i]
            else:
                x = nums[1+i]
                i += 1
        
        return i+1

    # pending
    def removeDuplicates_2(self, nums) -> int:

        if len(nums)==1:
            return 1
        
        k = 0;
        i = 1
        while i < len(nums):
            print(nums)
            if (nums[i - 1] == nums[i]):
                del nums[i]
                k += 1
                i = i - 1 
            i += 1

        return k



test_list = [0,0,1,1,1,2,2,3,3,4]
sol = Solution();
print(sol.removeDuplicates(test_list))