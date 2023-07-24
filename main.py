from overheads import find_highest_overhead
from cash_on_hand import cash_on_hand
from profit_loss import profit_and_loss
from pathlib import Path
def main():
    find_highest_overhead('./csv_reports/overheads.csv')
    cash_on_hand('./csv_reports/cash_on_hand.csv')
    profit_and_loss('./csv_reports/profit_and_loss.csv')
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    filepath=Path.cwd()/'summary_report.txt'
    filepath.touch()
    with open("summary_report.txt", "w") as new_file:
        for name in filenames:
            with open(name) as f:
                for line in f:
                    new_file.write(line)
            
                new_file.write("\n")
main()