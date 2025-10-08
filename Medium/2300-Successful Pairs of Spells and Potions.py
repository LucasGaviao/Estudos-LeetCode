from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = [0 for _ in range(len(spells))]
        potions.sort()
        for i in range(len(output)):
            idx = self.bns(potions, spells[i], success)
            output[i] = len(potions) - idx if idx != -1 else 0
        return output
    
    def bns(self, potions: List[int], spell: int, success: int):
        low, high = 0, len(potions) - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if potions[mid] * spell >= success:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return idx

print(Solution().successfulPairs([5,1,3],[1,2,3,4,5],7))
print(Solution().successfulPairs([3,1,2],[8,5,8],16))