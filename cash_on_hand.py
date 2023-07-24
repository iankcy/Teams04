from pathlib import Path 
import csv 

fp = Path.cwd()/"csv_reports\cash_on_hand.csv"
with fp.open(mode="r", encoding="latin-1", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)

    days = []
    cashOnHand = []

    for row in reader: 
        days.append (row[0])
        cashOnHand.append (float(row[1]))
    
#def highest_COH_increment (cashOnHand):
    
def cash_on_hand(cashOnHand):

    for i in range(1, len(cashOnHand)):
      increasing = all(cashOnHand[i] > cashOnHand[i-1] for i in range (1, len(cashOnHand)))
    if increasing == True:
      print ("cash surplus")
    if increasing == False:
      print ('cash deficit')
    difference = cashOnHand[i]-cashOnHand[i-1]
    if difference > 0 :
        print("CASH SURPLUS")

print(cash_on_hand(cashOnHand))
    #print (f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: {highest_increment_amount}")
        #difference = cashOnHand[i]-cashOnHand[i-1]
        #differenceList.append(difference)
        
    #increasingCOH = all(differenceList[i]) > (differenceList[i - 1]) for i in range(1, len(differenceList))
    
    #if increasingCOH: 
        #print("CASH SURPLUS")
   
    #print (f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: {highest_increment_amount}")

  with open("summary_report.txt", "w") as summary_file:
    if all(diff >= 0 for diff in differences):
        summary_file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")

        if highest_increment_day is not None:
            day = highest_increment_day + 1  # Adding 1 to account for 0-indexed list
            summary_file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: USD {highest_increment_amount}\n")
    else:
        summary_file.write("[PROFIT DEFICIT] NET PROFIT ON SOME DAYS IS LOWER THAN PREVIOUS DAY\n")

        for day, amount in deficit_days:
            summary_file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {amount}\n")
    