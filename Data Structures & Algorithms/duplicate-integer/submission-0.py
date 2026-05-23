class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        
        # Sorts in-place
        nums.sort()
        prev = nums[0]

        for curr in nums[1:]:
            print(f'prev={prev}, curr={curr}')
            if prev == curr:
                return True

            prev = curr


        return False
        