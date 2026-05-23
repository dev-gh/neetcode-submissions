class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = dict()
        for n in nums:
            if mapping.get(n) != None:
                return True
            else:
                mapping.setdefault(n, 1)

        return False
        