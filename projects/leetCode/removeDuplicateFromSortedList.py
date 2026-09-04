# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                # Bypass the duplicate node (DO NOT move current forward yet!)
                current.next = current.next.next
            else:
                # Only move forward if the next value is different
                current = current.next

        return head


    def createNodes(self, values): 
        if not values:
            return None
        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def printNodes(self, head):
        elements = []
        current = head
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements))

answer = Solution()

head = answer.createNodes([1,1,2,3,3])
print(answer.deleteDuplicates(head))
