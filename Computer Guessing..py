import random

def guess(x):
  random_number= random.randint(1,x)
  guess= 0
  
  while guess!= random_number:
   guess = int(input(f'Guess a number between 1 and {x}:'))
   if guess<random_number:
     print("Too low")
   elif guess>random_number:
     print("Too High")
    
  print(f"Correctly Guessed it is {random_number}")
    
def computer_guess(x):
 low=1
 high=x
 feedback =''
 while feedback!='c':
     if low!=high:
      guess=random.randint(low,high)
     else:
        guess=low #could be high
     feedback= input(f"Is Number {guess} (L) lower or (H) higher: ")
     if feedback =='h':
        high=guess-1
     elif feedback =='l':
        low=guess+1
 print(f"Correctly Guessed it is {guess}")
 
computer_guess(10)
