class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that helps simplify edge cases
        dummy = ListNode(0, head)
        first = second = dummy

        # Move `first` pointer `n+1` steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both `first` and `second` pointers until `first` reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # `second.next` is the node to be removed
        second.next = second.next.next

        return dummy.next
