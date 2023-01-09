class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l_par = "({["
        r_par = ")}]"

        for char in s:

            if char in l_par:
                stack.append(char)

            elif char in r_par and stack:
                pos = r_par.index(char)
                cur_par = stack[-1]
                if (l_par[pos] == cur_par):
                    stack.pop()
                    continue; 
                else:
                    return False;

            else:
                return False;

        return len(stack)==0;







test_string = "([])"
sol = Solution();
print(sol.isValid(test_string))