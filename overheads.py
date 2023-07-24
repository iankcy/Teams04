from pathlib import Path
import csv


def find_highest_overhead(fp):
    highest_overhead = 0
    highest_category = ""

    total_overheads = 0  # To calculate the total overhead percentage

    with open(fp, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)

        for category, overhead in reader:
            overhead = float(overhead)
            total_overheads += overhead

            if overhead > highest_overhead:
                highest_overhead = overhead
                highest_category = category

    # Calculate the percentage of the highest overhead category out of the total overheads
    highest_overhead_percentage = (highest_overhead / total_overheads) * 100

    # return the output
    return f"[HIGHEST OVERHEAD] {highest_category}: {round(highest_overhead_percentage,2)}%"