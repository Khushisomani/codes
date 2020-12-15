class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s=nums.count(0)
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(len(nums)-s,len(nums)):
            nums[i]=0
        return nums