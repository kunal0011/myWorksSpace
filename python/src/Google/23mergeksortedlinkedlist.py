from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Initialize the heap with the first node of each list
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        # Process the heap until it's empty
        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
