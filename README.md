# Todo_App
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
    

 
 
 
 import json 
from datetime import date

def create_user(user_id,password):
    with open("id_password.json","r") as f:
        id_pass_data=json.load(f)
       
        id_pass_data[user_id]=password
        with open("id_password.json","r+") as f:
            f.seek(0)
            json.dump(id_pass_data,f,indent=4)
            f.close()
            
          
def old_user(username):
    while (True):
        with open(f"{username}.json","r") as f: 
            todoData = json.load(f) # we can access todoData outside the scope because it is obtained from with as..
        
        currentdate=date.today()
        if len(todoData) == 0:
            print(f"Hey there!! Welcome to TodoCli. Please Enter Your Name ")
            todoData["Name"] = username
            todoData["Date"] = str(currentdate)
            
            print(f"Hey {username}! I hope you had a good start of a day.Lets Plan our day ")
            print("\nCreate a task by writing <create task> of <add task>")
            cmd = input(">>") #taking input from the user ..
            
            todoData["Today"]=[]
            
            if cmd=="create task" or cmd=="add task":
                task_description=input("\n Enter your task description: ")
                scheduled_time=input("\n Enter scheduled time: ")
                
                task={
                    "description":task_description,
                    "scheduled_time":scheduled_time
                }
                todoData["Today"].append(task)
                
                with open(f"{username}.json","w") as f:
                    json.dump(todoData,f,indent=4) #json.dump is used to dump the data to the json file.. excpects 3 parameters..
                    
                    
        elif "Today" in list(todoData.keys()):
            #first we have to print existing task
            tasks = todoData["Today"]
            username = todoData["Name"]
            currdate=todoData["Date"]
            print(f"Today date is {currdate}")
            print(f"Hey {username}  here are the task for today ")
            for task in tasks:
                print(".........Your Tasks for Today.............")
                print(f"Task No {tasks.index(task)+1}")
                print("Task Description ",task["description"])
                print("\n scheduled at : ",task["scheduled_time"])
            
            print("\n create another task by <add task> ")
            cmd=input(">>")
            if(cmd=='create task' or cmd == 'add task'):
                task_description=input(" enter task description ")
                scheduled_time=input("enter your shchdeuled time ")
                
                task={
                    "description":task_description,
                    "scheduled_time":scheduled_time
                }
                todoData["Today"].append(task)
                
                with open(f"{username}.json","r+") as f:
                    f.seek(0)
                    json.dump(todoData,f,indent=4)
                    f.close()
                print("Task created succedssfully ")
                print("If you want to add more task type add task / create task ")
                print("If you r done click done ")
                continue
            if cmd=="done" or cmd=="exit":
                print("have a good day ")
                break
            if cmd == "delete user":
                with open(f"{username}.json", "w") as f:
                    json.dump({}, f, indent=4)
                    f.close()
            

def Authenticator(user_id,password):
    with open("id_password.json","r") as f:
        readdata=json.load(f)
        for task in readdata:
            if task==user_id and readdata[task]==password:
                return True
            else:
                return False


user_name=""       
successfull=False
is_USEr=input("Are you a new user y/n ")
if(is_USEr=='n' or is_USEr=='N'): 
    print("Please Login to continue ")
    user=input("Enter your user id ")
    password=input("Enter your password ")
    is_authentic=Authenticator(user,password)
    if(is_authentic==True):
        old_user(user)
    else:
        print("Hey please enter your login details correctly...")
elif is_USEr=='Y' or is_USEr=='y':
    print("please create a new account ")
    while True:
        name=input("please enter your name ")
        checker=False
        with open("id_password.json","r") as f:
            fileData=json.load(f)
            for task in fileData:
                if task==name:
                    checker=True
                    
            if checker==True:
                print("This name is already taken please choose a diffent name ")
                continue
            elif checker==False:
                password=input("choose a strong password ")
                with open("id_password.json","r+")as f:
                    fileData[name]=password
                    json.dump(fileData,f,indent=4)  
                    f.close()
                    user_name=name
                    print("user created successfully!! ") 
                    successfull=True
                    break             
        
if(successfull):
    with open(f"{user_name}.json","w+") as f:
        data={}
        json.dump(data,f,indent=0)
    old_user(user_name)

         
        
        
 {
    "name": "Himanshu",
    "date": "2023-01-19",
    "today": [
        {
            "description": "study",
            "scheduled_time": "1:00pm"
        },
        {
            "description": "Lunch",
            "scheduled_time": "1:30"
        }
    ]
}

{
    "Himanshu": "Abcd@1234"
}


{
    "Name": "Himanshu",
    "Date": "2023-01-19",
    "Today": [
        {
            "description": "study",
            "scheduled_time": "12:00am"
        },
        {
            "description": "travel",
            "scheduled_time": "3:30pm"
        },
        {
            "description": "Watching movies",
            "scheduled_time": "10:00pm"
        }
    ]
}
                
                
            
            
            
        
        
        
    

     
