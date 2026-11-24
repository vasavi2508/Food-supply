# Food-supply
# Food Supply Chain Stock Reconciliation System

## 1. Project Overview

The **Food Supply Chain Stock Reconciliation System** is a Python-based application designed to analyse and reconcile food stock quantities across multiple locations.

The system calculates expected remaining stock by comparing quantities received, distributed, and damaged. It identifies discrepancies between calculated and recorded stock and determines the replenishment quantity required at each location.

This application helps warehouses and food distribution centres maintain accurate stock records and avoid shortages.

## 2. Objectives

- To maintain food stock records across multiple locations.
- To calculate the expected remaining stock.
- To compare calculated stock with recorded stock.
- To identify stock discrepancies.
- To calculate the total quantity of damaged food items.
- To determine replenishment requirements.
- To generate a consolidated stock reconciliation report.
- To improve inventory management and reduce stock shortages.

## 3. Assumptions

1. Multiple food items can be stored across different locations.
2. Each record represents one food item at one location.
3. All quantities are entered as non-negative whole numbers.
4. Opening stock is assumed to be zero.
5. Expected remaining stock is calculated by subtracting distributed and damaged quantities from received quantities.
6. Recorded stock is compared with expected remaining stock.
7. The reorder level represents the minimum stock quantity required.
8. If expected stock falls below the reorder level, replenishment is calculated up to the target stock level.
9. Target stock must be greater than or equal to the reorder level.

## 4. Formulas Used

### Expected Remaining Stock

Expected Stock = Received Quantity − Distributed Quantity − Damaged Quantity

### Stock Discrepancy

Discrepancy = Recorded Stock − Expected Stock

- Positive value: Recorded stock is higher than expected.
- Negative value: Recorded stock is lower than expected.
- Zero: Stock records are matched.

### Replenishment Calculation

If Expected Stock is below Reorder Level:

Replenishment = Target Stock − Expected Stock

Otherwise:

Replenishment = 0

## 5. Algorithm

1. Start the program.
2. Enter the number of stock records.
3. Enter the location name.
4. Enter the food item name.
5. Enter the quantity received.
6. Enter the quantity distributed.
7. Enter the quantity damaged.
8. Enter the recorded remaining stock.
9. Enter the reorder level.
10. Enter the target stock level.
11. Validate all entered quantities.
12. Store the stock details in a tuple.
13. Calculate expected remaining stock.
14. Calculate stock discrepancy.
15. Identify whether the stock records match.
16. Calculate the replenishment quantity.
17. Repeat the process for all stock records.
18. Calculate total received, distributed, damaged, and expected stock.
19. Display discrepancies and replenishment requirements.
20. Display the final reconciliation report.
21. Stop the program.

## 6. Pseudocode

```text
START

INPUT number of stock records

FOR each record:

    INPUT location name
    INPUT food item name
    INPUT received quantity
    INPUT distributed quantity
    INPUT damaged quantity
    INPUT recorded remaining stock
    INPUT reorder level
    INPUT target stock

    VALIDATE entered quantities

    STORE details as a tuple

    expected stock =
        received - distributed - damaged

    discrepancy =
        recorded stock - expected stock

    IF discrepancy == 0:
        status = MATCHED

    ELSE IF discrepancy > 0:
        status = RECORDED STOCK HIGHER

    ELSE:
        status = RECORDED STOCK LOWER

    IF expected stock < reorder level:
        replenishment =
            target stock - expected stock

    ELSE:
        replenishment = 0

    DISPLAY stock details

    UPDATE total quantities

DISPLAY total received
DISPLAY total distributed
DISPLAY total damaged
DISPLAY total expected stock
DISPLAY total recorded stock
DISPLAY discrepancies
DISPLAY total replenishment

STOP
```

## 7. Test Cases

| Test Case | Received | Distributed | Damaged | Recorded Stock | Expected Stock |
|---|---:|---:|---:|---:|---:|
| 1 | 1000 | 650 | 20 | 330 | 330 |
| 2 | 800 | 620 | 30 | 140 | 150 |
| 3 | 300 | 180 | 5 | 120 | 115 |
| 4 | 500 | 300 | 10 | 190 | 190 |

### Test Case Explanation

**Test Case 1: Matching Stock**

- Received: 1000
- Distributed: 650
- Damaged: 20
- Expected stock: 330
- Recorded stock: 330
- Result: No discrepancy.

**Test Case 2: Recorded Stock Lower**

- Received: 800
- Distributed: 620
- Damaged: 30
- Expected stock: 150
- Recorded stock: 140
- Result: Discrepancy of -10 units.

**Test Case 3: Recorded Stock Higher**

- Received: 300
- Distributed: 180
- Damaged: 5
- Expected stock: 115
- Recorded stock: 120
- Result: Discrepancy of +5 units.

**Test Case 4: Matching Stock**

- Received: 500
- Distributed: 300
- Damaged: 10
- Expected stock: 190
- Recorded stock: 190
- Result: No discrepancy.

## 8. Sample Output

```text
==============================================
          FINAL SUMMARY
==============================================

Total Records: 4
Total Quantity Received: 2600
Total Quantity Distributed: 1750
Total Quantity Damaged: 65
Total Expected Stock: 785
Total Recorded Stock: 780
Discrepancies Found: 2
Total Replenishment Required: 530

==============================================
Stock reconciliation completed successfully.
==============================================
```

## 9. Python Concepts Used

- Variables and data types
- Input and output statements
- Tuples
- Lists
- Conditional statements (if, elif, else)
- For loops
- Functions
- Function arguments and return values
- Arithmetic operators
- Logical operators
- Tuple indexing
- List operations

## 10. Conclusion

The Food Supply Chain Stock Reconciliation System successfully analyses food stock quantities across multiple locations.

It calculates remaining stock, identifies discrepancies between recorded and expected quantities, and determines replenishment requirements.

This project demonstrates the practical application of Python concepts such as tuples, lists, functions, loops, and conditional statements in solving real-world inventory management problems.

## 11. Project Structure

```text
Food-Supply-Chain-Reconciliation/
│
├── food_stock_reconciliation.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 12. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `food_stock_reconciliation.py`.
4. Run the program using:

```bash
python food_stock_reconciliation.py
```

5. Enter the number of stock records.
6. Enter food item and location details.
7. View the stock reconciliation report.
8. Check discrepancies and replenishment quantities.
9. Capture the actual program output screenshot.
10. Upload the Python file, README, and screenshot to GitHub.

## 13. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Food supply
