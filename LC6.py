class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result_arr = [""] * numRows
        i = 0
        circle = 2 * numRows - 2
        while i < len(s):
            j = i % circle
            if j < numRows:
                result_arr[j] += s[i]
            else:
                result_arr[circle - j] += s[i]
            i += 1
        result = ""
        for item in result_arr:
            result += item
        return result
