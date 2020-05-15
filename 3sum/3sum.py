from typing import List

class Solution:
    @staticmethod
    def twoSum(nums, sum_req, begin):
        res = []
        need = set()
        for i in range(begin, len(nums)):
            if nums[i] in need:
                res.append([sum_req - nums[i], nums[i]])
            else:
                need.add(sum_req - nums[i])
        return res
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            sum_req = -nums[i]
            pairs = Solution.twoSum(nums, sum_req, i+1)
            for p in pairs:
                triplets.add(tuple([nums[i]] + p))

        return list(map(list, triplets))           

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(Solution().threeSum(arr))
