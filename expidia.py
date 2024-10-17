# num = 1

# array = [0, 1, 1, 1, 0, 0]

# nums = "".join(map(str, array))

# print(nums)

# num2 = int(nums, 2)

# print(bin(num))

# print(bin(num ^ num2))

class Solution:
    def is_num_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        elif num == 2:
            return True
        
        for i in range(2, int(num**.5) + 1, 1):
            if num % i == 0:
                return False

        return True
    
s = Solution()

assert s.is_num_prime(8) == False  # 8 is not prime (divisible by 2)
assert s.is_num_prime(18) == False  # 18 is not prime (divisible by 2)
assert s.is_num_prime(7) == True    # 7 is prime
assert s.is_num_prime(11) == True   # 11 is prime
assert s.is_num_prime(17) == True   # 17 is prime
assert s.is_num_prime(95) == False  # 95 is not prime (divisible by 5)
assert s.is_num_prime(93) == False  # 93 is not prime (divisible by 3)
assert s.is_num_prime(97) == True   # 97 is prime

# Additional edge cases
assert s.is_num_prime(0) == False     # 0 is not prime
assert s.is_num_prime(1) == False     # 1 is not prime
assert s.is_num_prime(2) == True      # 2 is the smallest prime number
assert s.is_num_prime(3) == True      # 3 is prime
assert s.is_num_prime(4) == False     # 4 is not prime (divisible by 2)
assert s.is_num_prime(-7) == False    # Negative numbers are not prime
assert s.is_num_prime(29) == True     # 29 is prime
assert s.is_num_prime(100) == False   # 100 is not prime (divisible by 2 and 5)
assert s.is_num_prime(101) == True    # 101 is prime
assert s.is_num_prime(999) == False   # 999 is not prime (divisible by 3)

print("All test cases passed!")