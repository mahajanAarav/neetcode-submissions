class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        while(min<=max):
            middle = (min+max)//2
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                min = middle + 1
            else: 
                max = middle -1
        return -1
                
            
