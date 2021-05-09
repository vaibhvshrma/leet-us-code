import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        Try to make array of 1s from target
        """
        if len(target) == 1 and target[0] != 1:
            return False

        total_sum = sum(target)
        mx_heap = [-x for x in target]
        heapq.heapify(mx_heap)

        while mx_heap and mx_heap[0] != -1:
            top = -heapq.heappop(mx_heap)
            remaining_sum = total_sum - top
            if remaining_sum >= top or remaining_sum == 0:
                return False
            if remaining_sum == 1:
                return True

            q, r = divmod(top, remaining_sum)
            total_sum -= q * remaining_sum
            heapq.heappush(mx_heap, -r)
        return True
