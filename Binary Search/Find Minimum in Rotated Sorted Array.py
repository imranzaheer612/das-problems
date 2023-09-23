class Solution:

    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while(l <= r):
            print(l, r)

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        


nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
sol = Solution()

print(sol.findMin(nums))