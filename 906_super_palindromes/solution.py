class Solution:
    @staticmethod
    def is_palindrome(num):
        # num = str(num)
        return num == num[::-1]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        mx = int(1e5)+1
        left = int(left)
        right = int(right)
        cnt = 0

        for i in range(1, mx):
            s_num = str(i)
            # even length
            num = int(s_num + s_num[::-1])
            sq = num * num
            if sq > right:
                break
            if sq >= left and self.is_palindrome(str(sq)):
                print(sq)
                cnt += 1

        for i in range(1, mx):
            s_num = str(i)
            # odd length
            num = int(s_num + s_num[::-1][1:])
            sq = num * num
            if sq > right:
                break
            if sq >= left and self.is_palindrome(str(sq)):
                print(sq)
                cnt += 1

        return cnt
