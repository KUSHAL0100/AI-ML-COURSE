products = {
    "Burger": 120,
    "Pizza": 250,
    "Coke": 40,
    "Fries": 90
}

stocks = {
    "Burger": 10,
    "Pizza": 5,
    "Coke": 15,
    "Fries": 20
}

bill = {}
grand_total = 0


while True:

    print("\n------------ MENU ------------")

    for item in products:
        print(f"{item} : ₹{products[item]} | Stock : {stocks[item]}")

    print("------------------------------")

    item = input("Enter item name or done: ")
    item = item.capitalize()

    if item == "Done":
        break

    if item not in products:
        print("Item not available!!")
        continue

    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Invalid quantity!")
        continue

    if qty <= stocks[item]:

        if item in bill:
            bill[item] += qty
        else:
            bill[item] = qty

        stocks[item] -= qty

        print(f"{qty} {item} added successfully!")

    else:
        print("Insufficient stock!!")


# FINAL BILL
if bill:

    print("\n============== BILL ==============")

    for item in bill:
        price = products[item]
        qty = bill[item]
        total = price * qty
        grand_total += total

        print(f"\nItem      : {item}")
        print(f"Price     : ₹{price}")
        print(f"Quantity  : {qty}")
        print(f"Subtotal  : ₹{total}")

    gst = grand_total * 0.18
    final_amount = grand_total + gst

    print("\n----------------------------------")
    print(f"Subtotal     : ₹{grand_total}")
    print(f"GST (18%)    : ₹{gst}")
    print(f"Grand Total  : ₹{final_amount}")
    print("==================================")

else:
    print("Nothing added to bill!")