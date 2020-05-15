class MedianCandidate:
    def __init__(self, reqNumLeft):
        self.reqNumLeft = reqNumLeft
        self.found = False

class Solution:
    def upper_bound(self, arr, key):
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo+1) // 2

            if arr[mid] <= key:
                lo = mid
            else:
                hi = mid - 1
        
        if arr[lo] > key:
            return -1
        
        return lo

    def lower_bound(self, arr, key):
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo) // 2

            if arr[mid] >= key:
                hi = mid
            else:
                lo = mid + 1

        if arr[lo] < key:
            return -1
        
        return lo


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)

        # we will have 2 median positions if m+n is even
        twoMeds = (m+n) % 2 == 0

        numsReqLeft1 = (m+n) >> 1
        numsReqLeft2 = numsReqLeft1 - 1 if twoMeds else None

        numReq = {numsReqLeft1}
        if twoMeds:
            numReq.add(numsReqLeft2)

        # binary search for first median value in first list
        median = 0.

        lo, hi = 0, m-1

        while (lo < hi) and numReq:
            mid = lo + (hi-lo) // 2

            j = self.upper_bound(nums2, nums1[mid])

            if j >= 0 and nums1[mid] == nums2[j]:
                k = self.lower_bound(nums2, nums1[mid])

                if numsReqLeft1 - mid in range(k, j+1):
                    median += nums2[numsReqLeft1 - mid]
                    numReq.remove(numsReqLeft1)

                if twoMeds and numsReqLeft2 - mid in range(k, j+1):
                    median += nums2[numsReqLeft2 - mid]
                    numReq.remove(numsReqLeft2)

                if median:
                    break

            elif j + mid in numReq:
                median += nums1[mid]
                numReq.remove(j+mid)

            elif j + mid > numsReqLeft1:
                pass
            




                


