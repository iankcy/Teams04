import csv 
 
 
def find_highest_overhead(fp): 
    '''
    This function is to help find the highest overhead and print out the category as well as the value in percentage. 
    '''
    highest_overhead = 0 
    highest_category = "" 
    
    # To calculate the total overhead percentage 
    total_overheads = 0  
 
    # Open the CSV file for reading
    with open(fp, mode="r", newline="") as file: 
        reader = csv.reader(file) 
        next(reader) # Skip the header
        next(reader) # Skip the second line

        # Iterate through each line in the CSV file
        for category, overhead in reader: 
            overhead = float(overhead) 
            total_overheads += overhead

            # Check if the current overhead is higher than the previously recorded highest overhead
            if overhead > highest_overhead: 
                highest_overhead = overhead 
                highest_category = category 
 
    # Calculate the percentage of the highest overhead category out of the total overheads 
    highest_overhead_percentage = (highest_overhead / total_overheads) * 100 
 
    # Return the output 
    return f"[HIGHEST OVERHEAD] {highest_category}: {round(highest_overhead_percentage,2)}%"