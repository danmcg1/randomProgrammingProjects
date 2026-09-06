# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

nums = [1,1,2,3,4,3,4]

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

        


answer = Solution()

print(answer.singleNumber(nums))