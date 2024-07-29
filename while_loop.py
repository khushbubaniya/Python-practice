i = 1
while i < 10:
  print(i)
  i += 1
  
# with break statement 
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1
  
# with continue statement 
i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)
  
# with else statement 
i = 1
while i < 5:
  print(i)
  i += 1
else:
  print("i is no longer less than 5")