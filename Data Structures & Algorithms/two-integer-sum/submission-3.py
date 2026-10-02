class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,x in enumerate(nums):
            needed = target - x

            if needed in hmap:
                return [hmap[needed], i]
            else:
                hmap[x]=i
        return [-1,-1]
        