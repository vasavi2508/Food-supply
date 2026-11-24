
# Food Supply Chain Stock Reconciliation System

# Function to calculate expected remaining stock
def calculate_remaining(received, distributed, damaged):

    remaining = received - distributed - damaged

    return remaining


# Function to calculate stock discrepancy
def calculate_discrepancy(recorded, expected):

    discrepancy = recorded - expected

    return discrepancy


# Function to calculate replenishment quantity
def calculate_replenishment(remaining, reorder_level, target_stock):

    if remaining < reorder_level:
        return target_stock - remaining

    return 0


# Main program
print("==============================================")
print("   FOOD SUPPLY CHAIN STOCK RECONCILIATION")
print("==============================================")

stock_records = []

n = int(input("Enter number of stock records: "))

if n <= 0:

    print("Please enter a valid number of records.")

else:

    # Collect stock details
    for i in range(n):

        print("\nEnter details for Record", i + 1)

        location = input("Enter location name: ")
        item = input("Enter food item name: ")

        received = int(input("Enter quantity received: "))
        distributed = int(input("Enter quantity distributed: "))
        damaged = int(input("Enter quantity damaged: "))
        recorded = int(input("Enter recorded remaining stock: "))
        reorder_level = int(input("Enter reorder level: "))
        target_stock = int(input("Enter target stock level: "))

        # Validate quantities
        if (received < 0 or distributed < 0 or damaged < 0
                or recorded < 0 or reorder_level < 0
                or target_stock < 0):

            print("Invalid input: Quantities cannot be negative.")
            continue

        if distributed + damaged > received:

            print("Invalid input: Distributed and damaged quantities")
            print("cannot exceed received quantity.")
            continue

        if target_stock < reorder_level:

            print("Invalid input: Target stock must be")
            print("greater than or equal to reorder level.")
            continue

        # Store details as a tuple
        record = (
            location,
            item,
            received,
            distributed,
            damaged,
            recorded,
            reorder_level,
            target_stock
        )

        stock_records.append(record)

    # Initialize summary variables
    total_received = 0
    total_distributed = 0
    total_damaged = 0
    total_expected = 0
    total_recorded = 0
    total_replenishment = 0
    discrepancy_count = 0

    print("\n==============================================")
    print("          STOCK RECONCILIATION REPORT")
    print("==============================================")

    # Process each stock record
    for record in stock_records:

        location = record[0]
        item = record[1]
        received = record[2]
        distributed = record[3]
        damaged = record[4]
        recorded = record[5]
        reorder_level = record[6]
        target_stock = record[7]

        # Calculate expected stock
        expected = calculate_remaining(
            received, distributed, damaged
        )

        # Calculate discrepancy
        discrepancy = calculate_discrepancy(
            recorded, expected
        )

        # Calculate replenishment
        replenishment = calculate_replenishment(
            expected, reorder_level, target_stock
        )

        # Identify stock status
        if discrepancy == 0:
            status = "Matched"
        elif discrepancy > 0:
            status = "Recorded stock higher"
        else:
            status = "Recorded stock lower"

        # Display individual report
        print("\nLocation:", location)
        print("Food Item:", item)
        print("Quantity Received:", received)
        print("Quantity Distributed:", distributed)
        print("Quantity Damaged:", damaged)
        print("Expected Remaining Stock:", expected)
        print("Recorded Remaining Stock:", recorded)
        print("Stock Discrepancy:", discrepancy)
        print("Stock Status:", status)
        print("Replenishment Required:", replenishment)

        # Update totals
        total_received += received
        total_distributed += distributed
        total_damaged += damaged
        total_expected += expected
        total_recorded += recorded
        total_replenishment += replenishment

        if discrepancy != 0:
            discrepancy_count += 1

    # Display final summary
    print("\n==============================================")
    print("              FINAL SUMMARY")
    print("==============================================")

    print("Total Records:", len(stock_records))
    print("Total Quantity Received:", total_received)
    print("Total Quantity Distributed:", total_distributed)
    print("Total Quantity Damaged:", total_damaged)
    print("Total Expected Stock:", total_expected)
    print("Total Recorded Stock:", total_recorded)
    print("Discrepancies Found:", discrepancy_count)
    print("Total Replenishment Required:", total_replenishment)

    print("\n==============================================")
    print("Stock reconciliation completed successfully.")
    print("==============================================")
