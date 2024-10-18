def pos_system():
    items = {
        "111": {"name": "A", "price": 1},
        "222": {"name": "B", "price": 2},
        "333": {"name": "C", "price": 3},
    }

    while True:
        start_new_receipt = input("Would you like to start a new receipt? (yes/no): ")
        if start_new_receipt != 'yes':
            print("Exit")
            break

        total_cost = 0
        receipt_items = []

        while True:
            barcode = input("Enter item barcode: ")
            quantity = int(input("Enter quantity: "))

            if barcode in items:
                item = items[barcode]
                item_cost = item['price'] * quantity
                total_cost = total_cost + item_cost
                receipt_items.append((item['name'], quantity, item['price'], item_cost))
            else:
                print("Item not found. Please enter a valid barcode.")

            another_item = input("Would you like to add another item? (yes/no): ")
            if another_item != 'yes':
                break

        print("\n--- Receipt ---")
        for name, quantity, price, item_cost in receipt_items:
            print(f"{name}: {quantity} x ${price:.2f} = ${item_cost:.2f}")
        print(f"Total Amount: ${total_cost:.2f}")
        print("----------------")


pos_system()