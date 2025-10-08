class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0        
        h = set()
        max_s = l = 0
        r = 1
        h.add(s[l])
        while l < r and r < len(s):
            if s[r] not in h:
                h.add(s[r])
                max_s = max(max_s, len(h))
            else:
                while l < s.index(s[r]) + 1:
                    h.remove(s[l])
                    l += 1
            r += 1
        return max(max_s, len(h))