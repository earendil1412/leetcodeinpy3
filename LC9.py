class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x % 10 == 0 and x != 0) or x < 0:
            return False
        elif x < 10:
            return True
        else:
            temp_str = str(x)
            if temp_str == temp_str[::-1]:
                return True
            else:
                return False
