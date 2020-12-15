class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sum1=0
        sum2=0
        i=0
        j=len(piles)-1
        k=0
        while i<j:
            if k%2==0:
                if sum1+piles[i]>sum1+piles[j]:
                    sum1+=piles[i]
                    i+=1
                else:
                    sum1+=piles[j]
                    j-=1
            else:
                if sum2+piles[i]>sum2+piles[j]:
                    sum2+=piles[i]
                    i+=1
                else:
                    sum2+=piles[j]
                    j-=1
        if sum1>sum2:
            return True

                
        