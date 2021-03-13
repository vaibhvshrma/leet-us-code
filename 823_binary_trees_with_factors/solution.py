class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = int(1e9+7)
        hash_set = set(arr)
        
        @cache
        def num_trees(num):
            res = 1
            for val in hash_set:
                b = num//val
                if num % val == 0 and b in hash_set:
                    res += (num_trees(val) * num_trees(b)) % MOD
            return res

        return sum(num_trees(val) for val in hash_set) % MOD
