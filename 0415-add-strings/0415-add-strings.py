class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        result = []
        while i >= 0 or j >= 0 or c:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            tot = n1 + n2 + c
            result.append(str(tot % 10))
            c = tot // 10

            i -= 1
            j -= 1

        return ''.join(reversed(result))
