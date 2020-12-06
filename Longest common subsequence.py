class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubseq(a, b):
            j=0
            for i in range(len(b)):
                if a[i]==b[j]:
                    j+=1
                    if j==len(a):
                        return False
            return True
        c = Counter(strs)
        s = sorted(c.keys(), key=len, reverse=True)
        for i in range(len(s)):
            if c[s[i]] > 1:
                continue
            else:
                for j in range(i):
                    if (isSubseq(s[i],s[j])):
                        return len(s[i])
            if i==0:
                return len(s[i])
        return -1 
            
            