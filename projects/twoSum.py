
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,3]
# target = 6

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results_dict = {}
        results = []

        for index, num in enumerate(nums):
            complement = target - num
            
            if complement in results_dict:
                return(results_dict[complement], index)
                
            results_dict.update({num: index})

solver = Solution()
print(solver.twoSum(nums, target))


    