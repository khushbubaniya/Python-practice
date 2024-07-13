#python program to demostrate length of strting 
# using len () fuction 
'''
str = "Apple"
print(len(str))


#using for loop 
def findlen(str):
    counter = 0
    for i in str :
        counter += 1
    return counter
    
    
str = "orange"
print (findlen(str))

# To print even length words in string 
 
#input string 
n="my name is khushbu"

s=n.split(" ") 
l=list(filter(lambda x: (len(x)%2==0),s)) 
print(l)

# using the enumerate function 
n = " I am studying math"
s = n.split(" ")
print([x for i,x in enumerate(s) if len(x)%2==0])

#how tyo remove letters from a strting in python
test_str = "iamstudyingmath"
 
# using slice + concatenation
new_str = test_str[:2] + test_str[3:]
 
print ("The string after removal of i'th character : " + new_str)
'''
#reverse words in a given string in python

def rev_sentence(sentence): 
 
    # first split the string into words 
    words = sentence.split(' ') 
 
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
 
   
    return reverse_sentence 
 
if __name__ == "__main__": 
    input = 'i am studying python'
    print (rev_sentence(input)) 
    
# python program to demostrate symmetry and palindrome of the string 
#using slicing method 

string = 'madam'
length = len (string)
hlf = length//2

f_str = string [:hlf]
s_str = string[hlf + length%2:]

if f_str == s_str :
    print(string, 'strting is symmetry')
else:
    print(string,'string is not symmetry')
    
    
if f_str == s_str[::-1]:
    ''.join(reversed(s_str)) 
    print(string, 'string is palindrome')
else:
    print(string, 'string isnot palindrome')
    