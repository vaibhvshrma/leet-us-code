from typing import List
import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # single source shortest path
        # dijkstra's algo

        # first take input
        adjlist = collections.defaultdict(list)
        for sorc, dest, cost in flights:
            adjlist[sorc].append((dest, cost))

        vis = [False] * n
        pq = [(0, src, 0)]

        while pq:
            cost, node, stop = heapq.heappop(pq)
            if node == dst:
                return cost
            if stop > K:
                continue
            if not vis[node]:
                vis[node] = True
                for nbr, prc in adjlist[node]:
                    heapq.heappush(pq, (cost+prc, nbr, stop+1))

        return -1


if __name__ == "__main__":
    import ipdb
    ipdb.set_trace()
    print(Solution().findCheapestPrice(
        5,
        [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
        2,
        1,
        1
    ))

