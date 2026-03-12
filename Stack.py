# Stack Price Analyzer using Menu

# list to store prices
prices = []

# function to add price
def add_price():
    price = int(input("Enter stock price: "))
    prices.append(price)
    print("Price added successfully!\n")


# function to show prices
def show_prices():
    if len(prices) == 0:
        print("No prices available\n")
    else:
        print("Current Stock Prices:", prices, "\n")


# function to analyze stock span using stack
def analyze_span():

    if len(prices) == 0:
        print("No prices to analyze\n")
        return

    stack = []              # stack to store indexes
    span = [0] * len(prices)

    stack.append(0)
    span[0] = 1

    for i in range(1, len(prices)):

        # remove smaller prices from stack
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    print("\nStock Span Analysis\n")

    for i in range(len(prices)):
        print("Day", i+1, "Price =", prices[i], "Span =", span[i])

    print()


# -------- Main Menu --------

while True:

    print("------ Stack Price Analyzer ------")
    print("1. Add Stock Price")
    print("2. Show Prices")
    print("3. Analyze Stock Span")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_price()

    elif choice == "2":
        show_prices()

    elif choice == "3":
        analyze_span()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice\n")