class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)!=0:
            a=nums[0]
            c=1
            i=1
            while i<len(nums):
                if nums[i]==a:
                    if c<2:
                        c+=1
                        i+=1
                    else:
                        nums.remove(nums[i])
                        if i<len(nums):
                            if nums[i]!=a:
                                c=1
                                a=nums[i]
                                i+=1
                            else:
                                c=2
                                a=nums[i]
                else:
                    a=nums[i]
                    c=1
                    i+=1
            return len(nums)
        else:
            return 0
            
                