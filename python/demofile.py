calculation_to_miliseconds = 24
name_of_unit = "hours"



def days_to_unit(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days is equivalent to {num_of_days * calculation_to_miliseconds} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered 0, you might want to try again " 
    else:
        return "invalid variable. please enter only positive intergers"

def validate_and_execute():
    
    try:
        user_input_value = int(num_of_days_element)
        if user_input_value > 0:
            calculated_value = days_to_unit(user_input_value)
            print(calculated_value)
    
    except ValueError:
        print ("The input is not a number, this could crash the program") 

        
user_input = ""           
while  user_input != "exit": 
    user_input = input("hey user, enter a number of days and i would transfer to hours!\n")
    list_of_days = user_input.split(",")
    print(list_of_days)
    print(set(list_of_days))
    
    print(type(set(list_of_days)))
    
    
    for num_of_days_element in set(list_of_days):
        validate_and_execute() 
