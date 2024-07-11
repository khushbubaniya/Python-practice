'''
# two add two numbers in python 
num1 = int(input("enter a first number here:"))
num2 = int(input("enter a second number her:"))
sum = (num1+num2)

print ("sum of two number is :", sum)


#python program to find sqaure root
#using exponentiation
mun1 = int(input("enter a number:"))
sr = mun1**(1/2)
print ("the sqaure root of given number is:",sr)
       

#python program to calculate the area of triangle
h = float(input("enter the height of triangle :"))
b = float(input("enter the base of triangle :"))
area = (1/2)*h*b
print("Area of triangle is :" ,area)


# swapping two variable in python
#(solution) using third variable
x = 8
y = 5

temp = x
print('the temp value is :',x)

x=y
print ('the value of x is:',x)

y=temp
print('the value of y is:',y)

#( solution ) without using third variable 
x = 10
y = 12

x,y = y,x
print (" the value of x is: ",x)
print (" the value of y is: ",y)

'''
# using Swap fuction
def swaplist (newlist):
    size  = len ( newlist)
    
    temp = newlist[0]
    newlist[0]=newlist[size - 1]
    newlist[ size - 1] = temp
    
    return newlist

newlist = [1,2,4,6,8,12]   
print(swaplist(newlist)) 
