print("==========================================")
print("       GIANT MANUAL FINANCE CORE          ")
print("==========================================")

print("STEP 1: INITIAL ACCOUNT BALANCES")
walletCash = float(input("Enter how much cash you have in your wallet ($): "))
bankBalance = float(input("Enter how much money is in your bank account ($): "))
savingsBalance = float(input("Enter how much money is in your emergency savings ($): "))

totalMoneyAvailable = walletCash + bankBalance + savingsBalance

print("------------------------------------------")
print("STEP 2: FIXED MONTHLY OBLIGATIONS")
rentBill = float(input("Enter your monthly rent or housing cost ($): "))
utilityBill = float(input("Enter your total electricity/water bill cost ($): "))
internetBill = float(input("Enter your phone and internet bill cost ($): "))
insuranceBill = float(input("Enter your monthly health or car insurance ($): "))

totalFixedBills = rentBill + utilityBill + internetBill + insuranceBill

print("------------------------------------------")
print("STEP 3: OUTSTANDING LOANS AND DEBTS")
creditCardDebt = float(input("Enter your total unpaid credit card balance ($): "))
studentLoanDebt = float(input("Enter your remaining student loan balance ($): "))
carLoanDebt = float(input("Enter your remaining car loan balance ($): "))

totalDebtsOwed = creditCardDebt + studentLoanDebt + carLoanDebt

print("------------------------------------------")
print("STEP 4: MANUAL VARIABLE EXPENSE LOGGING")
totalVariableSpent = 0.0
keepAddingExpenses = "yes"

while keepAddingExpenses == "yes":
    print("Your variable spending is currently: $", totalVariableSpent)
    newExpense = float(input("Enter a new individual expense amount ($): "))
    totalVariableSpent = totalVariableSpent + newExpense
    keepAddingExpenses = input("Do you have another expense to log right now? (yes/no): ")

print("------------------------------------------")
print("STEP 5: MANUAL SAVINGS GOAL CHECKER")
savingsGoalTarget = float(input("Enter a savings goal you want to reach ($): "))
monthlySavingsAmount = float(input("Enter how much cash you can save each month ($): "))

monthsRemainingToGoal = savingsGoalTarget / monthlySavingsAmount

print("------------------------------------------")
print("SYSTEM CALCULATING MASTER FINANCIAL DATA...")
print("------------------------------------------")

print("=== FINAL ACCOUNT METRICS ===")
print("Total Liquidity Assets: $", totalMoneyAvailable)
print("Total Monthly Fixed Bills: $", totalFixedBills)
print("Total Outstanding Debt Liabilities: $", totalDebtsOwed)
print("Total Variable Expenses Logged: $", totalVariableSpent)

print("------------------------------------------")
print("=== FINANCIAL HEALTH STATUS ===")

currentNetWorth = totalMoneyAvailable - totalDebtsOwed
print("Your Current Net Worth: $", currentNetWorth)

if currentNetWorth < 0:
    print("Status Warning: Your liabilities are higher than your assets.")

if currentNetWorth >= 0:
    print("Status Success: You maintain a positive net worth.")

totalMonthlyOutflow = totalFixedBills + totalVariableSpent
print("Total Overall Cash Outflow: $", totalMonthlyOutflow)

if totalMonthlyOutflow > totalMoneyAvailable:
    dangerDeficit = totalMonthlyOutflow - totalMoneyAvailable
    print("CRITICAL ALERT: Your spending exceeds available cash by: $", dangerDeficit)

if totalMonthlyOutflow <= totalMoneyAvailable:
    safeSurplus = totalMoneyAvailable - totalMonthlyOutflow
    print("SAFE POSITION: Remaining cash balance after all expenses: $", safeSurplus)

print("------------------------------------------")
print("=== FUTURE PROJECTIONS ===")
print("Target Goal: $", savingsGoalTarget)
print("Estimated months needed to fulfill your target goal: ", monthsRemainingToGoal)

print("------------------------------------------")
print("End of giant financial tracking execution.")
print("Thank you for using the dashboard tool.")
