from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")
# input should look like this "learn python:10.02.2033

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60)

print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")

# Enter your goal with a deadline separated by colon
# Learn python:03.08.2022
# Dear user! Time remaining for your goal: Learn python is 25 hours