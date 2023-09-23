class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        l , r = 0, 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                prof = prices[r] - prices[l]
                maxP = max(prof, maxP)
            else:
                l = r
            r += 1

        return maxP


prices = [2,1,2,1,0,1,2]
sol = Solution()

print(sol.maxProfit(prices))