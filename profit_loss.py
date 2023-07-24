from pathlib import Path 
import csv 

#create a path for "profit_and_loss.csv" 
fp = Path("C:/project_group2_KESI/csv_reports/profit_loss.csv") 
if fp.exists():
    with fp.open(mode="r", encoding="latin-1", newline="") as file:
     reader = csv.reader(file)
    next(reader)

def compute_netprofit_difference(netprofit_column):
    differences = []
    highest_increment_day = None
    highest_increment_amount = 0

    for i in range(1, len(netprofit_column)):
        #calculate the difference "-" in net profit between the current day "i"  and the previous day "1"
        difference = netprofit_column[i] - netprofit_column[i - 1]
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
    for i in range(1, len(netprofit_column)):
        if netprofit_column[i] > netprofit_column[i - 1]:
          surplus_count += 1

# Write the results to the "summary_report.txt" file
    with open("summary_report.txt", "w") as summary_file:
        summary_file.write("Net Profit Differences:\n")
    for day, diff in enumerate(differences, 1):
        summary_file.write(f"Day {day}: Net profit difference - ${diff}\n")

        summary_file.write(f"\nHighest increment occurred on Day {highest_increment_day + 1}, "
                           f"with an amount of ${highest_increment_amount}\n")

    if surplus_count == len(netprofit_column) - 1:
        summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
    else:
        summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT DOES NOT INCREASE ON EVERY DAY\n")
       