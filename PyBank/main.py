# import module
import csv

# file paths
file_to_load = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

# lists, counters, variables
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_revenue = 0

# open csv
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
# loop
    for row in reader:

        # track totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
    
        # track revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
    
        # calculate greatest inc
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
        
        # calculate greatest dec
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
        
# Calculate avg revenue change
revenue_avg = sum(revenue_change_list)/len(revenue_change_list)

# create output
output = (
    f"\nFinancial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

#print
print(output)

#export
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
