tasks = []
def AddTask(task):
    task = input("Enter Your Task:")
    tasks.append(task)

def DisplayTask():
    print(tasks)
    return tasks

def DeleteTask():
    task_number = int(input('Enter Your Task index to delete:'))
    if 0 <= task_number < len(tasks):
        removed_tasks = tasks.pop(task_number)
        print(f'Task {removed_tasks} Deleted')

def Mark():
    completed = int(input('Enter your Task Index you have Completed:'))
    not_completed = input('Enter your Task Name you not Completed:')
    if completed < len(tasks):
        tasks[completed] = tasks[completed] + '✅'
        tasks[tasks.index(not_completed)] += '❌'
    
def Exit():
    print("Exiting.....")
def main():
    while True:
        print('\nTO-DO-LIST')
        print('1.Add Task')
        print('2.Display Task')
        print('3.Delete Task')
        print('4.Mark Tasks Completed/Not')
        print('5.Exit')

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            AddTask(tasks)
        elif choice == 2:
            DisplayTask()
        elif choice == 3:
            DeleteTask()
        elif choice == 4:
            Mark()
        else:
            print('Your Remaining List is',DisplayTask())
            Exit()
            break
main()