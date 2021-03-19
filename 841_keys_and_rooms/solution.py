class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = collections.deque([0])
        
        while queue:
            front = queue.popleft()
            if not visited[front]:
                for nbr in rooms[front]:
                    if not visited[nbr]:
                        queue.append(nbr)
                visited[front] = True
        
        return all(visited)
