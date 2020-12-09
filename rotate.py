class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) < 2:
            return nums
        
        n = len(nums)
        q = k % n
        
        nums[:] = nums[n-q:] + nums[:n-q]