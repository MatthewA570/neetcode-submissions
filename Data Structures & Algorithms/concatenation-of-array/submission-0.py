class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = nums.copy()
        size = len(nums)
        for i in range(size):
            new_array.append(nums[i])
        return new_array



        # The initial indexes match
        # The indexes out of bounds for ORIGINAL nums array match the indexes of the original nums