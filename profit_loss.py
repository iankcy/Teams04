from pathlib import Path 
import csv 

#create a path for "profit_and_loss.csv" 
fp = Path("/Users/nurshuadahnoor/git/project_group2_KESI/csv_reports/profit_and_loss.csv") 
if fp.exists():
    with fp.open(mode="r", encoding="latin-1", newline="") as file:
     reader = csv.reader(file)

def compute_net_profit_difference(net_profit_column):
    differences = []
    highest_increment_day = None
    highest_increment_amount = 0

    for i in range(1, len(net_profit_column)):
        #calculate the difference in net profit between the current day and the previous day
        difference = net_profit_column[i] - net_profit_column[i - 1]
        differences.append(difference)

        #check if the current difference is higher than the highest increment
        if difference > highest_increment_amount:
            highest_increment_amount = difference
            highest_increment_day = i

 #print the net profit difference   
    print("Net Profit Differences:")
    for day, diff in enumerate(differences, 1):
        print(f"Day {day}: Net profit difference - ${diff}")

#print the highest increment occured on the days
    print(f"\nHighest increment occurred on Day {highest_increment_day + 1}, "
          f"with an amount of ${highest_increment_amount}")
    
#check for surplus
    surplus_count = 0
    for i in range(1, len(net_profit_column)):
        if net_profit_column[i] > net_profit_column[i - 1]:
            surplus_count += 1

# Write the results to the "summary_report.txt" file
    with open("summary_report.txt", "w") as summary_file:
        summary_file.write("Net Profit Differences:\n")
        for day, diff in enumerate(differences, 1):
            summary_file.write(f"Day {day}: Net profit difference - ${diff}\n")

        summary_file.write(f"\nHighest increment occurred on Day {highest_increment_day + 1}, "
                           f"with an amount of ${highest_increment_amount}\n")

        if surplus_count == len(net_profit_column) - 1:
            summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        else:
            summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT DOES NOT INCREASE ON EVERY DAY\n")
       