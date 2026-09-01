# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:

#     1 <= nums.length <= 1^4
#     -1^4 <= nums[i] <= 1^4
#     nums contains distinct values sorted in ascending order.
#     -1^4 <= target <= 1^4

nums = [1,3,5,6]
target = 2

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0       
        
        while index <= (nums[-1]*2):
            if  index >= len(nums):
                return index
            elif nums[index] < target:
                index += 1
            else:
                return index
             

answer = Solution()

print(answer.searchInsert(nums,target))