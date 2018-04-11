class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        i = 0
        for num in nums:
            if num not in dict:
                dict[num] = i
            if target - num in dict and dict[target - num] != i:
                return [dict[target - num], i]
            i += 1
        raise ValueError("Illegal param")
