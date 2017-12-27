class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def search(i, j):
            if target == nums[i] == nums[j]:
                return [i, j]
            if nums[i] <= target <= nums[j]:
                mid = (i+j)//2
                l = search(i, mid)
                r = search(mid+1, j)
                if -1 in l+r:
                    return max(l, r)
                else:
                    return [l[0], r[1]]
            else:
                return [-1, -1]
        return search(0, len(nums)-1)
