class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        # Push all digits of l1 to stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # Push all digits of l2 to stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Process both stacks
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)
            new_node.next = head
            head = new_node

        return head
