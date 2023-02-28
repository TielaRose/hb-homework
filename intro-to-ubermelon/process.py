# create a file object from the um-server-01.txt so we can access it in python
log_file = open("um-server-01.txt")


# Function definition
def generate_sales_reports(log_file):
    """Print sales report for Monday"""

    # get each line in 'log_file'
    for line in log_file:
        line = line.rstrip()  # remove extra whitespace to the right
        # get the first 3 characters on each line, which is the day of the week
        day = line[0:3]
        # if the day is Monday, then print that line
        if day == "Mon":
            print(line)


# call generate_sales_reports and pass it the log file from line 2
generate_sales_reports(log_file)
