from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convertendo os inteiros para string
        nums_str = list(map(str, nums))
        
        # Comparador personalizado
        def compare(x, y):
            # Se x + y é maior, x deve estar antes de y
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Ordenando a lista com o comparador personalizado
        nums_str.sort(key=cmp_to_key(compare))
        
        # Concatenando os numeros da lista ordenada
        largest_num = ''.join(nums_str)
        
        # Edge case: Se o maior numero da lista for 0
        if largest_num[0] == '0':
            return '0'
        
        return largest_num