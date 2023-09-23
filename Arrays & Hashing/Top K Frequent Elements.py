from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def withOutHeap(self, nums: list[int], k: int) -> list[int]:
        
        map = defaultdict(int)

        for n in nums:
            map[n] = map[n] + 1

        max_nums = []
        for i in range(k):
            m = max(map, key=map.get)
            max_nums.append(m)
            map[m] = -1
            
        return max_nums
   
    """
    Time : O(nlogn)
    Space : O(n)
    """
    def withHeap(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)
        res = []

        for n in nums:
            map[n] = map[n] + 1

        for val, count in map.items():
            if len(res) < k:
                heappush(res,(count,val))
            else:
                heappush(res,(count,val))
                heappop(res)

        return [val for count, val in res]
    
    """
    Time : O(n)
    Space : O(n)
    """
    def withBucketSort(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)
        freq = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            map[n] = map[n] + 1

        for v, c in map.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)

            if len(res) == k:
                return res



nums = [1,1,1,2,2,3]
k = 2
# nums = [1]
# k = 1

sol = Solution()
print(sol.withBucketSort(nums, k))