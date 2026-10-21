# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next or k == 0:
            return head
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        k %= n
        steps = n - k
        for _ in range(steps):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head

        