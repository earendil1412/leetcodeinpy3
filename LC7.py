class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        if x >= 10:
            divide = 10
        else:
            divide = -10
        while x // divide != 0:
            divide *= 10
        result = 0
        i = 1
        while divide > 1 or divide < -1:
            divide //= 10
            if x < 0:
                temp = 0 - x // divide
                x += temp * divide
            else:
                temp = x // divide
                x -= temp * divide
            result += temp * i
            i *= 10
        if -2147483648 <= result <= 2147483647:
            return result
        else:
            return 0
