# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        head = dummyNode
        carry = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0

            head.next = ListNode(sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            sum = l1.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            head.next = ListNode(sum)
            head = head.next
            l1 = l1.next

        while l2 != None:
            sum = l2.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            head.next = ListNode(sum)
            head = head.next
            l2 = l2.next

        if carry > 0:
            head.next = ListNode(carry)

        return dummyNode.next
