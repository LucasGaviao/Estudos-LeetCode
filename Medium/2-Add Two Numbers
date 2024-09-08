# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        give = 0
        h3 = ListNode()
        
        while (l1 != None and l2 != None): 
            new = l1.val + l2.val + give
            give = new//10
            new = new%10
    
            if h3.next == None:
                h3.next = ListNode(new, None)
                i3 = h3.next 
            else:
                i3.next = ListNode(new, None)
                i3 = i3.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            new = l1.val + give
            give = new//10
            new = new%10
            i3.next = ListNode(new, None)
            i3 = i3.next
            l1 = l1.next
        while l2:
            new = l2.val + give
            give = new//10
            new = new%10
            i3.next = ListNode(new, None)
            i3 = i3.next
            l2 = l2.next
        
        if give == 1:
            i3.next = ListNode(give, None)
        return h3.next
