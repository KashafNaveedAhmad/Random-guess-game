print("hello world")
import random
my_guess= random.randint(0,10)
attempts=0
guess=None

while(my_guess!=guess):
 guess=int(input("MAKE A GUESS:"))  
 attempts=attempts +1  
 if(my_guess!=guess):
  if(my_guess>guess):
    print("TOO LOW")
  elif(my_guess< guess):
    print("TOO HIGH")
 else:
    print("CONGRATS!!")
    print("you have guessed correctly by",attempts,"attempts")
    
