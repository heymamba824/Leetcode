class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        #nums1 = set(nums1)
        re = [-1] * n 
        stack = [0]
        for i in range(1,len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index1 = nums1.index(nums2[stack[-1]])
                        re[index1] = nums2[i]
                    stack.pop()
                stack.append(i)
        return re 