

# find the length of a list in python
# using len()function
l = [ 2,4,6]
n = len(l)
print ("the length of list is :",n)


# using naive method 
li = [ 1,2,3,4,5]
print ("the list is :"+ str(li))
counter = 0
for i in li :
    counter = counter + 1
    
    
print ("the length of list using naive method is:" + str(counter))

# python code to find the length
# of list using enumerate function
list1 = [1, 4, 5, 9, 10, 5, 7, 8]
s = 0
for i, a in enumerate(list1):
    s += 1
print(s)


#python program to find the maximum of two numbers
def maximum (a,b):
    if a>= b:
        return a
    else :
        return b
    
a = 2
b = 5
print (maximum (a,b))

#using ma() function
a = 4
b = 5
maximum = max(a,b)
print ( maximum)

# using ternary operator
a = 9
b = 5
print (a if a>=b else b)
