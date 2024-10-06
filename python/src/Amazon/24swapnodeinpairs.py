# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0
        dummyNode = ListNode(-1)
        prevgrouphead = dummyNode
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        curr = head
        next = head

        while count >= 0:
            prev = None
            head = curr
            if count >= 2:
                for i in range(2):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
            else:
                prevgrouphead.next = curr
                break
            prevgrouphead.next = prev
            prevgrouphead = head
            count -= 2

        return dummyNode.next
