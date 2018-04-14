class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        i = 0
        while i < len(s):
            len1 = __expand__(s, i, i)
            len2 = __expand__(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
            i += 1
        return s[start:end + 1]


def __expand__(s, left, right):
    """
    :type s: str
    :type left: int
    :type right: int
    :rtype: int
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
