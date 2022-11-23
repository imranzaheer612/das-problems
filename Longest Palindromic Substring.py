

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        start = 0
        maxLength = 1

        # possible substrings
        for i in range(n):
            for j in range(i, n):
                flag = True
                
                print()
                print("substring:", s[i:j+1])

                #check substring is palindrome
                print("check palindrome")
                for k in range(0, ((j - i) // 2 ) + 1):
                    print(s[i+k], "-", s[j-k], end="")
                    if (s[i + k] != s[j - k]):
                        print(" = not", end="\n")
                        flag = False;
                        break

                    print(end="\n")
                
                # check longest palindrome
                if (flag and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1
                    print("new pal **", s[start : start + maxLength])

        return s[start : start + maxLength]


my_str = "babad";
# my_str = "cbbd";
sol = Solution()

print(sol.longestPalindrome(my_str))