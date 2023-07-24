from overheads import find_highest_overhead
from profit_loss import profit_and_loss
from cash_on_hand import cash_on_hand

def main():
    # Call the three functions with the appropriate file paths
    cash_on_hand('./csv_reports/cash_on_hand.csv')
    find_highest_overhead('./csv_reports/overheads.csv')
    profit_and_loss('./csv_reports/profit_and_loss.csv')

    # Read the computed data from the three files
    with open("summary_report.txt", "w") as summary_report:
        with open("./csv_reports/cash_on_hand.csv", "r") as cash_on_hand_report:
            summary_report.write(cash_on_hand_report.read() + "\n")
        
        with open("./csv_reports/overheads.csv", "r") as overheads_report:
            summary_report.write(overheads_report.read() + "\n")
        
        with open("./csv_reports/profit_and_loss.csv", "r") as profit_and_loss_report:
            summary_report.write(profit_and_loss_report.read() + "\n")

main()
