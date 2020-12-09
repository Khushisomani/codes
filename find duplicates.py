class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
            else:
                a=abs(nums[i])
                break
        return a
        