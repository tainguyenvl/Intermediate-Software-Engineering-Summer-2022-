def isValid(s):
    stack = [0]
    dic = {0:None, '(':')', '[':']', '{':'}'}
    for i in s:
        if i in dic:
          stack.append(i)
        else:
          if dic[stack.pop()] != i:
            return False
    return stack == [0]
       
          
def matchingBraces(braces):
    result = []
    for i in braces:
      if isValid(i):
        result.append('YES')
      else:
        result.append('NO')
    return result
  
braces = ['{{','{{()']
print (matchingBraces(braces))