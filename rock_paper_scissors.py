rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

images=[rock,paper,scissors]
u_choice=int(input("Enter ur choice 0 for Rock,1 for paper and 2 for scissors\n"))
if u_choice>2 or u_choice<0:
  print("Invalid input--U lose")
else:
  print("Ur choice")
  print(images[u_choice])
  c_choice=random.randint(0,2)
  print("Computers choice")
  print(images[c_choice])
  print(f"Computer chose {c_choice}")

  if u_choice==c_choice:
     print("Its a draw")
  elif u_choice==0 and c_choice==2:
     print("U win")
  elif c_choice==0 and u_choice==2:
     print("U lose")
  elif c_choice>u_choice:
     print("U lose")
  elif u_choice>c_choice:
     print("U win")
  else:
    print("U lose")
  
