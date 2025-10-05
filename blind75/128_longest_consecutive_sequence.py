class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 in nums:
                continue
            curr_count = 1

            i = 1
            while num + i in nums:
                curr_count += 1
                i += 1

            if curr_count > max_count:
                max_count = curr_count

        return max_count
