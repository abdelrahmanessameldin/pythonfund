#import datetime
from datetime import datetime

user_input = input ("enter your goal with a dead line seprated by column ! \n")
input_list = user_input.split(":")
goal= input_list[0]
deadline=input_list[1]
print(input_list)

#deadline_date = (datetime.datetime.strptime(deadline, "%d.%m.%y"))
deadline_date = (datetime.strptime(deadline, "%d.%m.%y"))

#today_date =(datetime.datetime.today())
today_date =(datetime.today())


timetill = (deadline_date-today_date)

print(f"Dear user ! time remaining for your goal : {goal} is {timetill.days} Days")

hours_till_date = (int(timetill.days * 24))
print (f"Dear user! the total unmber of hours till your deadline is : {hours_till_date} Hours ")