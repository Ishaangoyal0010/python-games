#rock paper scissors

import random as rd
#user turn code
a=int(input('''what do you choose?
1 for rocks
2 for paper
3 for scissors\n'''))
match (a):
     case 1:
        # 1="rock"
        print("you choose rock")
        print('''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              ''')
     case 2:
        print("you choose paper")
        print("""
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
              """)
     case 3:
        print("you choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              """)
     case _:
        print("enter valid number")
#computer turn code
b=rd.randint(1,3)
match (b):
     case 1:
        print("computer choose rock")
        print('''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
           
              ''')
     case 2:
        print("computer choose paper")
        print("""
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
              """)
     case 3:
        print("computer choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              """)
     case _:
        print("enter valid number")

if(a==b):
   print("DRAW!!")
#greater than ke sath...(a+1) because 3 hoga tho loose hogaa tho islie 2 conditions needed
elif(b>a   and b==(a+1) ):
   print("COMPUTER WINS!!")
# ye exception case hai greater than ka.... kyuki isme chhoti value bade value ko deafeat kar rhi
elif(a==3 and b ==1):
   print("COMPUTER WINS!!")
elif(a>b and a==(b+1)):
   print("YOU WIN!!")
elif(b==3 and a==1):
   print("YOU WIN!!")

### match case use karte if else ki jgh tho easy padhta to write...but 5 statement or lamba hojata

