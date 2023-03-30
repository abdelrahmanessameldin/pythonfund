#Days to Units
import helper
#from helper import days_and_unit_dictionary, new_user_input---> no need for helper method
#import helper as hhhh --> change module name

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    helper.validate_and_execute(days_and_unit_dictionary)
