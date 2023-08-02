class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # make prefix and suffix array
        n = len(nums)
        pref = [0 for i in range(n)]
        suf = [0 for i in range(n)]
        res = [0 for i in range(n)]
        
        # calculate prefiix and store in prffix arr
        pref[0] = 1
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        # calculate suffix and store in suffix arr
        suf[n - 1] = 1
        for i in range(n - 2 , -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        # multiply prefix and suffix & store in res arr
        for i in range(n):
            res[i] = pref[i] * suf[i]  

        return res


nums = [1,2,3,4]

sol = Solution()
print(sol.productExceptSelf(nums))