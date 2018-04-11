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
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
            i += 1
        raise ValueError("Illegal param")
