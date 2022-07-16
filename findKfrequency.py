'''
Element with a frequency of K
Input: [1, 2, 3, 2, 1, 2, 3, 2, 1], k = 2 
Output: 3

Input: [1, 2, 3], k = 3
Output: null 

Input: [1, 2, 2, 1, 4, 5], k = 2
Output: 1 or 2 

Input: [], k = 2 
Output: null 
'''

def findKfrequency(nums, n):
  dic = {}
  arr = []
  for i in range(len(nums)):
    if nums[i] in dic:
      dic[nums[i]] +=1
    else:
      dic[nums[i]] = 1

  for k,v in dic.items():
    if v == n:
      arr.append(k)
  return arr

print(findKfrequency([10, 2, 3, 10, 10, 1, 2, 3, 2, 1],2))