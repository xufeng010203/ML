


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_linklist(self, head):
        if not head:
            return None
        if head.next == None:
            return head

        tmp = None
        while head:
            cur = head
            cur.next = tmp
            tmp = cur
            head = head.next
        return tmp

