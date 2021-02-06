class Solution:
    def dfs(self, root):
        while self.adjlist[root]:
            nxt = self.adjlist[root].popleft()
            self.dfs(nxt)
            
        self.res.appendleft(root)
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjlist = collections.defaultdict(list)
        
        for u, v in tickets:
            adjlist[u].append(v)
            
        for i in adjlist:
            adjlist[i] = collections.deque(sorted(adjlist[i]))
            
        self.adjlist = adjlist
        self.res = collections.deque()
        self.dfs('JFK')
        return self.res
