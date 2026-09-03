# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

head = [1,1,2,3,3]


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        k = 1
                
        for i in range(1, len(head)):
            if head[i] != head[i-1]:
                head[k] = head[i]
                k += 1
    
        return(head[0:k])

answer = Solution()

print(answer.deleteDuplicates(head))