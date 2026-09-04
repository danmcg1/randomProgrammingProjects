class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Allows print(node) to output a readable representation like: 1 -> 2 -> 3"""
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


# ==========================================
# LINKED LIST HELPER FUNCTIONS
# ==========================================


def build_list(values):
    """Converts a Python list into a Linked List.

    Usage: head = build_list([1, 2, 3])
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def to_list(head):
    """Converts a Linked List back into a standard Python list.

    Useful for quick assertions in unit tests.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result