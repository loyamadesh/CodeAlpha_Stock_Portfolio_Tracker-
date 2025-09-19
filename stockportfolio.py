def track_portfolio():
    # Step 1: Hardcoded dictionary for stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 400, "AMZN": 170}
    total_investment = 0

    print("Welcome to your Stock Portfolio Tracker.")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    # Step 2: User input loop
    while True:
        stock_name = input("Enter a stock ticker (e.g., AAPL) or 'done' to finish: ").upper()
        if stock_name == 'DONE':
            break

        # Check if the stock is in our dictionary
        if stock_name in stock_prices:
            try:
                quantity = int(input(f"Enter the quantity of {stock_name} you own: "))
                # Step 3: Calculate and add to total
                stock_value = stock_prices[stock_name] * quantity
                total_investment += stock_value
                print(f"Current value of {stock_name}: ${stock_value}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock not found. Please enter one from the available list.")

    # Step 4: Display total investment
    print(f"\nYour total investment portfolio is worth: ${total_investment}")

    # Step 5 (Optional): Save to a file
    with open("portfolio_summary.txt", "w") as file:
        file.write(f"Total Portfolio Value: ${total_investment}")
    print("Portfolio summary saved to portfolio_summary.txt")


# ✅ Run the tracker
track_portfolio()
