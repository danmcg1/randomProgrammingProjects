
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Constraints:
#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.


list1 = [1,3,5]
list2 = [2,4,6]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
    #     """
    #     :type list1: Optional[ListNode]
    #     :type list2: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """

        dummy  = ListNode()
        current = dummy
        while(list1 is not None and list2 is not None):
            if(list1.val <= list2.val):
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if(list1 is not None):
            current.next = list1
        elif(list2 is not None):
            current.next = list2
        return dummy.next


    def createNodes(self, values): 
        if not values:
            return None
        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
        
def printLinkedList(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements) if elements else "Empty")

answer = Solution()

l1 = answer.createNodes([1, 3, 5])
l2 = answer.createNodes([2, 4, 6])

merged_head = answer.mergeTwoLists(l1, l2)
printLinkedList(merged_head)
