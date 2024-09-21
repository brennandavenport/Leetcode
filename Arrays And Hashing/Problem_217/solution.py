class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}

        for num in nums:
            hashmap[num] = 0
        
        if len(hashmap) == len(nums):
            return False
        return True
    
s = Solution()

nums = [1,2,3]
print(s.containsDuplicate(nums))

