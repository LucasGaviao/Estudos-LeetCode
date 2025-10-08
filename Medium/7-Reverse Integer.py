class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        (sign, x) = (1, x) if x > 0 else (-1, -x)
        # print(sign, x)
        while x > 0: 
            y *= 10 
            y += x%10 
            x //= 10 
            # print(x, y)
            if (y < (-2)**31) or (y > 2**31 - 1):
                return 0
        return y * sign
    
# print(f'(-2)**31: {(-2)**31}')
# print(f'(2)**31: {(2)**31 - 1}')
# sol = Solution()
# print(sol.reverse(123499))
# print(sol.reverse(-123))
# print(sol.reverse(1534236469))
# print(9646324351 > 2147483647)