'''
Intersection of Two Arrays

'''

def intersectionArr(nums1, nums2):
  return list(set(nums1) & set(nums2))



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersectionArr(nums1,nums2))