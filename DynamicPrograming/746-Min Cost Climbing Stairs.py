from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dpArr = [cost[0], cost[1]]
        i = 0
        for i in range(2, len(cost)):
           dpArr.append(cost[i] + min(dpArr[i-1], dpArr[i-2]))
        # print(i, len(cost))
        dpArr.append(min(dpArr[i], dpArr[i-1]))
        return dpArr[-1]
        