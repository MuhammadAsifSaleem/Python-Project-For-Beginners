print('''
This Program written by Muhammad Asif Saleem
''')
import random
number=random.randint(1,100)
guess=int(input("Guess a Number between 1 and 100:"))
if guess ==number:
    print("Correct!You Guessed it.")
else:
    print("wrong!The Number Was",number)
