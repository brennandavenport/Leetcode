"""
Assume u r given a str and u wnat to shrink it

aabbccd -> a2b2c2d
bc
aa -> a2 and so on

if num of chars is 1 just put the char


aaaaba

a4ba

they need to be continous

s is only lowercase english letters



"""


class Solution:
    def shrink(self, s) -> str:

        hashMap = {}

        res = []

        l = 0

        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] += 1

            if s[l] != s[i]:
                if hashMap[s[l]] > 1:
                    
                    res.append(str(hashMap[s[l]]))
                del hashMap[s[l]]

                l = i
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
                res.append(s[i])

        for values in hashMap.values():
            if values > 1:
                res.append(str(values))

        return "".join(res)



        # s = list(s)
        # out = ''
        # i = 0
        # j = i + 1
        # while i < len(s) and j < len(s):
        #     alpha = {'a':0,
        #          'b':0,
        #          'c':0}
            
        #     if ord(s[i]) == ord(s[j]):
        #         if alpha.get(s[i]) == 0:
        #             out += s[i]
        #         alpha[s[i]] = alpha.get(s[i]) + 1
        #         j += 1
        #     else:
        #         out += s[i]
        #         if alpha.get(s[i]):
        #             out += str(alpha.get(s[i]))
        #         i += 1
        #         j += 1
        # return out



        # Richard Solution
        # currLetter = ""
        # freq = 0
        # res = ""
        # for i, a in enumerate(s):
        #     if currLetter == "":
        #         currLetter = s[i]
        #         freq += 1
        #     elif currLetter != "":
        #         if s[currLetter - 1] == s[currLetter]:
        #             freq += 1
        #     if currLetter != currLetter - 1:
        #         res = res.append(currLetter) + res.append(freq)
        #         currLetter = ""
        #         freq = 0

        # return res
    





















s = Solution()

if s.shrink("aaaba") != "a3ba":
    print(s.shrink("aaaba"))
    raise Exception

if s.shrink("aaazba") != "a3zba":
    raise Exception

if s.shrink("a") != "a":
    raise Exception

# Additional Test Cases

# Test case 1: Repeating characters at the start
if s.shrink("bbcc") != "b2c2":
    print(s.shrink("bbcc"))
    raise Exception

# Test case 2: Mixed repeating and non-repeating characters
if s.shrink("aabbccdde") != "a2b2c2d2e":
    raise Exception

# Test case 3: All characters are different
if s.shrink("abcdefg") != "abcdefg":
    raise Exception

# Test case 4: All characters are the same
if s.shrink("aaaaaaa") != "a7":
    raise Exception

# Test case 5: Single character input
if s.shrink("z") != "z":
    raise Exception

# Test case 6: Long repeating sequence
if s.shrink("bbbbbbbbbb") != "b10":
    raise Exception

# Test case 7: Repeating characters spread across the string
if s.shrink("aabbccddaa") != "a2b2c2d2a2":
    raise Exception

# Test case 8: Empty string input
if s.shrink("") != "":
    raise Exception

# Test case 9: Repeating character at the end
if s.shrink("abcdefgggg") != "abcdefg4":
    raise Exception

# Test case 10: Mixed repeating and single characters
if s.shrink("hhhiiiij") != "h3i4j":
    raise Exception


