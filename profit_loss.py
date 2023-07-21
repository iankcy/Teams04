from pathlib import Path 
import csv 

#create a path for "profit_and_loss.csv" 
fp = Path("/Users/nurshuadahnoor/git/project_group2_KESI/csv_reports/profit_and_loss.csv") 
with fp.open(mode="r", encoding="latin-1", newline="") as file:
#create a "csv reader" object
     reader= csv.reader(file)

def compute_net_profit_difference(net_profit_column):
    differences = []
    highest_increment_day = None
    highest_increment_amount = 0

    for i in reader(1, len(net_profit_column)):
        #calculate the difference in net profit between the current day and the previous day
        difference = net_profit_column[i] - net_profit_column[i - 1]
        differences.append(difference)

        #check if the current difference is higher than the highest increment
        if difference > highest_increment_amount:
            highest_increment_amount = difference
            highest_increment_day = i
    
    print("Net Profit Differences:")
    for day, diff in enumerate(differences, 1):
        print(f"Day {day}: Net profit difference - ${diff}")

    print(f"\nHighest increment occurred on Day {highest_increment_day + 1}, "
          f"with an amount of ${highest_increment_amount}")
    
