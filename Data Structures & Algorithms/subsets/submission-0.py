class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(path[:])
                return

            #decision one
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()

            #decision two
            backtrack(index+1,path)
        backtrack(0,[])
        return res
