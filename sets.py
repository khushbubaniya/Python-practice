#add a list of element to a set 
sample1 = {'red','green','yellow'}
sample2 = {'black','blue','orange'}
sample1.update(sample2)
print(sample1)

# return a new set of identical items from two sets

s1 = { 12,15,18,20,22}
s2 = {18,24,26,12,15,28}
print(s1.intersection(s2))

# get only unique items from two sets from above quetion
print (s1.union(s2))

# Return a set of elements present in Set A or B, but not both...........
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))

# Check if two sets have any elements in common. If yes, display the common elements

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))