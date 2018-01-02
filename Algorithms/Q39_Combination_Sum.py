class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if not candidates:
            return ret

        def _combinationSum(target, max_candidate_index, current_combination):
            if max_candidate_index < 0:
                return
            remaining = target
            tmp = []
            while remaining > 0:
                _combinationSum(remaining, max_candidate_index-1, current_combination+tmp)
                tmp.append(candidates[max_candidate_index])
                remaining -= candidates[max_candidate_index]
            if remaining == 0:
                ret.append(current_combination + tmp)

        def find_max_possible_candicates(target, max_candidate_index):
            while max_candidate_index >= 0 and candidates[max_candidate_index] > target:
                max_candidate_index -= 1
            return max_candidate_index

        candidates = sorted(candidates)
        max_candidate_index = find_max_possible_candicates(target, len(candidates)-1)
        _combinationSum(target, max_candidate_index, [])
        return ret


