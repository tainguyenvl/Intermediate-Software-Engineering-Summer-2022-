

def getDecodedString(s):
  stack = []
  current_string = ""
  k = 0
    
  for char in s:
      if char == "[":
          # Just finished parsing this k, save current string and k for when we pop
          stack.append((current_string, k))
          # Reset current_string and k for this new frame
          current_string = ""
          k = 0
      elif char == "]":
          # We have completed this frame, get the last current_string and k from when the frame 
          # opened, which is the k we need to duplicate the current current_string by
          last_string, last_k = stack.pop(-1)
          current_string = last_string + last_k * current_string
      elif char.isdigit():
          k = k * 10 + int(char)
      else:
          current_string += char
  
  return current_string
    


encoded = "3[a]2[bc]"

print(getDecodedString(encoded))
