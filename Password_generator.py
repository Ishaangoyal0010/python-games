## password creator

import random as rd
print("welcome to password generator!")
al=['z','q','a','w','s','x']
ig=['1','2','3','4','5','6','7','8','9','0']
sy=['&','^','%','$','#','@','!']

a=int(input("enter no. of alphabets you want-"))
b=int(input("enter no. of integers you want-"))
c=int(input("enter no. of symbols you want-"))
password=''
for i in range(0,a):
    p=rd.choice(al)
    password+=p
for j in range(0,b):
    l=rd.choice(ig)
    password+=l
for k in range(0,c):
    m=rd.choice(sy)
    password+=m
print(password)


password_pro=''
for g in range(0,len(password)):
    h=rd.choice(password)
    password_pro+=h
print(password_pro)
print("basic password=", password)
print("pro password=", password_pro)

#uper password_pro mai ye gslti hai random.choice() mai wo alphabet 4 maange hai par 6 bhi de sakta because it can repeat tho gadbad
# eg:-
#basic password= aq55^&
#pro password= qq&55q

