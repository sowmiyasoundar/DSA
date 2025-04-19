class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l