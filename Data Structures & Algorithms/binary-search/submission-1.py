class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0 
        max = len(nums)-1
        while min<=max:
            middle = (max+min)//2
            if nums[middle] == target:
                return middle

            elif target>nums[middle]:
                min = middle + 1

            elif target<nums[middle]:
                max = middle - 1
        return -1