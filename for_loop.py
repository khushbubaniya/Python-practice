
names = ['hari','shyam','ram','krish']
for x in names:
    print (x)
    
# loop through string
for x in 'krish':
    print(x)
    
# with break statement
names = ['hari','shyam','ram','krish']
for x in names:
    print (x)
    if x== 'shyam':
        break
    
# another way 
names = ['hari','shyam','ram','krish']
for x in names:
    if x == 'hari':
        break
    print(x)
    
# with continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# the range function .range function take three value that is starting value .ending value and how many step to be done, if these valu are not given then it automatically take start as 0 and step +1
for x in range(2, 6):
  print(x)
  
# with step 
for x in range(2, 10, 2):
  print(x)
  
# else in loop 
for x in range(15):
  print(x)
else:
  print("finished!")
  
# else with break statement
for x in range(10):
  if x == 5: break
  print(x)
else:
  print("finished!")
  
# nested loops
adj = ["red", "green", "yellow"]
alphabets = ["a", "b", "c"]

for x in adj:
  for y in alphabets:
    print(x, y)
    
for x in range(0,10):
    for y in range(0,x):
       print("*",end="")
       
    print()
    