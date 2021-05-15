class Solution:
    @staticmethod
    def slide_stones(row: List[str]) -> List[str]:
        res = []
        stones = 0
        total_cells = 0
        row.append("*")
        for i in range(len(row)):
            ch = row[i]
            total_cells += 1
            if ch == "#":
                stones += 1
            elif ch == "*":
                res.extend(["."] * (total_cells-stones-1))
                res.extend(["#"] * stones)
                res.append("*")
                stones = total_cells = 0
        return res[:-1]

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        slid_stones = [self.slide_stones(row) for row in box]
        res = [[arr[i] for arr in reversed(slid_stones)] for i in range(len(slid_stones[0]))]
        return res
