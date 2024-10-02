class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrc = [i for i in arr]
        arr.sort()
        hash = {}

        c = 1
        for n in arr:
            if n not in hash:
                hash[n] = c
                c += 1
        
        return [hash[i] for i in arrc]

        