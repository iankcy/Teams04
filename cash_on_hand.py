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
      print ("[CASH SURPLUS]")
    
    
    
    
    
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
    