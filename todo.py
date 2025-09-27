
# create an empty tasks list
tasks = ["task1","task2","task3"]
completed_tasks = []



# show menu
def show_menu():
    print('''
    \n --- To-Do List Menu ---\n
    ---------------------------------------------------------
    1.View Tasks
    2.Add a task
    3.update a task
    4.Delete a Task
    5.mark as done
    6.clear tasks 
    7.Exit
   ------------------------------------------------------------
''')
    

# view Tasks function
def view_tasks():
    if len(tasks) == 0:
        print("No Tasks yet! ")
    else:
        print("\n Your Pending Tasks:")
        print('-------------------------------------------------')
        for index,value in enumerate(tasks,start=1):
            print(f'{index}.{value}')

# view completed tasks function
def view_completed_tasks():
    if len(completed_tasks) == 0:
        print("No Tasks completed yet!")
    else:
        print("\n Your Tasks:")
        for index,value in enumerate(completed_tasks,start=1):
            print(f'{index}.{value} mark as completed')
# add a task function
def add_task():
    task_name = input("Enter a new task:")
    # add task to tasks list
    tasks.append(task_name)
    print(f'Task {task_name} added!')

# update task function
def update_task():
    view_tasks()
    if len(tasks) == 0:
        print("No tasks available to update!")
        return

    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            old_task = tasks[task_number - 1]
            new_task = input(f'Enter the new description for task "{old_task}": ').strip()
            
            if new_task:
                tasks[task_number - 1] = new_task
                print(f'Task {task_number} updated to: "{new_task}"')
                view_tasks()
            else:
                print("Update canceled. Task description cannot be empty.")
        else:
            print(f"Task number {task_number} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Function task marks as done
def mark_done():
    view_tasks()
    if len(tasks) == 0:
        print("No tasks availble!")
        return
    try:
        task_number = int(input("Enter task number to mark as done"))
        if task_number>=1 and task_number<=len(tasks):
            remove_task = tasks.pop(task_number-1)
            completed_tasks.append(remove_task)
            print(f'Task " {remove_task} " marked as done')
        else:
            print(f"task number {task_number} not exsists")
    except:
        print("Invalid input. Please enter a valid number.")
    
# delete a task function
def delete_task():
    view_tasks()
    if len(tasks) == 0:
        print("No tasks availble to delete!")
        return
    try:
        task_number = int(input("Enter task number to delete:"))
        if task_number>=1 and task_number<=len(tasks):
            remove_task = tasks.pop(task_number-1)
            print(f'Task " {remove_task} " deleted.')
            view_tasks()
        else:
            print(f"task number {task_number} does not exsist.")
    except:
        print("Invalid input. Please enter a valid number.")

# clear all list  function
def clear_tasks():
    completed_tasks.clear()
    tasks.clear()
    view_tasks()



    