"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random   # Python module named random

random_number = random.randint(1,20) # Generate a random number between 1 and 20
'''''''''''''
import random
def number_guess():
    random_number=random.randint(1,6)
    guess_count=1
    while guess<=5:
        guess=int(input("ENTER A NUMBER TO GUESS BETWEEN 1 TO 6"))
        if guess==random_number:
            print("HORRAY YOU GOT IT IN THE",guess_count,"TIME")
        elif guess>random_number:
            print("THE PREDICTED NUMBER IS HIGH")
        else:
            print("THE PREDICTED NUMBER IS LOW")
        
