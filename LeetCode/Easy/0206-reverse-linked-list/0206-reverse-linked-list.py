# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        tmp = dummy = ListNode()
        arr = []
        while head:
            arr.append(head.val)
            head = head.next if head.next else False
        while arr:
            ar = arr.pop()
            tmp.next = ListNode(ar)
            tmp = tmp.next

        return dummy.next
            