class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0:
            return 0
        
        x = x if n>0 else 1/x
        n = abs(n)
        xx = x
        ans = 1
        print(list(bin(n)[2:]))
        for i in reversed(list(bin(n)[2:])):
            if i=='1': 
                ans*=xx
            xx = xx**2
        return ans
        