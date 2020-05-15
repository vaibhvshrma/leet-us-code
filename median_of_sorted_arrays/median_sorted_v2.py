class Solution:
    def upper_bound(self, arr, key, equal=True):
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo+1) // 2

            if arr[mid] < key or (equal and arr[mid] == key):
                lo = mid
            else:
                hi = mid - 1
        
        if arr[lo] > key:
            return -1
        
        return lo

    def lower_bound(self, arr, key, equal=True):
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo) // 2

            if arr[mid] > key or (equal and arr[mid] == key):
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

        # numbers required to the left for it to be a median value
        numsReqLeft = (m+n) >> 1

        # binary search for first median value in first list
        median = 0

        lo, hi = 0, m-1

        while lo <= hi:
            mid = lo + (hi-lo) // 2

            j = self.upper_bound(nums2, nums1[mid])

            if j >= 0 and nums1[mid] == nums2[j]:
                k = self.lower_bound(nums2, nums1[mid])

                if numsReqLeft - mid in range(k, j+1):
                    median += nums2[numsReqLeft - mid]
                    if (numsReqLeft - mid - 1 in range(k, j+1) 
                    or nums1[mid] == nums1[mid-1] or nums1[mid] == nums1[(mid+1)%m]):
                        return 1.0 * median
                    break

            elif j + mid + 1 == numsReqLeft:
                median += nums1[mid]
                break

            elif j + mid + 1 > numsReqLeft:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if median: # found (m+n)/2 in first array
            x = self.upper_bound(nums2, median, False)
            y = self.upper_bound(nums1, median, False)

            x = nums2[x] if x != -1 else 0
            y = nums1[y] if y != -1 else 0

            return (max(x,y) + median) / 2
        else:
            # search for (m+n)/2 in second array
            lo, hi = 0, n-1

            while lo <= hi:
                mid = lo + (hi-lo) // 2

                j = self.upper_bound(nums1, nums2[mid])

                if j >= 0 and nums2[mid] == nums1[j]:
                    k = self.lower_bound(nums1, nums2[mid])

                    if numsReqLeft - mid in range(k, j+1):
                        median += nums1[numsReqLeft - mid]
                        if (numsReqLeft - mid - 1 in range(k, j+1) 
                        or nums2[mid] == nums2[mid-1] or nums2[mid] == nums2[(mid+1)%n]):
                            return 1.0 * median
                        break

                elif j + mid + 1 == numsReqLeft:
                    median += nums2[mid]
                    break

                elif j + mid + 1 > numsReqLeft:
                    hi = mid - 1
                else:
                    lo = mid + 1
                
                x = self.upper_bound(nums2, median, False)
                y = self.upper_bound(nums1, median, False)

                x = nums2[x] if x != -1 else 0
                y = nums1[y] if y != -1 else 0

                return (max(x,y) + median) / 2



                


