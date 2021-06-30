



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def merge_two_linklist(self, l1, l2):
        """
        合并俩个链表
        :param l1:
        :param l2:
        :return:
        """
        if not l1 and l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        #选出第一个节点
        if l1.val < l2.val:
            head = ListNode(l1.val)
            cur = head
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            cur = head
            l2 = l2.next

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.val
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head

