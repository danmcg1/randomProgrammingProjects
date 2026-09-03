# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.

a = "1010"
b = "1011"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        stringDiff = len(a)-len(b)

        if stringDiff > 0:
            b = b.rjust(len(a),"0")
        elif stringDiff <= 0:
            a = a.rjust(len(b), "0")

        a = list(a)
        b = list(b)
        output = [0] * max(len(a), len(b))

        i = 0
        carry = 0
        while i < max(len(a), len(b)):
            i += 1

            total = int(a[-i]) + int(b[-i]) + carry

            output[-i] = total % 2
            carry = total // 2
            
            
        if carry == 1:
            output.insert(0, 1)

        result = ''.join([str(s) for s in output])
            
        #return result

        
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return bin(int(a,2) + int(b,2))[2:] 


answer = Solution()

print(answer.addBinary(a,b))