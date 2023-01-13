import json
from datetime import date 

emptyDoc=False

# f= open("todoDB.json","r")
task={}
while True:
    with open("todoDB.json","r") as f:
        #reading the todoDB.json
        todoData=json.load(f)
    #print(todoData)

#print(todoData)
    keys=list(todoData.keys())
    currentDate=date.today()
   
    #checking whether the user is the new user or not
    if len(todoData)==0:
        emptyDoc=True
        username=input("\nHi there!! welcome to todocli ,please enter your name")
        todoData["name"]=username
        todoData["date"]=str(currentDate)
        print(f"Hey {username}! I hope you had a good start of the day,lets plan your day together .You can create your first taks by typing create task or add task")

        cmd=input(">>")

        todoData["today"]=[]
        if cmd == "create task" or cmd=="add task":
            print("\nPlease provide about your tasks as per the cli instructions\n")
            print("\n Add time in milatiary format\n")

            #tasks discriptions as input
            task_discription =input("\nPlease enter your tasks discription:  \n")
            scheduled_time= input("\nplease enter the schedule time:   \n ")
            tasks={
                "discription":task_discription,
                "scheduled_time":scheduled_time
            }
            todoData["today"].append(tasks)
            with open("todoDB.json","w") as f:
                json.dump(todoData,f,indent=4)
                continue
        elif cmd == "break" or cmd=="close":
            break
