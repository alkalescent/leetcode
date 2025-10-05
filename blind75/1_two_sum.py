class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            candidate = target - num
            cand_idx = lookup.get(candidate)
            if cand_idx and cand_idx != idx:
                return [idx, lookup[candidate]]
