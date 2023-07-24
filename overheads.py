from pathlib import Path
import csv


def find_highest_overhead():
    highest_overhead = 0
    highest_category = ""

    total_overheads = 0  # To calculate the total overhead percentage

    fp = Path.cwd() / 'overheads.csv'

    with fp.open(mode="r", encoding="latin-1", newline="") as file:
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

    # Generate the output
    output_str = f"[HIGHEST OVERHEAD] {highest_category}: {round(highest_overhead_percentage,2)}%"

    file_path = Path.cwd() / 'summary_file.txt'
    file_path.touch()
    with open(file_path, "w") as summary_file:
        summary_file.write(output_str + "\n")