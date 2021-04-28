class Solution:
    @staticmethod
    def get_prefix(arr):
        pref = []
        sm = 0
        for i in arr:
            sm += i
            pref.append(sm)
        return pref

    def leastBricks(self, wall: List[List[int]]) -> int:
        pref_wall = [self.get_prefix(row) for row in wall]
        full_length = sum(wall[0])
        cntr = collections.Counter()
        for row in pref_wall:
            for edge in row:
                cntr[edge] += 1
        cntr[full_length] = 0

        return len(wall) - max(cntr.values())
