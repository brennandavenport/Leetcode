class solution(object):
    def palidrome(self, num):
        original = str(num)
        reversed_string = original[::-1]

        return reversed_string == original
    