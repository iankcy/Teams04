from pathlib import Path
import csv

# Create a function to find the highest overhead for the given scenario
def find_highest_overhead(scenario):
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

                # Checking the scenario and the category to update the highest overhead and its category
                if scenario == "Scenario 1":
                    if overhead_value > highest_overhead and row[0] == "Salary Expense":
                        highest_overhead = overhead_value
                        highest_category = row[0]
                elif scenario == "Scenario 2":
                    if overhead_value > highest_overhead and row[0] == "Depreciation Expense":
                        highest_overhead = overhead_value * 2 # Doubling the overhead value
                        highest_category = row[0]
            except ValueError:
                # If the overhead value cannot be converted to a float, skip the  row and continue
                continue
        # Return the highest overhead category and its value
        return highest_category, highest_overhead

# Find the highest overhead for Scenario 1
highest_category_1, highest_overhead_1 = find_highest_overhead("Scenario 1")
print("The highest overhead category in Scenario 1 is:", highest_category_1)

# Find the highest overhead for Scenario 2
highest_category_2, highest_overhead_2 = find_highest_overhead("Scenario 2")
print("The highest overhead category in Scenario 2 is:", highest_category_2)

# Create a dictionary to store the results of both scenarios
summary_data = {
    "Scenario 1": {"category": highest_category_1, "overhead": highest_overhead_1},
    "Scenario 2": {"category": highest_category_2, "overhead": highest_overhead_2}
}

# Write the results to the "summary_report.txt" file
with open ("summary_report.txt", "w") as summary_file:
    # Loop through each scenario and its data in the summary_data dictionary
    for scenario, data in summary_data.items():
        # Write the formatted data to the file, including the category and overhead value in percentage.
        summary_file.write("[HIGHEST OVERHEAD] {} : {:.2f}%\n".format(data["category"], data["overhead"]))