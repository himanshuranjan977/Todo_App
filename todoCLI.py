import json
from datetime import date

emptyDoc = False

task_count=0 

while True:
    with open("todoDB.json", "r") as f:
        todoData = json.load(f)
    # f = open("todoDB.json", "r")
    # todoData = json.load(f)
    # print(todoData, type(todoData))

    currentDate = date.today()

    if len(todoData) == 0:
         emptyDoc = True
         username = input("\nHi there!! Welcome to TodoCLI. Please enter your username: ")
         todoData["name"] = username
         todoData["date"] = str(currentDate)

         print(f"Hey {username}! I hope you had a good start of the day, let's plan your day together\nYou can create your first task by typing create task or add task\n")
         cmd = input(">>")

         print("\nCreate a task by weriting <create task> or <add task>")
         todoData["today"] = []

         if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter scheduled time for the task: ")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
    elif "today" in list(todoData.keys()):
        # First print the existing tasks
        tasks = todoData["today"]
        username = todoData["name"]
        currDate = todoData["date"]
        print(f"Today is {date}")
        print(f"\nHey {username}, here are the tasks for your day\n")

        for task in tasks:
            print(f"\nTask number {tasks.index(task)+1}")
            print("\nTask Description: ", task["description"])
            print("\nScheduled time: ", task["scheduled_time"])

        print("\n create another task")
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\n Enter your task description: ")
            scheduled_time = input("\nEnter your scheduled time: ")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)

            print("\nTask created successfully")
            print("\nIf you want to add more task, type add task / create task")
            print("\nIf you're done for now, please type done")
        
        elif cmd == "delete all tasks":
            todoData["today"] = []
            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            print("\nTasks deleted successfully")
        elif cmd == "delete user":
            todoData = {}
            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
            print("\nUser deleted successfully")
           
        if cmd == "done" or cmd == "exit":
            print("\nHave a great day!!")
        break
    

 