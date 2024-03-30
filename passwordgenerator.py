# #Program to generate random password
import random

password = ''
print("WELCOME TO THE PASSWORD GENRATOR")
letters = ['A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','[',']']
alp = int(input("How many alphabets you want input in your password\n"))
num = int(input("How many numbers you want input in your password\n"))
sym = int(input("How many symbols you want input in your password\n"))
for i in range(1,alp+1):
    a = random.choice(letters)
    password = password + a
for i in range(1,num+1):
    b = random.choice(numbers)
    password += b
for i in range(1,sym + 1):
    c = random.choice(symbols)
    password += c
d = list(password)
random.shuffle(d)
e = ''
for ele in d:
    e += ele
print(e)




#Same program using the string module\


import random
import string

password = ''
alphabet = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
# print(alphabet)
# print(numbers)
alp = int(input("Enter the number of alphabets\n"))
num = int(input("Enter the number of digits\n"))
sym = int(input("Enter the number of symbols\n"))
for i in range(1,alp+1):
    char = random.choice(alphabet)
    print(char)
    password = password + char
for i in range(1,num+1):
    number = random.choice(numbers)
    password += number
for i in range(1,sym+1):
    symbol = random.choice(symbols)
    password += symbol
print(password)
d = list(password)
random.shuffle(d)
e = ''
for ele in d:
    e += ele
print(e)



#Program to input the length of the password

import random
import string
password=""
alp=int(input("enter the length of password:\n"))
alphabet= string.ascii_letters+string.digits+string.punctuation
for i in range(1,alp+1):
    c=random.choice(alphabet)
    password+=c
print(password)
