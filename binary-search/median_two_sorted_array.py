class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1)> len(nums2)):
            nums1,nums2=nums2,nums1
        total=len(nums1)+len(nums2)
        half=(total+1)//2
        left=0
        right=len(nums1)

        while left<=right:
            i=(left+right)//2
            j=half-i
            nums1left=nums1[i-1] if i>0 else float(-inf)
            nums1right=nums1[i] if i<len(nums1) else float(inf)
           
            nums2left=nums2[j-1] if j>0 else float(-inf)
            nums2right=nums2[j] if j<len(nums2) else float(inf)
            print(f'nums1left:{nums1left} nums2left:{nums2left} nums1right:{nums1right} nums2right:{nums2right} ')
            if (nums1left<=nums2right and nums2left <=nums1right):
                print("here")
                if total % 2 :
                    return max(nums1left,nums2left)
                else:
                    return (max(nums1left,nums2left)+ min(nums1right,nums2right))/2

            elif nums1left> nums2right:
                right=i-1
            elif nums2left> nums1right:
                left=i+1
        
