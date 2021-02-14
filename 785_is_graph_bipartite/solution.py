class Solution:
    def helper(self, graph, color, start):
        queue = collections.deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            pres_color = color[node]
            for nbr in graph[node]:
                if color[nbr] == pres_color:
                    return False
                if color[nbr] == -1:
                    queue.append(nbr)

                color[nbr] = 1 - pres_color
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]

        for node in range(len(graph)):
            if color[node] == -1:
                if not self.helper(graph, color, node):
                    return False

        return True
