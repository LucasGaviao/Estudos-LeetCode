import math
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ordered_d = sorted(difficulty)
        # ordered_p = sorted(profit)
        total_profit = 0

        for i in range(len(worker)):
            curr_profit = self.search(difficulty, ordered_d, profit, worker[i])
            total_profit += curr_profit
        return total_profit
            

    def search(self, difficulty, ordered_d, profit, worker):
        low, high = 0, len(ordered_d) - 1
        value = 0
        while low < high:
            mid = math.ceil((low + high)/2)
            if ordered_d[mid] <= worker:
                low = mid + 1
                value = max(profit[difficulty.index(ordered_d[mid])], value)
            else:
                high = mid - 1
            print(f'w={worker}, mid={mid}, difficulty[mid]={difficulty[mid]}, value={value}')
        return value

        

# class Job:
#     def __init__(self, d: int, p: int):
#         self.d = d
#         self.p = p
        
# print(Solution().maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
# print(Solution().maxProfitAssignment([85,47,57],[24,66,99],[40,25,25]))
print(Solution().maxProfitAssignment([68,35,52,47,86],[67,17,1,81,3],[92,10,85,84,82]))