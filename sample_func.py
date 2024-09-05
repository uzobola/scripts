
# Write a Python function that calculates the uptime percentage of a service based on the total number of hours and the number of hours the service was down. 
# The function should take 2 parameters(total hours and down hours, inputted when the function is run). 
# Lastly, the function should return the uptime percentage rounded to two decimal places. 


# Function takes 2 parameters (total hours and down hours)
def uptime_percent(total_hrs, down_hrs):
# Calculate uptime hours by minusing the num of hours down from the total hours up and put them in variables
    uptime_hrs = total_hrs - down_hrs
# Calculate percentage and put in variable
    uptime_percent = (uptime_hrs / total_hrs) * 100
    
# return uptime percentage rounded to two decimal places using round() 
# round() takes the value to be rounded and the num of places it should be rounded to
    return round(uptime_percent, 2)



# Lets test
total_hrs = float(input("Enter the total number of hours: "))
down_hrs = float(input("Enter the number of down hours: "))

result = uptime_percent(total_hrs, down_hrs)
print(result)