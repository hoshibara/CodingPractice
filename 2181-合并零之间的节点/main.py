# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_tail = result
        tmp = 0
        now = head.next
        while now is not None:
            if now.val == 0:
                result_tail.next = ListNode(val=tmp)
                result_tail = result_tail.next
                tmp = 0
            else:
                tmp += now.val
            now = now.next
        return result.next
