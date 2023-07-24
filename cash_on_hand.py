from pathlib import Path 
import csv 

fp = Path.cwd()/"csv_reports\cash_on_hand.csv"
with fp.open(mode="r", encoding="latin-1", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cashOnHand = []

    for row in reader: 
        cashOnHand.append ([row[0],row[1]])
        
    cashOnHandData = cashOnHand[1:]
    
def highest_COH_increment (cashOnHandData):

    highest_increment_day = 0 
    highest_increment_amount = 0 
    prev_cash_on_hand = int(cashOnHand[1][1])
    increment = 0

    for data in cashOnHandData:
        day = data[0]
        cash_on_hand = int(data[1])

        for i in range(1,len(cashOnHand)):
            if cashOnHand[i]> cashOnHand[i-1]:
                print ("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        if cash_on_hand < prev_cash_on_hand:
            increment = prev_cash_on_hand - cash_on_hand
            
            if increment > highest_increment_amount:
                highest_increment_amount = increment
                highest_increment_day = day
        
        prev_cash_on_hand = cash_on_hand 
    print (f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: {highest_increment_amount}")
    


    

highest_COH_increment(cashOnHandData)
