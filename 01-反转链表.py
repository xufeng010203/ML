# # class Solution:
# #     def ReverseLinkList(self, node):
# #
# #
# #         if not node or node.next == None:
# #             return node
# #
# #         pre = None
# #         while node:
# #             cur = node
# #             node = node.next
# #             cur.next = pre
# #             pre = node
# #
# #         return pre
# #
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def MergeTwoLinkList(self, l1, l2):
#         if not l1 and l2:
#             return None
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#
#         head = ListNode(0)
#         cur = head
#         while l1 and l2:
#             if l1.val > l2.val:
#                 head.next = l2
#                 l2 = l2.next
#             else:
#                 head.next = l1
#                 l1 = l1.next
#             cur = cur.next
#
#         if l1:
#             cur.next = l1
#         if l2:
#             cur.next = l2
#
#         return cur


class Solution:
    def DeleteNode(self, head, node):
        if head == node:
            del node




        if node.next == None:
            while head:
                if head == node:
                    head.next = None
                head = head.next
        else:
            node.val = node.next.val
            n_node = node.next
            node.next = n_node.next
            del n_node

