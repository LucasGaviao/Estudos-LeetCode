class Solution:
    def singleNumber(self, nums: List[int]) -> int: # type:ignore
        ones = 0
        twos = 0

        for i in nums:
            ones = (i ^ ones) & ~twos
            twos = (i ^ twos) & ~ones
        
        return ones