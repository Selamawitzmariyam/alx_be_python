# Prompt the user for task details

# Step 1: Input task description
task = input("Enter your task: ")

# Step 2: Input task priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Step 3: Input if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Step 4: Process the task based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}'  is a high priority task"
    case "medium":
        message = f"'{task}'  is a medium priority task."
    case "low":
        message = f"'{task}'  is a low priority task"
    case _:
        message = f" '{task}' has an unknown priority level"

# Step 5: Modify the message if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"

# Step 6: Print the customized reminder
print(message)
