from overheads import find_highest_overhead
from cash_on_hand import cash_on_hand 
from profit_loss import profit_and_loss 
def main(): 
    # Extract cash on hand surplus/deficit and highest cash increment data
    cash_surplus, cash = cash_on_hand("./csv_reports/cash_on_hand.csv") 
    # Extract net profit surplus/deficit and highest net profit increment data
    net_profit_surplus, net_profit = profit_and_loss("./csv_reports/profit_and_loss.csv") 
    
    # Create a summary report text file
    with open("summary_report.txt", "w") as new_file: 
        # Write the highest overhead information into the summary report
        new_file.write(find_highest_overhead('./csv_reports/overheads.csv')) 
 
        # Check if there is a cash surplus
        if cash_surplus: 
            new_file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
            new_file.write(f"\n[HIGHESTs CASH SURPLUS] DAY: {cash[0]}, AMOUNT: USD{int(cash[1])}") 
        else: 
            # Write cash deficit information into the summary report
            for deficit in cash: 
                new_file.write(f"\n[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{int(deficit[1])}") # type: ignore 
        # Check if there is a net profit surplus
        if net_profit_surplus: 
            new_file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
            new_file.write(f"\n[HIGHEST NET PROFIT SURPLUS] DAY: {net_profit[0]}, AMOUNT: USD{int(net_profit[1])}") 
        else: 
            # Write net profit deficit information into the summary report
            for deficit in net_profit: 
                new_file.write(f"\n[PROFIT DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{int(deficit[1])}") # type: ignore 
                
# Call the main function to generate the summary report 
main()