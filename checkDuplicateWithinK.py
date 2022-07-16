'''

'''

def checkDuplicateWithinK(nums, k):
  h = set()
  for i in range (len(nums)):
    if nums[i] in h:
      return True
    h.add(nums[i])

    if i >=k:
      h.remove(nums[i-k])
  return False


nums = [5,3,2,7,5,3,2,4,3,5]
print(checkDuplicateWithinK(nums,3))