# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order.
#  The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [9]
# Output: [1,0]

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]

digits = [4,3,2,1]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = int("".join(map(str, digits)))
    
        integer += 1
    
        intList = list(str(integer))

        convertedList = [int(i) for i in intList]
    
        return convertedList
        
            
        
answer = Solution()

print(answer.plusOne(digits))