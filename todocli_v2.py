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

         
        
        
        
                
                
            
            
            
        
        
        
    

     
