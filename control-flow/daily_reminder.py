task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a high priority task. Try to schedule it soon..")
        else:
            print("Invalid priority entered. Please use either yes or no")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Note: {task} is a medium priority task that is time-bound. Plan it into your day.")
        elif time_bound == "no":
            print(f"Note: {task} is a medium priority task. Complete it when possible.")
        else:
            print("Invalid priority entered. Please use either yes or no")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Note: {task} is a low priority task with a deadline. Try not to postpone it too much.")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid priority entered. Please use either yes or no")
    case _:
        print("Invalid priority entered. Please use high, medium, or low.")
