# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # verificando quantos ListNodes tem por parte
        c = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            c += 1
        divs = c/k
        if divs < 1: 
            divs = 1

        # criando a list de output
        output = []
        #print(divs , divs%1)
        for i in range(k):
            if head:
                output.append(head)
                for _ in range(1, int(divs)):
                    if head == None:
                        break
                    head = head.next

                if divs%1 != 0 and i < c%k:
                    if head == None:
                        continue
                    head = head.next
                
                if head:
                    ant = head
                    head = ant.next
                    ant.next = None
            else:
                output = output + [ListNode('',None) for _ in range(i,k)]
                #print(output)
                break

        return output
        
        
        


