class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        g = nums[0]
        m = 0
        cont = 1
        for i in range(1, len(nums)):
            if nums[i] < g:
                continue
            if nums[i] > nums[i-1]:
                if nums[i] > g:
                    g = nums[i]
                    m = 1
                cont = 1
                continue
            if nums[i] == nums[i-1] & nums[i]:
                cont += 1
            m =max(m, cont)      
        return max(m, cont)