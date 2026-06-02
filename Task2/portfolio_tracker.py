import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("      SMART PORTFOLIO TRACKER")
print("=" * 50)

while True:
    stock = input("\nEnter Stock Symbol (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n")
print("=" * 50)
print("PORTFOLIO SUMMARY")
print("=" * 50)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(
        f"{stock:<10} Qty: {quantity:<5} "
        f"Price: ${price:<8} Value: ${value}"
    )

print("-" * 50)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
print("-" * 50)

# Save report to CSV
with open("portfolio_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(
        ["Stock", "Quantity", "Price", "Investment Value"]
    )

    for stock, quantity in portfolio.items():
        writer.writerow(
            [
                stock,
                quantity,
                stock_prices[stock],
                stock_prices[stock] * quantity
            ]
        )

    writer.writerow([])
    writer.writerow(
        ["Total Investment", total_investment]
    )

print("\n✅ Report saved as portfolio_report.csv")
