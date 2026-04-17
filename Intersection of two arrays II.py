class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    lis.append(i)
                    nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    lis.append(i)
                    nums2.remove(i)

        
        return lis
