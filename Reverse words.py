class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(' '))
        front=0
        end=len(s)-1
        while front<end:
            s[front],s[end]=s[end],s[front]
            front+=1
            end-=1
        k=''
        for i in s:
            if i:
                k+=i
                k+=' '
        return k[:len(k)-1]
            
        