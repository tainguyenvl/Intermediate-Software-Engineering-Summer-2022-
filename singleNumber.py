''''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

def singleNumber(nums):
    # Write your code here
    d = {}
    for i in nums:
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    
    for key, val in d.items():
        if val == 1:
            return key
          
  nums = [1,2,1,2,4]
  print(singleNumber(nums))