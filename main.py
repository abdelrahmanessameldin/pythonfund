calculation_to_min = 24 * 60 
name_of_unit = "mins"
#creatd list so we could put all multi inputs in a list and the same for the output
results = []


def days_to_min(num_of_days):
             
    return (f"{num_of_days} Days are {num_of_days* calculation_to_min} {name_of_unit}")

def validate_and_execute(num_of_days_element):

    try:
        user_input_number= int(num_of_days_element)
        #conversion for postitive integers only 
        if (user_input_number) > 0:
            return days_to_min (user_input_number)
         #   print (result)
        elif user_input_number == 0:
            raise ValueError("you entered zero it is not accepted")
        else:
            raise ValueError("you entered a negative number, it is not allowed")  
    except ValueError as e:

        print(str(e))
        print ("your input is not a number , please make sure to enter the right number")

user_input = ""
while user_input != "exit" :
    user_input = input("hey user, enter a number of days to be converted to minutes !, make sure to be in a comma seprated format\n")

#list validation
    
    print (set(user_input.split(", ")))
    print(type(set(user_input.split(", "))))
#set validation
    print (user_input.split(", "))
    print(type(user_input.split(", ")))
    
    for num_of_days_element in set(user_input.split(", ")):
        result = validate_and_execute(num_of_days_element)
        '''   results.append(result)'''
        print(result)