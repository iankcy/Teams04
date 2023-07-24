from pathlib import Path 
import csv

def profit_and_loss():
    fp = Path.cwd() / 'profit_and_loss.csv'
    with fp.open(mode="r", encoding="latin-1", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)

        empty_dict = {}
        for day, sales, trading_profit, operating_expense, net_profit in reader:
            empty_dict[day] = float(net_profit)
        differences = []
        deficit_days = []
        net_profit_values = list(empty_dict.values())
        highest_increment_day = -1
        highest_increment_amount = 0

        for i in range(1, len(net_profit_values)):
            difference = net_profit_values[i] - net_profit_values[i - 1]
            differences.append(difference)

            if difference > highest_increment_amount:
                highest_increment_amount = difference
                highest_increment_day = i

            if difference < 0:
                deficit_days.append((i + 1, abs(difference)))

    file_path = Path.cwd() / 'summary_report.txt'
    file_path.touch()

    with open("summary_report.txt", "w") as summary_file:
        if all(diff >= 0 for diff in differences):
            print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
            summary_file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")

            if highest_increment_day >= 0:
                day = highest_increment_day + 1
                summary_file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: USD {highest_increment_amount}\n")
        else:
            summary_file.write("[PROFIT DEFICIT] NET PROFIT ON SOME DAYS IS LOWER THAN PREVIOUS DAY\n")

            for day, amount in deficit_days:
                summary_file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {int(amount)}")