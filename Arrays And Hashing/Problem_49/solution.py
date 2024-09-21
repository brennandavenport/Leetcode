class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = dict()

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)

            if key not in res:
                res[key] = [s]
            else:
                res[key] += [s]

        return res.values()
    
s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

print(ord("a"))