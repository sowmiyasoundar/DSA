class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t=0
        return [(t:=t+x)for x in nums]