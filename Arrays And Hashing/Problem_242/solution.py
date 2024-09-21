class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap_s = dict()
        hashmap_t = dict()

        for i in range(len(s)):
            hashmap_s[s[i]] = s.count(s[i])
            hashmap_t[t[i]] = t.count(t[i])
        
        for char in hashmap_s:
            if hashmap_s[char] != hashmap_t.get(char, 0):
                return False
        return True
    

s = Solution()

print(s.isAnagram("anagram", "nnagram"))
        