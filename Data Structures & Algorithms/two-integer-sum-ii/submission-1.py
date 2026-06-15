class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        j=len(nums)-1
        while(i<j):
            total_sum=nums[i]+nums[j]
            if total_sum>target:
                j-=1
            elif total_sum<target:
                i+=1
            else:
                ans=[i+1,j+1]
                i+=1
                j-=1
        return ans