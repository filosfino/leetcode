class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if not candidates:
            return ret

        def find_next_smaller_value(max_candidate_index):
            while max_candidate_index>0 and candidates[max_candidate_index-1]==candidates[max_candidate_index]:
                max_candidate_index -= 1
            max_candidate_index-=1
            return max_candidate_index

        def _combinationSum(target, max_candidate_index, current_combination):
            item = candidates[max_candidate_index]
            if max_candidate_index < 0:
                return
            # use the item and return
            if target == item:
                ret.append(current_combination + [item])
                max_candidate_index = find_next_smaller_value(max_candidate_index)
                if max_candidate_index < 0:
                    return
                _combinationSum(target, max_candidate_index, current_combination)
                return
            # use the item and feed to next loop
            if target > item:
                _combinationSum(target-item, max_candidate_index-1, current_combination+[item])
            # do not use the item and feed to next loop
            max_candidate_index = find_next_smaller_value(max_candidate_index)
            if max_candidate_index < 0:
                return
            _combinationSum(target, max_candidate_index, current_combination)

        def find_max_possible_candicates(target, max_candidate_index):
            while max_candidate_index >= 0 and candidates[max_candidate_index] > target:
                max_candidate_index -= 1
            return max_candidate_index

        candidates = sorted(candidates)
        max_candidate_index = find_max_possible_candicates(target, len(candidates)-1)
        _combinationSum(target, max_candidate_index, [])
        return ret


