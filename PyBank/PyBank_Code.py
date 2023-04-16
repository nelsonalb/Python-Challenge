import csv
import os

# Set the path for the CSV file
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
total_profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Open the CSV file
with open(file_path) as financial_data:
    csvreader = csv.reader(financial_data)

    # Read the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Calculate the total number of months included in the dataset
        total_months += 1

        # Calculate the total net amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])

        # Calculate the change in profit/loss from the previous month
        profit_loss_change = int(row[1]) - prev_profit_loss

        # Update the value of prev_profit_loss
        prev_profit_loss = int(row[1])

        # Add the profit/loss change to the total profit/loss change
        if total_months > 1:
            total_profit_loss_change += profit_loss_change

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Calculate the greatest decrease in losses (date and amount) over the entire period
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average change in "Profit/Losses" between months over the entire period
average_change = round(total_profit_loss_change / (total_months - 1), 2)

# Print the analysis to the terminal
print("-----------------------------------------------------")
print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
print("-----------------------------------------------------")

# Export a text file with the results
with open("PyBank/Analysis/Financial_Analysis.txt", "w") as analysis_file:
    analysis_file.write("----------------------------------------------------------\n")
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("----------------------------------------------------------\n")
    analysis_file.write(f"Total Months: {total_months}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change}\n")
    analysis_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    analysis_file.write("----------------------------------------------------------\n")