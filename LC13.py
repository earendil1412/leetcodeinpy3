dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        sum_result = 0
        minus_result = 0
        while n < len(s) - 1:
            if dic[s[n]] < dic[s[n + 1]]:
                minus_result += dic[s[n]]
            else:
                sum_result += dic[s[n]]
            n += 1
        return sum_result + dic[s[len(s) - 1]] - minus_result
