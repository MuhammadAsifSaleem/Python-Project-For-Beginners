print('''
This Program written by Muhammad Asif Saleem
''')
name=input("What is your name?:")
print("hello Mr/Miss",name)
score=0
question1=input("what is the capital of pakistan")
if question1.lower()=="islamabad":
    score+=1
question2=input("what is 5+7")
if question2=="12":
    score+=1
question3=input("Which planet is known as the Red Planet?")
if question3.lower()=="mars":
    score+=1
question4=input("What color do you get by mixing red and white?")
if question4.lower()=="pink":
    score+=1
question5=input("How many days are there in a week?")
if question5.lower()=="7":
    score+=1

print("your score is:",score,"/5")
