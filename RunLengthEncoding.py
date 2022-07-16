def printRLE(arr):
  i = 0
  while i < len(arr) -1:
    count  = 1
    while i < len(arr) - 1 and arr[i] == arr[i+1]:
      count += 1
      i +=1

    print(arr[i] + str(count), end ="")
    i += 1



arr = "wwwwaaadexxxxxxywww"
printRLE(arr)

