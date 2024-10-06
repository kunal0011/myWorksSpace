class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Step 1: Calculate lengths of both linked lists
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lenA = get_length(headA)
        lenB = get_length(headB)

        # Step 2: Align the pointers
        # Move the pointer of the longer list ahead by the difference in lengths
        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        # Step 3: Move both pointers until they meet or reach the end
        while headA and headB:
            if headA == headB:
                return headA  # Intersection point
            headA = headA.next
            headB = headB.next

        return None  # No intersection
