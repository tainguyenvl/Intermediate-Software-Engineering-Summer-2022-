def isValid(s):
    stack = [0]
    dic = {0:None, '(':')', '[':']', '{':'}'}
    for i in s:
        if i in dic:
            stack.append(i)
        else:
            if i == ')' or i == ']' or i == '}':
              if dic[stack.pop()] != i:
                  return False
    return stack == [0]


print(isValid('{[ab*1]}'))