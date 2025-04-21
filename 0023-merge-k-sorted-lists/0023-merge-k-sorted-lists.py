# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
heapq solution = [(val, node_head)]
'''
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        for i , curr_list in enumerate(lists):
            if curr_list:
                heapq.heappush(queue , (curr_list.val, i, curr_list))

        dummy = ListNode(0)
        temp = dummy

        while queue:
            value, indx,  curr_node = heapq.heappop(queue)
            temp.next = ListNode(value)
            temp = temp.next
            if curr_node.next:
                curr_node = curr_node.next
                heapq.heappush(queue , (curr_node.val, indx, curr_node))
        return dummy.next