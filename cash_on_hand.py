import csv

def cash_on_hand(fp):
    '''
    This function is to find the difference in the cash on hand data and print out the days and amount in USD that have the highest increment.
    '''
    # Open the CSV file for reading
    with open(fp,mode="r", newline="") as file:
        reader = csv.reader(file)

        next(reader) # Skip the header
        next(reader) # Skip the second line
        days = []  # To store the days for cash on hand data
        cash_on_hand = [] # To store the cash on hand values for corresponding days
        # Extract data from the CSV file
        for row in reader:
            days.append(row[0])
            cash_on_hand.append(float(row[-1]))
            
    # Initialize variables to keep track of maximum cash on hand increase, corresponding day, surplus status, and deficits
    max_cash_on_hand = 0 # To store the maximum increase in cash on hand
    max_day = ""  # To store the day with the highest cash on hand increase
    surplus = True # Flag to indicate if there is a surplus of cash on hand
    deficits = []  # List to store tuples of days and corresponding deficit amounts

    # To analyse the cash on hand data to identify whether it is surplus or deficit with the following requirements
    for i in range(1, len(cash_on_hand)):
        difference = cash_on_hand[i] - cash_on_hand[i - 1]
        if difference < 0:
            surplus = False
            deficits.append((days[i], abs(difference)))
        else:
            if difference > max_cash_on_hand:
                max_cash_on_hand = difference
                max_day = days[i]

    # Return the analysis results in a tuple
    if surplus:
        return (surplus, (max_day, max_cash_on_hand))
    else:
        return (surplus, deficits)