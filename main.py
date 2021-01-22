"""
Chatbot
Author: Wyatt Mathes 
Period/Core: 7

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")

  
# start of my code
  """ 
  This function below is to have the user input there frist name and last name so that it can go to the next step to ask how there day is going.
  """ 
  
  name = input("What is your first name? ")
  name2  = input("What is your last name? ")
  # this function is a input function so that when it is done saying hello theusers name it will ask a question that the user can input on

  hows_your_day = input("Hello, Nice to meet you " + name +" "+ name2 + ", How is your day going? ")

  """
  This cobe below is to find if the ueser inputs bad to say thats not good and ask whats wrong but if the user imputs good it will say the print function under the else statement. 
  """

  if (hows_your_day == "bad" or hows_your_day == "horrible"):
    print("Thats not good!")
    bad_day = input("Whats Wrong? ")
    print("Oh thats no good, I hope it gets better.")
  
  elif(hows_your_day == "good" or hows_your_day == "great"):
    print("Thats good to hear!")
  else: 
    print("That's weird i have never heard of that!")
  
  # These two functions below are to ask the user there age and then if they are 16 or older it will say that they are old enough to drive 
  age = int(input("How old are you? "))

  if (age >= 16):
    print("Nice you are old enough to drive!! ")
  # The elif statement is to have a if statement but that will be ran after the first if is ran and it the first one is not true it will go to the elif and if its not ture it will just skip it. But if the first one is true it will not look at the elif. 
  elif(age < 16 and age >= 14):
    print("You are not old enough to drive yet but you are close")
  else: 
    print("You can't drive yet")
  
  where_from = input("Where are you from? ")

  print(" Nice I love that place, I am from Mars.")
  
  number = input("Can I guess your favorite number? ")

  if (number == "yes"):
    print("Ok, Great!")
  else: 
    print("Im going to anyways")
  
  print(random.randint(0,20))

  random_number = input("Did I get it right? ")
  if (random_number == "yes"):
    print("Nice! I got it we have to be best friends now!")
  else: 
    print("Oh thats to bad but we have to still be friends!")
  print("Now that we are best friends I'm going to go to talk to someone new thanks for being my bestfriend!!!!!!")



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()


