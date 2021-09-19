class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
        if i!=len(nums1):
            ans.extend(nums1[i:])
        if j!=len(nums2):
            ans.extend(nums2[j:])
        if len(ans)%2==0:
            l=len(ans)
            return (ans[l//2]+ans[(l//2)-1])/2
        return ans[int(len(ans)//2)]