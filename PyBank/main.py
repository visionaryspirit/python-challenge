
from pathlib import Path 
import csv

dates = []
profits_losses = []

csvpath = Path('../Instructions/PyBank/Resources/budget_data.csv')
    
with open(csvpath, 'r') as file:
    print(type(file))
    
    reader = csv.reader(file, delimiter = ',')
    print(type(reader)) 
    
    header = next(reader)
    print(f"{header}")    
    
    
    for row in reader:
        date = row[0]
        dates.append(date)
        
        pros_loss = int(row[1])
        profits_losses.append(pros_loss)
        
        
greatest_decrease_profits = 0        
greatest_increase_profits = 0
total_change = 0
count_profit_loss = 0
previous_profit_loss = profits_losses[0]
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''

for index in range(1, len(profits_losses)):
    profit_loss = profits_losses[index]
    date = dates[index]
    change = profit_loss - previous_profit_loss
    total_change += change
    previous_profit_loss = profit_loss
    count_profit_loss += 1

    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = date
    elif change < greatest_decrease: 
        greatest_decrease = change 
        greatest_decrease_date = date
    
average_change = round(total_change / count_profit_loss, 2)


header = ['Metric', 'Value']
metrics = [
    ['Total Months', len(dates)],
    ['Total', f'{sum(profits_losses)}'],
    ['Average Change', f'{average_change}'],
    ['Greatest Increase in Profits', f'{greatest_increase_date} ({greatest_increase:,})'],
    ['Greatest Decrease in Profits', f'{greatest_decrease_date} ({greatest_decrease:,})']
]

output_path = Path('financial_analysis.csv')

with open(output_path, 'w') as file: 
    writer = csv.writer(file, delimiter = ',')
    
    writer.writerow(header)
    writer.writerows(metrics)




