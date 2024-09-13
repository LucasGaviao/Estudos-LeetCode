class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr_s = len(arr) + 1
        prefix = [0 for _ in range(arr_s)]
        for i in range(1, arr_s):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        
        return [(prefix[right+1] ^ prefix[left]) for left, right in queries] 
         
