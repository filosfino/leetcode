class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        length = len(nums)
        if length <= 3:
            return ret

        nums = sorted(nums)
        # print(nums)
        self.n_sum(4, nums, target, [], ret)
        return ret

    def n_sum(self, n, nums, target, result, results):
        length = len(nums)
        # print('n_sum', n, target, result, results)
        if n > 2:
            for p in range(0, length-n+1):
                if p > 0 and nums[p] == nums[p-1]:
                    continue
                if nums[p] * n > target or nums[-1] * n < target:
                    break
                self.n_sum(n-1, nums[p+1:], target-nums[p], result+[nums[p]], results)
        elif n == 2:
            i, j = 0, length-1
            while i < j:
                # print('i: %s %s, j: %s %s' %(i, nums[i], j, nums[j]))
                t = [nums[i], nums[j]]
                s = sum(t)
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    # print('before append', n, target, result, results)
                    results.append(result + t)
                    i += 1
                    j -= 1
                    while i < j and nums[i-1] == nums[i]:
                        i += 1
                    while i < j and nums[j+1] == nums[j]:
                        j -= 1

