# exe 1
# checking the higst score without using the max function

"""scores = [20, 40, 50, 67,90]
high = scores[0]
for score in scores :
    if score > high :
        high = score
print(score)
"""
# exe 2 Remove Duplicates (Week 6, using Week 7's Sets)

"""numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique = list(set(numbers))
print(unique)
"""
# exe 3 Task Manager (Week 6 Mini Project — combining lists + dictionaries)

task = []

print("wellcome to our task seter /n here is how our website works /n you would add the task you want to do and /n and set the time for the reminder /n and then you would be notified")

task_name = input('what is the task >> ')
task.append({"task":task_name,"done":False})
print(task)