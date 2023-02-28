def print_daily_report(day_number, path):
    """Given a day number & path to the deliveries, produce a report.

    Opens the deliveries file at [path], processes each line, and gerates a readable report."""
    print(f"Day {day_number}")

    # Create a file object from the string passed in as a path
    the_file = open(path)

    # Iterate over each line in the file
    for line in the_file:
        line = line.rstrip()  # Remove trailing whitespace from each line
        words = line.split('|')  # Create a list of strings

        # Assign a meaningful variable to each item from the words list
        melon, count, amount = words

        # Display information
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


# Function calls for existing reports
print_daily_report(1, "um-deliveries-day-1.txt")
print_daily_report(2, "um-deliveries-day-2.txt")
print_daily_report(3, "um-deliveries-day-3.txt")
