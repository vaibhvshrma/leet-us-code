class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.elem_freq_map = collections.Counter()
        self.freq_elem_map = collections.defaultdict(list)

    def push(self, x: int) -> None:
        self.elem_freq_map[x] += 1
        freq = self.elem_freq_map[x]
        self.max_freq = max(self.max_freq, freq)
        self.freq_elem_map[freq].append(x)
        
        
    def pop(self) -> int:
        mp = self.freq_elem_map[self.max_freq]
        res = mp.pop()
        if not mp:
            self.max_freq -= 1
        self.elem_freq_map[res] -= 1
        return res
    
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
