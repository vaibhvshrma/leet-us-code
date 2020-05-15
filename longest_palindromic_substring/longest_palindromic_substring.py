class Solution:    
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        
        res = ''

        # for element i find max palindromic substring of odd len centered at i

        for i in range(0, len(s)):
            l,r = i-1, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if len(res) < (r-l-1):
                res = s[l+1:r]
        
        # find max palindromic substring of even len having centers i-1, i

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                l,r = i-2, i+1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                
                if len(res) < (r-l-1):
                    res = s[l+1:r]
        
        return res

if __name__ == '__main__':
    sol = Solution()

    while 1:
        print(sol.longestPalindrome(input()))