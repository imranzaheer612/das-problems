from collections import defaultdict
class Solution:
    def withSort(self, strs: list[str]) -> list[list[str]]:
        
        map = defaultdict(list)

        for words in strs:
            sortedWord = ''.join(sorted(words))
            map[sortedWord].append(words)
                
        return list(map.values())


    def withCount(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())



strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()

print(sol.withCount(strs))