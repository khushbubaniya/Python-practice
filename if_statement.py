# check email and password are correct or not

email=input('enter your email')
password= input('enter your password')

if email=='notex@gmail.com' and password=='12345':
    print('welcome!')
    
else:
    print('incorrect cridentials!')

    
#elif statement

eml= input ('enter an email ')
psw= input('enter a password ')

if eml == 'aba@gmail.com' and psw == '1245':
    print ('welcome!')
    
elif eml== 'aba@gmail.com' and psw!= '1245':
    print('password incorrect!')
    psw = input('re-enter your password ')
    if psw== '1245':
        print('finally correct password')
    else:
        print ('stil incorrect !')
        
else:
    print('incorrect cridentials!')
    
    
# nested if-statement

eml= input ('enter an email ')
if '@' in eml:
    psw= input('enter a password ')

    if eml == 'aba@gmail.com' and psw == '1245':
        print ('welcome!')
    
    elif eml== 'aba@gmail.com' and psw!= '1245':
        print('password incorrect!')
        psw = input('re-enter your password ')
        if psw== '1245':
          print('finally correct password')
        else:
         print ('stil incorrect !')
        
    else:
        print('incorrect cridentials!')
else:
    print('email is incorrect!')
