# wsap two tuples in python 
tup1 = (8,10)
tup2 = (22,21)
tup1,tup2 = tup2,tup1
print (tup1)
print (tup2)

# check if all items in the tuple are the same

def check(n):
    return all (i == n[0] for i in n)


tuple1 = (13,13,13,13,13)
print(check(tuple1))

# counts the number of occurrences of item 14 from a tuple
tuple2 = (13,14,15,18,20,14,14)
print(tuple2.count(14))

# copy specific elements from one tuple to a new tuple
tuples = (8,10,7,0,7,12,15,18)
tuple3 = tuples[4:-1]
print(tuple3)