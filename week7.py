task = []

while True :
   
    task_name = input("input your task : ")
    if task_name == "exit" :
        break
    if len(task) >= 5 :
        print("only five task can be noted suscribe to premuim to continiue")
        break
    task.append({"task": task_name ,"done":False})
 
    print(task)
    print(f'number of task booked {len(task)}')
