class Solution:
    # recursive (up-bottom)
    def tribonacci_r(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
    def tribonacci(self, n: int) -> int:
        tbArray = [0, 1, 1] + [0]*(n-2)
        
        l = 3
        while l < n+1:
            tbArray[l] = tbArray[l-3] + tbArray[l-2] + tbArray[l-1]
            # print(f"l: {l}, n: {n}, tbArray: {tbArray}")
            l += 1 
        
        return tbArray[n]
    

# sol = Solution()
# print(sol.tribonacci(0))
# print(sol.tribonacci(1))
# print(sol.tribonacci(2))
# print(sol.tribonacci(3))
# print(sol.tribonacci(4))
# print(sol.tribonacci(5))