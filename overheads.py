from pathlib import Path
import csv

# Create a function to find the highest overhead
def find_highest_overhead():
    # Initialize variables to store the highest overhead and its category
    highest_overhead = 0
    highest_category = ""

    # Create a Path object for the "overheads.csv" file in the current working directory file
    fp = Path("C:/project_group2_KESI/csv_reports/overheads.csv")

    # Opening the csv file in the read mode with specified encoding and newline settings
    with fp.open(mode="r", encoding="latin-1", newline="") as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Skip the header row
        next(reader)

        # Loop through each row in the csv file
        for row in reader:
            try:
                # Converting the second column (index 1) to a floating-point number
                overhead_value = float(row[1])

                # Checking the category to update the highest overhead and its category
                if overhead_value > highest_overhead:
                    highest_overhead = overhead_value
                    highest_category = row[0]
            except ValueError:
                # If the overhead value cannot be converted to a float, skip the  row and continue
                continue
        # Return the highest overhead category and its value
        return highest_category, highest_overhead

# Find the highest overhead
highest_category, highest_overhead = find_highest_overhead()
print("The highest overhead category is:", highest_category)
print("The highest overhead value is: {:.2f}%".format(highest_overhead))


# Write the results to the "summary_report.txt" file
with open ("summary_report.txt", "w") as summary_file:
        # Write the formatted data to the file, including the category and overhead value in percentage.
        summary_file.write("[HIGHEST OVERHEAD] {} : {:.2f}%\n".format(highest_category, highest_overhead))