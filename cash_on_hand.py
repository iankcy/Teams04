from pathlib import Path
import csv

def cash_on_hand(fp):
    with open(fp,mode="r", newline="") as file:
        reader = csv.reader(file)

        next(reader)
        next(reader)
        days = []
        cash_on_hand = []
        for row in reader:
            days.append(row[0])
            cash_on_hand.append(float(row[-1]))

    max_cash_on_hand = 0
    max_day = ""
    surplus = True
    deficits = []

    for i in range(1, len(cash_on_hand)):
        difference = cash_on_hand[i] - cash_on_hand[i - 1]
        if difference < 0:
            surplus = False
            deficits.append((days[i], abs(difference)))
        else:
            if difference > max_cash_on_hand:
                max_cash_on_hand = difference
                max_day = days[i]

    file_path = Path.cwd() / 'summary_report.txt'
    file_path.touch()
    with open(file_path, "w") as summary_report:
        if surplus:
            summary_report.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            summary_report.write(f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD {max_cash_on_hand}\n")
        else:
            for day, amount in deficits:
                summary_report.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD {int(amount)}\n")