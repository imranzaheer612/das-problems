from collections import Counter

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        for char in t:
            if char not in s:
                return False
            s = s.replace(char, '', 1)
                
        return True
    
    """
    Time : O(2n)
    Space : O(n)
    """
    def withHashMap(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countS[t[i]] = countS.get(t[i], 0) - 1

        for key in countS:
            if countS[key] != 0:
                return False

        return True

    """
    Time : O(2n)
    Space : O(n)
    """
    def withCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    """
    Time : O(nlogn)
    Space : O(1)
    """
    def withSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
# s = "aacc"
# t = "ccac"
sol = Solution()

print(sol.withSort(s, t))