from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])

class Solution:
    def is_valid_point(self, pt):
        return pt.x in range(self.num_rows) and pt.y in range(self.num_cols)

    def set_visited(self, pt):
        self.grid[pt.x][pt.y] = '0'

    def is_land(self, pt):
        return self.grid[pt.x][pt.y] == '1'

    def bfs(self, root):
        '''
        Breadth first search starting from root
        with neighbours being 4 connected
        '''
        grid = self.grid
        queue = deque()
        queue.append(root)

        while(queue):
            curr = queue.popleft()

            if not self.is_land(curr):
                continue

            self.set_visited(curr)

            left_pt = Point(curr.x, curr.y-1)
            right_pt = Point(curr.x, curr.y+1)
            below_pt = Point(curr.x+1, curr.y)
            above_pt = Point(curr.x-1, curr.y)

            process = lambda pt: (self.is_valid_point(pt)
                and self.is_land(pt)
                and queue.append(pt)
            )

            process(left_pt)
            process(right_pt)
            process(below_pt)
            process(above_pt)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        self.grid = grid
        self.num_rows = num_rows
        self.num_cols = num_cols

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    start = Point(i, j)
                    self.bfs(start)
                    num_islands += 1

        return num_islands
