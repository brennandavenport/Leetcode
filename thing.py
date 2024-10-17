import time

# from PyPDF2 import PdfMerger

# merger = PdfMerger()

# merger.append("resumeC.pdf")
# merger.append("transcriptC.pdf")

# merger.write("merged.pdf")
# merger.close()

# Hashing an integer
print(hash(42))  # Output: (some integer)

# Hashing a string
print(hash("hello"))  # Output: (some integer)
print(hash("hello!")) 

print(time.time())

# Hashing a tuple (immutable type)
# print(hash((1, 2, 3)))  # Output: (some integer)

# Hashing a list (raises a TypeError because lists are mutable)
# print(hash([1, 2, 3]))  # Raises TypeError: unhashable type: 'list'


class Solution:
    def calc_fib(self, num) -> int:
        if num == 0 or num  == 1:
            return num
        
        return (self.calc_fib(num - 1) + self.calc_fib(num - 2))
    

s = Solution()

print(s.calc_fib(5))
