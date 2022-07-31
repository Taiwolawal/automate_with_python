def days_to_unit(num_of_days, conversion):
    if conversion == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Enter a valid input"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered value 0, enter a valid positive number")
        else:
            print("You entered a negative number. Enter a positive number")
    except ValueError:
        print("Enter a valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()