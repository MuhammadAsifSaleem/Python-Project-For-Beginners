tasks=[]
while True:
    print("\noptions:add,view,done,exit")
    choice=input("what would you like to do?").lower()
    if choice == "add":
        task=input("enter a new task:")
        task.append(task)
    elif choice=="view":
        for i,task in enumerate(tasks):
            print(i+1,task)
    elif choice == "done":
        number = int(input("Enter task number to mark done: "))
        if 0 < number <= len(tasks):
            tasks.pop(number-1)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    elif choice == "exit":
        break
    else:
        print("Invalid choice.")
