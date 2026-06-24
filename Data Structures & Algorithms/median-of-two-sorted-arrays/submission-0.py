class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        nums1.sort()
        i=0
        j=len(nums1)-1
        while i<j:
            i+=1
            j-=1
        if i==j:
            return nums1[i]*1.0
        else:
            x=nums1[i]+nums1[j]
            x*=1.0
            return x/2