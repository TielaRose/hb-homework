# ***********************
# OLD CODE
# ***********************

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00


# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

# ***********************
# REFACTORED CODE
# ***********************

def print_payment_status(payment_data_filename, melon_cost=1):
    """Given a path to the orders, produce a report of discrepencies between expected and actual payment.

    Opens the customer orders file at [path], parses each line for customer name, melons ordered, and total amount paid. Compares expected payment to actual payment per customer, and prints a readable report of customers who over or underpaid"""

    # Create a file object from the string passed in as a path
    payment_data = open(payment_data_filename)

    # Iterate over each line in the file
    for line in payment_data:
        line = line.rstrip()  # Remove trailing whitespace from each line
        order = line.split('|')  # Create a list of strings

        # Assign a meaningful variable to each item from the words list
        order_id, cust_name, num_melons, amt_paid = order

        # Change the number of melons and amount paid into floats
        num_melons = float(num_melons)
        amt_paid = float(amt_paid)

        # Calculate the amount a customer should have paid (expected amount)
        expected_amt = num_melons * melon_cost

        # Compare the expected amount to the actual amount; if it differs, print that customer's information
        if expected_amt != amt_paid:
            print(
                f'{cust_name} paid ${amt_paid: .2f}, expected ${expected_amt: .2f}')

    # Close the file
    payment_data.close()


print_payment_status('customer-orders.txt')
