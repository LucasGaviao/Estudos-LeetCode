class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c =0
        d = 0
        for bill in bills:
            if bill == 5:
                c += 1
            elif bill == 10:
                c -= 1
                d += 1
            else:
                if d > 0:
                    d -= 1
                    c -= 1
                else:
                    c -= 3
            if c < 0:
                return "false"
        return "true"

s = Solution()
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{s.lemonadeChange(case)}\n")
exit(0)