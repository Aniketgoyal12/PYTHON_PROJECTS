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
