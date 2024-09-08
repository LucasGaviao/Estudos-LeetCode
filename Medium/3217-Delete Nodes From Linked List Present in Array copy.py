# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]: # type:ignore
        nums = set(nums)
        ant = None
        ih = head
        while ih != None and ih.next != None:

            # evita começar com um numero que esta em nums
            if ih.val in nums and ant == None:
                head = head.next
                ih = ih.next
                continue

            ant = ih
            if ih.next.val in nums:
                next2 = ih.next.next
                while next2 != None and next2.val in nums:
                    next2 = next2.next
                ant.next = next2
                ih = ant.next
            else:
                ih = ih.next

        return head

