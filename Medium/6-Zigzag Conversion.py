class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = ['']*numRows
        k = 0
        while k < len(s):
            for i in range(numRows):
                if k < len(s):
                    array[i] = array[i] + s[k]
                    k += 1
            #print(i)
            #print(array)
            if i == numRows-1:
                i -= 1
                while i > 0 and k < len(s):
                    array[i] = array[i] + s[k]
                    i -= 1
                    k += 1
            #print(array)
        output = ''
        for sub in array:
            output += sub
        return output