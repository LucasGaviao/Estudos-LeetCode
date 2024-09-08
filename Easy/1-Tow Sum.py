class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashmap:
                return[i, hashmap[a]]
            hashmap[nums[i]] = i
