class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        table = {}
      #  print(s1)
      #  print(s2)
        out = []
        for word in s1:
           # print(word, out)
            if word in table and word in out:
                out.remove(word)
                continue
            if word not in s2 and word not in table:
                out.append(word)
                table[word] = 1
            if word in s2:
                s2.remove(word)
                table[word] = 1
        
        for word in s2:
            if word in table and word in out:
                out.remove(word)
                continue

            if word not in s1 and word not in table:
                out.append(word)
                table[word] = 1

        return out
                