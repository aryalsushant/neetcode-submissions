class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i,x in enumerate(nums):
            chaiyeko = target - x

            if chaiyeko in hmap:
                return[hmap[chaiyeko], i]
            hmap[x]=i
        return[-1,-1]

        