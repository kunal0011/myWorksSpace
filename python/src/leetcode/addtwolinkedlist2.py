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
            sum = l1.val  + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            head.next = ListNode(sum)
            head = head.next
            l1 = l1.next
            
        while l2 != None:
            sum = l2.val  + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            head.next = ListNode(sum)
            head = head.next
            l2 = l2.next

        if carry > 0:
            head.next= ListNode(carry)
            
        return dummyNode.next
    
class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        carry, curr = 0, dummy
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
if __name__ == '__main__':
     node = ListNode(2)
     node.next = ListNode(4)
     node.next.next = ListNode(3)
     
     node1 = ListNode(5)
     node1.next = ListNode(6)
     node1.next.next = ListNode(4)
     
     s = Solution1()
     print(s.addTwoNumbers(node,node1))



        