from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = answer = ListNode()
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heappop(heap)
            idx = node[1]
            answer.next = node[2]
            
            answer = answer.next
            if answer.next:
                heappush(heap, (answer.next.val, idx, answer.next))
        return root.next
