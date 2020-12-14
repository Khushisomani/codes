class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set([()])
        for num in sorted(nums):
            subsets.update([s + (num,) for s in subsets])
        return subsets