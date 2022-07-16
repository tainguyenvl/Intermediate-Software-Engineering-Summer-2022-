def sortSubArray(arr):
  left = 0
  right = len(arr) -1

  while left < len(arr) - 1 and arr[left] <= arr[left+1]:
    left +=1

  if left == len(arr) - 1:
    return 0

  while right > 0 and arr[right] >= arr[right-1]:
    right -=1

  subarrayMax = -float('inf')
  subarrayMin = float('inf')
  for k in range(left, right):
    subarrayMax = max(subarrayMax, arr[k])
    subarrayMin = min(subarrayMin, arr[k])
    
  while left > 0 and arr[left - 1] > subarrayMin:
    left -= 1
  while right < len(arr) - 1 and arr[right+1] < subarrayMax:
    right += 1

  return right - left + 1



arr = [1, 2, 5, 3, 7, 10, 9, 12]

print(sortSubArray(arr))