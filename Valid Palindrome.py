class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = []
        for c in s:
            if c.isalnum():
                res.append(c)
        
        tmp = ''.join(res).lower()
        return tmp == tmp[::-1]
    

    def withPointers(self, s: str) -> bool:
        
        s = [c.lower() for c in s if c.isalnum()]

        n =  len(s)
        
        if n == 0:
            return False
    
        i = 0
        j = n - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
    
    """
    With out creating extra arr
    Inc/Dic while an alpanum is found
    then check palindrome
    """
    def withOutArr(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# s = "race a car"
s = "A man, a plan, a canal: Panama"
sol = Solution()

print(sol.withOutArr(s))