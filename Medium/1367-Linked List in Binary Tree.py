# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.storinglist = []

    def isSubPath(self, head, root):
        self.storeToList(head, root)
        for element in self.storinglist:
            if self.checkSubPath(head, element):
                return True
        return False

    def storeToList(self, head, root):
        if head is None or root is None:
            return
        if head.val == root.val:
            self.storinglist.append(root)
        self.storeToList(head, root.left)
        self.storeToList(head, root.right)

    def checkSubPath(self, head, node):
        if head is None:
            return True
        if node is None:
            return False

        if head.val == node.val:
            return self.checkSubPath(head.next, node.left) or self.checkSubPath(head.next, node.right)
        return False