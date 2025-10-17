class Solution:
    hmap = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if str(n) not in self.hmap:
            self.hmap[str(n)] = Solution.climbStairs(self, n-1) + Solution.climbStairs(self, n-2)
        return self.hmap[str(n)]