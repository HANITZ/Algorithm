# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = ''
        while l1 != None:
            n1= str(l1.val) + n1
            l1 = l1.next

        n2 = ''
        while l2 != None:
            n2 = str(l2.val) + n2
            l2 = l2.next
        
        num = str(int(n1)+int(n2))
        node = ListNode()
        cur = node
        for i in range(len(num)-1, -1, -1):
            cur.next = ListNode(int(num[i]))

            cur = cur.next
   
    
        return node.next
            