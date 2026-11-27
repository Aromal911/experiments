'''To write a program to calculate the electricity bill
You are given the task of calculating the electricity bill of a house. Each house has the following
components: fan, light, washing machine, and computer. Each fan consumes 1 unit per day,
and each light consumes 0.5 units per day, the washing machine consumes 2 units per day and
each computer consumes 3 units per day.
Let the cost of 1 unit be 50 rupees. Input the number of fans, lights, washing machines, and
computers for a particular house and find the total electricity bill for that house for 2 months.
Assume a 30-day month.'''
FAN_CONSUMPTION = 1 # 1 unit per day per fan
LIGHT_CONSUMPTION = 0.5 # 0.5 units per day per light
WASHING_MACHINE_CONSUMPTION = 2 # 2 units per day per washing machine
COMPUTER_CONSUMPTION = 3 # 3 units per day per computer
COST_PER_UNIT = 50 # Cost per unit in rupees
DAYS_IN_MONTH = 30 # Number of days in a month
MONTHS = 2 # Calculate for 2 months
# Input: Number of fans, lights, washing machines, and computers
fans = int(input("Enter the number of fans: "))
lights = int(input("Enter the number of lights: "))
washing_machines = int(input("Enter the number of washing machines: "))
computers = int(input("Enter the number of computers: "))
# Calculate total daily consumption for each appliance
total_daily_consumption = (fans * FAN_CONSUMPTION +
lights * LIGHT_CONSUMPTION +
washing_machines * WASHING_MACHINE_CONSUMPTION +
computers * COMPUTER_CONSUMPTION)
# Calculate total consumption for 2 months
total_consumption = total_daily_consumption * DAYS_IN_MONTH * MONTHS
# Calculate total electricity bill
total_bill = total_consumption * COST_PER_UNIT
# Display the total electricity bill
print("The total electricity bill for 2 months is: " + str(total_bill) + " rupees.")
