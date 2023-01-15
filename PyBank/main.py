#Dependencies
import pandas as pd
import os

#Function to convert negative number to positive number (vice versa)
def convert_sign(value):
    return value * (-1)

#File Path
file_name = "budget_data.csv"
dir = os.path.dirname(__file__)
csv_file = os.path.join(dir, "Resources", file_name)

#Read the CSV file
csv_df = pd.read_csv(csv_file)

#The total number of months included in the dataset
total_months = csv_df["Date"].count()

#The net total amount of "Profit/Losses" over the entire period
net_total = csv_df['Profit/Losses'].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#Formula: (end value - beginning value) / 85
beginning_value = csv_df['Profit/Losses'][0]
end_value = csv_df['Profit/Losses'][total_months - 1]

#2 Decimal Places
average_change = "{:.2f}".format((end_value - beginning_value) / (total_months - 1))

#The greatest increase in profits (date and amount) over the entire period
increase_value = 0
increase_index = 0

for i in range(total_months- 1):
    if convert_sign(csv_df['Profit/Losses'][i]) + csv_df["Profit/Losses"][i+1] > increase_value:
        increase_value = convert_sign(csv_df['Profit/Losses'][i]) + csv_df["Profit/Losses"][i+1]
        increase_index = csv_df['Date'][i+1]

#The greatest decrease in profits (date and amount) over the entire period
decrease_value = 0
decrease_index = 0

for i in range(total_months- 1):
    if convert_sign(csv_df['Profit/Losses'][i]) + csv_df["Profit/Losses"][i+1] < decrease_value:
        decrease_value = convert_sign(csv_df['Profit/Losses'][i]) + csv_df["Profit/Losses"][i+1]
        decrease_index = csv_df['Date'][i+1]

#Print Statement
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_index} $({increase_value})")
print(f"Greatest Decrease in Profits: {decrease_index} $({decrease_value})")

#Output to Text File
txt_filepath = os.path.join(dir,'PyBank_Results.txt')

with open(txt_filepath, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total: ${net_total}" + "\n")
    text.write(f"Average Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {increase_index} $({increase_value})" + "\n")
    text.write(f"Greatest Decrease in Profits: {decrease_index} $({decrease_value})" + "\n")

