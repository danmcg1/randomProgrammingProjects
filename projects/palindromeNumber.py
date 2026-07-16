
# Check whether a number is a palindrome with True or False being returned

x = 1000001

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for n in range(int(len(str(x))/2)):
            if str(x)[n] != str(x)[-(n+1)]:
                return(False)
                break
            else:
                n += 1
        return(True)
        
            
        
answer = Solution()

print(answer.isPalindrome(x))


