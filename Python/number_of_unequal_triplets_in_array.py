class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        i, j, k = 0, 0, 0 # These are my pointers
        len_nums = len(nums)
        triplets = 0

        # i loop
        while i < len_nums - 2:

            j = i + 1
            # j loop
            while j < len_nums - 1:

                k = j + 1
                # k loop
                while k < len_nums:
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        triplets += 1
                    k += 1
                j += 1
            i += 1

        return triplets