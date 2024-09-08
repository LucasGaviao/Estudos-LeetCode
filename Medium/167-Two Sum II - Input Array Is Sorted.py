class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type:ignore
        a = 0
        b = len(numbers) - 1
        while numbers[a] + numbers[b] != target:
            if numbers[a] + numbers[b] < target:
                a += 1
            else:
                b -= 1
        return[a+1, b+1]