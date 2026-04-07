class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        lis = set(range(len(nums)+1))
      
        l = list(lis - set(nums))
        return l[0]

       
