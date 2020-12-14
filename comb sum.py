class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num = []
        x = list(itertools.combinations([1,2,3,4,5,6,7,8,9], r=k))
        for i in x:
            if sum(i) == n:
                num.append(i)
        return num
        