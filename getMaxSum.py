def getMaxSum(arr, k):
  left = 0
  right = 0
  sum = 0
  
  if k > len(arr):
    return -1
    
  while left <= len(arr) - k:
    right = 0
    temp = 0
    while right < k:
      temp += arr[left + right]
      right += 1
    sum = max(sum,temp)
    left += 1
  
  return sum

arr = [2,1,5,1,3,2]
k = 6
print(getMaxSum(arr, k))