print('''
This Program written by Muhammad Asif Saleem
Use This Symbol
+ Addition
- subtraction
* Multiplication
/ Division
''')
num1=int(input("Enter the First Num"))
num2=int(input("Enter the Second Num"))
opr=input("Enter the Operator")
if opr=='+':
    print("Sum is:",num1+num2)
elif opr=='-':
      print("Subtraction is:",num1-num2)
elif opr=='*':
      print("Multiplication is:",num1*num2)
elif opr=='/':
      print("Division is:",num1/num2)

print("Thank You")
