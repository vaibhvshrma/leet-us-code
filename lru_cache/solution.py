import heapq

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.ts = -1    # timestamp
        self.dct = {}
        self.pq = []
        self.most_recent_time = {}

    def _pop(self, key: int) -> None:
        del self.dct[key]

    def _pop_lru(self):
        while self.pq:
            fr = heapq.heappop(self.pq)
            ts, key = fr[0], fr[1]
            if key in self.dct and self.most_recent_time[key] == ts:
                self._pop(key)
                return

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        self.ts += 1
        self.most_recent_time[key] = self.ts
        heapq.heappush(self.pq, (self.ts, key))

        return self.dct[key]

    def put(self, key: int, value: int) -> None:
        self.ts += 1

        if key not in self.dct:
            if self.size == self.cap:
                    self._pop_lru()
            else:
                self.size += 1

        self.dct[key] = value
        self.most_recent_time[key] = self.ts
        heapq.heappush(self.pq, (self.ts, key))

    def __str__(self):
        res = f'Timestamp: {self.ts}\n'
        res += (f'Size: {self.size}\n')
        res += (f'Key and Vals: {self.dct}\n')
        res += (f'Most Recent Time: {self.most_recent_time}')
        return res
