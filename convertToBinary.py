def convertToBinary(num):
  stack = []
  result = ""
  while num != 0:
    stack.append(num % 2)
    num  = num // 2

  while stack:
    result = result + str(stack.pop())
  return result


print(convertToBinary(6))
  
      