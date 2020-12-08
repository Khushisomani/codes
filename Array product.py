class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        a=[]
        s=1
        ans = [None] * len(nums)
        prod = 1
        zeros = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zeros.add(i)
        for i in range(len(nums)):
            if len(zeros) == 0:
                ans[i] = prod // nums[i]
            else:
                if i not in zeros:
                    ans[i] = 0
                elif len(zeros) == 1:
                    ans[i] = prod
                else: # if nums has multiple 0
                    ans[i] = 0
                    
        return ans
                