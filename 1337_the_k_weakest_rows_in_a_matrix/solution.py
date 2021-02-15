class Node:
    def __init__(self, idx, num_civs):
        self.idx = idx
        self.num_civs = num_civs
        
    def __lt__(self, other):
        if self.num_civs == other.num_civs:
            return self.idx > other.idx 
        return self.num_civs < other.num_civs 

    
class Solution:
    @staticmethod
    def get_num_civs(row):
        return row.count(0)
        
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mn_heap = [Node(i, Solution.get_num_civs(mat[i])) for i in range(k)]
        heapq.heapify(mn_heap)
        for i in range(k, len(mat)):
            row = mat[i]
            num_civs = Solution.get_num_civs(row)    
            if mn_heap[0].num_civs < num_civs:     
                heapq.heappop(mn_heap)
                heapq.heappush(mn_heap, Node(i, num_civs))
        
        res = [node.idx for node in sorted(mn_heap)]
        res.reverse()
        return res
