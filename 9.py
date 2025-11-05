class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:     
            return True
        if x % 10 == 0 and x != 0:
            return False
        
        original = x
        digits = []
        while x > 0:
            rem = x % 10
            digits.append(str(rem))
            x = x // 10
        res = "".join(digits)
        
        if original == int(res):
            return True
        else:
            return False
