# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mdc(x, y):
        # garantido q x seja o menor
        if y < x:
            return(Solution.mdc(y,x))

        if y%x == 0:
            return x

        i = 0
        while i <= x//2:
            i += 1
            if x%i != 0:
                continue
            k = x/i
            if y%k == 0:
                return int(k)
        
        return 1
            

        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        while head and head.next != None:
            ant = head
            head = ant.next
            
            ant.next = ListNode(Solution.mdc(ant.val,head.val), head)
            
        return first