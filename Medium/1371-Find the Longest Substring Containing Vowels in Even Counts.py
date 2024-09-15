class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Mapa de estado das vogais para seus respectivos bits
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        # Estado inicial onde todas as vogais estão em contagem par
        state = 0
        # Dicionário para armazenar a primeira ocorrência de cada estado
        state_to_index = {0: -1}
        max_len = 0

        # Percorrer a string
        for i, char in enumerate(s):
            # Se o caractere for uma vogal, altere o bit correspondente
            if char in vowels:
                state ^= (1 << vowels[char])

            # Se o estado já foi encontrado antes, calcular a distância
            if state in state_to_index:
                max_len = max(max_len, i - state_to_index[state])
            else:
                # Armazenar o primeiro índice onde este estado ocorre
                state_to_index[state] = i

        return max_len
