class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {
            0: {
                1: "I",
                5: "V",
                10: "X",
            },
            1: {
                1: "X",
                5: "L",
                10: "C",
            },
            2: {
                1: "C",
                5: "D",
                10: "M",
            },
            3: {
                1: "M",
            }
        }
        
        ctr = 0
        res = []
        while num:
            curr_map = mp.get(ctr)
            digit = num%10
            if digit == 4:
                temp = curr_map[1] + curr_map[5]
            elif digit == 9:
                temp = curr_map[1] + curr_map[10]
            elif digit == 0:
                temp = ""
            elif digit >= 5:
                temp = curr_map[5] + (curr_map[1]*(digit-5))
            else:
                temp = curr_map[1] * digit
            res.append(temp)
            ctr += 1
            num //= 10
        return "".join(reversed(res))
