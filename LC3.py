class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        i = 0
        j = 0
        ans = 0
        for char in s:
            if char in dic:
                i = max(i, dic[char] + 1)
            ans = max(ans, j - i + 1)
            dic[char] = j
            j += 1
        return ans
