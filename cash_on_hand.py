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

    if surplus:
        return (surplus, (max_day, max_cash_on_hand))
    else:
        return (surplus, deficits)