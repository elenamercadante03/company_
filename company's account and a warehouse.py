# initial account balance
balance = 0

# warehouse dictionary
warehouse = {}

# list of recorded operations
operations = []

# display commands at start
print("Available commands:")
print("balance")
print("sale")
print("purchase")
print("account")
print("list")
print("warehouse")
print("review")
print("end")

while True:

    command = input("Enter command: ")

    if command == "end":
        break

    elif command == "balance":

        amount = float(input("Enter amount: "))
        balance += amount

        # remember operation
        operations.append(("balance", amount))

    elif command == "sale":

        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        if name in warehouse and warehouse[name] >= quantity:

            total = price * quantity
            balance += total
            warehouse[name] -= quantity

            operations.append(("sale", name, price, quantity))

        else:
            print("Not enough product in warehouse")

    elif command == "purchase":

        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        total = price * quantity

        if balance - total < 0:
            print("Not enough balance")
        else:

            balance -= total

            if name in warehouse:
                warehouse[name] += quantity
            else:
                warehouse[name] = quantity

            operations.append(("purchase", name, price, quantity))

    elif command == "account":

        print("Account balance:", balance)

    elif command == "list":

        for product in warehouse:
            print(product, warehouse[product])

    elif command == "warehouse":

        name = input("Product name: ")

        if name in warehouse:
            print(name, warehouse[name])
        else:
            print("Product not found")

    elif command == "review":

        start = input("From: ")
        end = input("To: ")

        if start == "" and end == "":
            for op in operations:
                print(op)
        else:
            start = int(start)
            end = int(end)

            for i in range(start, end):
                print(operations[i])

    else:
        print("Unknown command")

    # display commands again
    print("\nAvailable commands:")
    print("balance")
    print("sale")
    print("purchase")
    print("account")
    print("list")
    print("warehouse")
    print("review")
    print("end")
