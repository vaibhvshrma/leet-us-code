class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        skip = (numRows << 1) - 2

        res = [''] * len(s)
        k = 0

        tips = (len(s) + skip - 1) // skip  # ceil(len(s)/skip)

        for i in range(numRows):
            for j in range(tips):
                m, n = (j*skip) + i, ((j+1)*skip) - i
                if m < len(s):
                    res[k] = s[m]
                    k += 1
                if n < len(s) and i and i != numRows - 1:
                    res[k] = s[n]
                    k += 1
    
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()

    while True:
        x, y = input().split()
        y = int(y)
        print(sol.convert(x, y))