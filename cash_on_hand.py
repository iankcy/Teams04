from pathlib import Path 
import csv 

fp = Path("C:\IGP_PFB_git\project_group2_KESI\csv_reports\cash-onhand.csv")
with fp.open(mode="r", encoding="latin-1", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cashOnHand = []

    for row in reader: 
        cashOnHand.append ([row[0],row[1]])

def cash_on_hand():
    for 