class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minList=[0 for i in range(len(prices))]
        minList[0]=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            minList[i]=min(minList[i-1],prices[i])
            maxProfit=max(maxProfit,(prices[i]-minList[i-1]))
        return maxProfit