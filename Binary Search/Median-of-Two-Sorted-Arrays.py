

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        n = len(nums1)
        m = len(nums2)

        if (n > m):
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = n
        merged_arr_median = (n + m + 1) // 2
        
        while (start <= end):

            mid = (start + end) // 2
            l1_size = mid
            l2_size = merged_arr_median - mid

            # checking overflow of indices
            l1 = nums1[l1_size - 1] if (l1_size > 0) else float('-inf')
            l2 = nums2[l2_size - 1] if (l2_size > 0) else float('-inf')
            r1 = nums1[l1_size] if (l1_size < n) else float('inf')
            r2 = nums2[l2_size] if (l2_size < m) else float('inf')

            # if correct partition is done
            if l1 <= r2 and l2 <= r1:
                if ((m + n) % 2 == 0):
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                return max(l1, l2)

            elif (l1 > r2):
                end = mid - 1
            else:
                start = mid + 1


arr1 = [1, 2]
arr2 = [3, 4]


sol = Solution()

print(sol.findMedianSortedArrays(arr1, arr2))