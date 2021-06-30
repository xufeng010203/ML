'''

输入一个链表，输出该链表中倒数第k个节点

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def find_kth_o_tail(self, head, k):
        """
        查找链表中第k个节点
        :param k:
        :return:
        """
        if not head or not k:
            return None
        count = 0
        p = head
        q = head
        while count < k:
            p = p.next
            count += 1
        while p:
            q = q.next
            p = p.next
        return q.val
