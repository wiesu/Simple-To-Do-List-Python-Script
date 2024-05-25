def loadTask():
        with open("tasks.txt", "r") as file:           
            tasks = [line.strip() for line in file]
        return tasks

def saveTask(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def addTask(tasks):
    task = input("Please enter a task: ").capitalize()
    tasks.append(task)
    saveTask(tasks)
    print(f"Task '{task}' is added.")
    
def deleteList(tasks):
    try:
        delTask = int(input("Enter the task you want to delete: "))
        if 0 < delTask <= len(tasks):
            print(f"Task '{tasks[delTask -1]}' is deleted")
            tasks.pop(delTask - 1)
            saveTask(tasks)
        elif not tasks:
            print("There are no tasks currently.")    
        else:
           print("Invalid task number.")
    except:
        print("Invalid input. Please enter a number")  
              
def listTask(tasks):
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("\nTasks to do:")
        r = 0
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
def main():
    tasks = loadTask()
    print('Welcome To-Do List')
    while True:
        print('\n')
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View task")
        print("4. Exit")

        c = input('Enter your choice: ')
        if c == "1":
            addTask(tasks)
        elif c == "2":
            deleteList(tasks)
        elif c == "3":
            listTask(tasks)

        elif c == "4":
            break
        else:
            print("Invalid input number.")

if __name__ == "__main__":
    main()