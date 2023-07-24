from pathlib import Path
import csv

# Create a path for "profit_and_loss.csv"
fp = Path.cwd() / 'profit_and_loss.csv'
with fp.open(mode="r", encoding="latin-1", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)

    empty_dict = {}
    for day, sales, trading_profit, operating_expense, net_profit in reader:
        empty_dict[day] = float(net_profit)  # Convert net_profit to float

    differences = []
    net_profit_values = list(empty_dict.values())
    for i in range(1, len(net_profit_values)):
        difference = net_profit_values[i] - net_profit_values[i - 1]
        differences.append(difference)
    
    increasing = all(abs(differences[i]) > abs(differences[i - 1]) for i in range(1, len(differences)))

# Write the results to the "summary_report.txt" file
    with open("summary_report.txt", "w") as summary_file:

     if increasing:
        print("NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")

     else:
        print("[NET PROFIT SURPLUS] NET PROFIT DOES NOT INCREASE ON EVERY DAY")
        summary_file.write("\n[NET PROFIT SURPLUS] NET PROFIT DOES NOT INCREASE ON EVERY DAY\n")

    print("All differences:", differences)
    summary_file.write(f"Day {day}: Net profit difference - ${differences}\n")

    