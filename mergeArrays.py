
def mergeArrays(nums1, nums2):
  
  n = len(nums2)
  m = len(nums1) - len(nums2)

  while n:
    if m and nums1[m - 1] >= nums2[n - 1]:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1
  return nums1

nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]

print (mergeArrays(nums1,nums2))