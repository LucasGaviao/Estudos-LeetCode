from typing import List

# using hash


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashmap:
                return[i, hashmap[a]]
            hashmap[nums[i]] = i

    # using twopointer: returning True or False
    def twoSum_twoPointer(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0, r = len(nums) - 1
        while l < r:
            if (nums[l] + nums[r]) < target:
                l += 1
            elif(nums[l] + nums[r]) > target:
                r -= 1
            elif(nums[l] + nums[r]) == target:
                return True
        return False
        
