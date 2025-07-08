def task():
    tasks = [] #empty list
    print("____welcome to the tak management app ____")
    total_task = int(input("Enter how many tasks : "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)
    print(f"Todays tasks are \n {tasks}")
    while True:
        operation = int(input("Enter your choice\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been successfully added ")
        elif operation ==2:
            updated_val = input("Enter the taks name you want to update : ")
            if updated_val in tasks:
                up = input("Enter task : ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
                
        elif operation == 3:
            del_val = input("Which task you want to delete : ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted ...")

        elif operation == 4:
            print(f"Total tasks : {tasks}")

        elif operation == 5:
            print("Closing the program ...")
            break

        else:
            print("Invalid Operation")

task()