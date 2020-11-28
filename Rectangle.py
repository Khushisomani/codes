class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a1=(C-A)*(D-B)
        a2=(G-E)*(H-F)
        x=max(A,E)
        y=max(B,F)
        x1=min(C,G)
        x2=min(D,H)
        if x1>=x and x2>=y:
            a3=(x1-x)*(x2-y)
        else:
            a3=0
        return a1+a2-a3
        