dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(' ')
        if str == "":
            return 0
        if str[0] not in dic and str[0] != "-" and str[0] != "+":
            return 0
        num = 0
        if str[0] == "+" or str[0] == "-":
            if str[0] == "-":
                num = 0 - inAtoi(str[1:len(str)])
            else:
                num = inAtoi(str[1:len(str)])
        else:
            num = inAtoi(str)
        if num > 2147483647:
            return 2147483647
        elif num < -2147483648:
            return -2147483648
        else:
            return num


def inAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    i = 0
    while i < len(str) and str[i] in dic:
        i += 1
    if i == 0:
        return 0
    return int(str[0:i])
