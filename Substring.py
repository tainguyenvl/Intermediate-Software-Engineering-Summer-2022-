'''
Substring
Input: "CATDOG", "ATDO"
Output: True

Input: "CATDOG", "ATDOGE"
Output: False

EDGE CASE:
Input: "CATDOG", ""
Output: True

'''

def substring(str, substr):
  if (len(substr)) < 1:
    return True

  for i in range (len(str)):
    str_idx = i
    substr_idx = 0
    
    while substr_idx < len(substr) and str_idx < len(str) and str[str_idx] == substr[substr_idx]:
      str_idx += 1
      substr_idx += 1

    if substr_idx == len(substr):
      return True
  return False

print(substring('CATDOG','ATDO'))