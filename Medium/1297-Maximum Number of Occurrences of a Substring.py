class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashmap = {}
        max = 0
        for i in range(len(s)-minSize+1):
            chars = []
            a = s[i:i+minSize]
            for c in a:
                if c not in chars:
                    chars.append(c)
            if len(chars) > maxLetters:
                continue
            if a in hashmap:
                hashmap[a] += 1
            else:
                hashmap[a] = 1
            
            if hashmap[a] > max:
                max = hashmap[a]
       
        if maxSize != minSize:
            for i in range(len(s)-maxSize+1):
                chars = []
                a = s[i:i+maxSize]
                for c in a:
                    if c not in chars:
                        chars.append(c)
               # print(chars)
                if len(chars) > maxLetters:
                    continue
                if a in hashmap:
                    hashmap[a] += 1
                else:
                    hashmap[a] = 1
                
                if hashmap[a] > max:
                    max = hashmap[a]
                #print(hashmap)
        return max