class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cont = 0
        for word in words:
            valid = True
            for char in word:
                if char not in allowed:
                    valid = False
                    break
            if valid:
                cont += 1

        return cont