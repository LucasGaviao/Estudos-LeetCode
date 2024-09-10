# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matriz = []
        for i in range(m):
            linha = []
            for j in range(n):
                linha.append(-1)
            matriz.append(linha)
        
        inicio_lin = 0
        final_lin = m
        inicio_col = 0
        final_col = n
        lin = 0
        col = -1
        for _ in range(n):
            #print('lin: ',lin, inicio_lin, final_lin,'col: ', col, inicio_col, final_col)
            if col == inicio_col - 1:
                col += 1
                while col < final_col:
                    if head == None:
                        return matriz
                    matriz[lin][col] = head.val
                    ant = head
                    head = ant.next
                    col += 1
                col -= 1
                inicio_lin += 1
                #print('lin: ',lin, inicio_lin, final_lin,'col: ', col, inicio_col, final_col)
            #print(1, matriz)
            if lin == inicio_lin - 1:
                lin += 1
                while lin < final_lin:
                    if head == None:
                        return matriz
                    matriz[lin][col] = head.val
                    ant = head
                    head = ant.next
                    lin += 1
                lin -= 1
                final_col -= 1
                #print('lin: ',lin, inicio_lin, final_lin,'col: ', col, inicio_col, final_col)
            #print(2, matriz)

            if col == final_col:
                col -= 1
                while col >= inicio_col:
                    if head == None:
                        return matriz
                    matriz[lin][col] = head.val
                    ant = head
                    head = ant.next
                    col -= 1
                col += 1
                final_lin -= 1
                #print('lin: ',lin, inicio_lin, final_lin,'col: ', col, inicio_col, final_col)
            #print(3, matriz)

            if lin == final_lin:
                lin -= 1
                while lin >= inicio_lin:
                    if head == None:
                        return matriz
                    matriz[lin][col] = head.val
                    ant = head
                    head = ant.next
                    lin -= 1
                lin += 1
                inicio_col += 1
            #print('lin: ',lin, inicio_lin, final_lin,'col: ', col, inicio_col, final_col)

            #print(4, matriz)
        return matriz