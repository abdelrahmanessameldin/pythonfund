import datetime

# Create a datetime object representing the current date and time
now = datetime.datetime.now()

# Extract the date portion of the datetime object
date = now.date()
date2 = now.day


# Print the date as a string
print(date.strftime("%Y-%m-%d"))
print (now)
print (date2)