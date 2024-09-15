class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp

        i = 0
        for i in range(len(matrix)):
            linha = matrix[i]
            esq = 0
            d = len(linha)-1
            while esq < d:
                tmp = linha[esq]
                linha[esq] = linha[d]
                linha[d] = tmp
                esq += 1
                d -= 1