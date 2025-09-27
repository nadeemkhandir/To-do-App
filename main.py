from todo import *

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice"))
        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            update_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            mark_done()
        elif choice == 6:
            clear_tasks()
        elif choice == 7:
            break
        else:
            print("invalid choice")
    except ValueError:
        print("Invalid choice")

    
 













