import csv 
 
def profit_and_loss(fp): 
    '''
    This function is to find the difference in the profit and loss data and print out the days and amount in USD that have the highest increment.
    '''
    # Open the CSV file for reading
    with open(fp,mode="r", newline="") as file: 
        reader = csv.reader(file) 
 
        next(reader) # Skip the header
        next(reader) # Skip the second line
        days = [] 
        net_profit = [] 
        # Extract data from the CSV file
        for row in reader: 
            days.append(row[0]) 
            net_profit.append(float(row[-1])) 
    
    # Initialize variables to keep track of maximum net profit increase, corresponding day, surplus status, and deficits
    max_net_profit = 0 # To store the maximum increase in net profit
    max_day = "" # To store the day with the highest net profit increase
    surplus = True  # Flag to indicate if there is a surplus of net profit
    deficits = []  # List to store tuples of days and corresponding deficit amounts
 
    # To analyse the profit and loss data to identify whether it is surplus or deficit with the following requirements
    for i in range(1, len(net_profit)): 
        difference = net_profit[i] - net_profit[i - 1] 
        if difference < 0: 
            surplus = False 
            deficits.append((days[i], abs(difference))) 
        else: 
            if difference > max_net_profit: 
                max_net_profit = difference 
                max_day = days[i] 
    
    # Return the analysis results in a tuple
    if surplus: 
        return (surplus, (max_day, max_net_profit)) 
    else: 
        return (surplus, deficits)