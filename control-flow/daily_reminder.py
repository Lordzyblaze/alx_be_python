# daily_reminder.py

# Prompt the user for a single task
task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

    # Process the task based on priority and time sensitivity
match priority:
    case "high":
         reminder = f"Reminder: Your task '{task}' is of high priority."
    case "medium":
         reminder = f"Reminder: Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Reminder: Your task '{task}' is of low priority."
    case _:
        reminder = "Invalid priority level entered."

    # Modify the reminder if the task is time-bound
if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    # Provide a customized reminder
print(reminder)


