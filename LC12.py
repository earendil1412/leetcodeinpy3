__dic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = 1
        result = ""
        while num > 0:
            current_num = num % 10
            result = num_convert(current_num, n) + result
            num = num // 10
            n = n * 10
        return result


def num_convert(num, n):
    """
    :type num: int
    :type n: int
    :rtype: str
    """
    if num == 0:
        return ""
    elif num == 1:
        return __dic[n]
    elif num == 2:
        return __dic[n] + __dic[n]
    elif num == 3:
        return __dic[n] + __dic[n] + __dic[n]
    elif num == 4:
        return __dic[n] + __dic[5 * n]
    elif num == 5:
        return __dic[5 * n]
    elif num == 6:
        return __dic[5 * n] + __dic[n]
    elif num == 7:
        return __dic[5 * n] + __dic[n] + __dic[n]
    elif num == 8:
        return __dic[5 * n] + __dic[n] + __dic[n] + __dic[n]
    else:
        return __dic[n] + __dic[10 * n]
