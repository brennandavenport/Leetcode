class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_num_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        num = 0
        for i in range(len(s)):
            if  i + 1 < len(s) and roman_num_map.get(s[i]) < roman_num_map.get(s[i + 1]):
                num -= roman_num_map.get(s[i])
            else:
                num += roman_num_map.get(s[i])
        return num
    
s = Solution()

string = "MCMXCIVIII"
print(s.romanToInt(string))

string = "hello"

