########
# Name: Brendha Tasca Jakubiak
# Student ID: 991554242
# Date: February 5th, 2026
# Summary: A retail invoice program.
########

def printGreetMsg():
    """
    Displays a greeting message in the console.

    Returns:
        None
    """
    print("\nHello, traveler! Welcome to the virtual Potion Shop!\n")


def getUserInfo():
    """
    Collects basic user information via console input.

    Returns:
        tuple: (user_name, phone_number, postal_code)
    """
    print("Please tell me your name, phone number, and postal code:\n")
    
    while True:
        user_name = input("Name: ").strip()
        phone_number = input("Phone number (XXX-XXX-XXXX): ").strip()
        postal_code = input("Postal code (A1B 2C3): ").upper().strip()

        if user_name and phone_number and postal_code:
            # Checks if user entered an empty field
            return user_name, phone_number, postal_code
        else:
            print("\nPlease answer all fields.\n")
    

def getProducts():
    """
    Provides a collection of the Potion Shop products.

    Returns:
        dict: {
            product_id: {
                "name": str,
                "price": float
            }
        }
    """
    return {
        "cauldron": {
            "name": "Small Brewing Cauldron",
            "price": 25.00
        },
        "dragon_scales": {
            "name": "Dried Dragon Scales",
            "price": 12.50
        },
        "phoenix_feather": {
            "name": "Phoenix Feather Bundle",
            "price": 18.75
        },
        "stirring_rod": {
            "name": "Crystal Stirring Rod",
            "price": 9.99
        },
        "moonflower_petals": {
            "name": "Moonflower Petal Pouch",
            "price": 6.50
        }
    }

def collectOrder():
    """
    Presents store items one at a time with prices,
    prompts the user for desired quantities and returns the updated
    products dictionary with quantity values.

    Returns:
        dict: {
            product_id: {
                "name": str,
                "price": float,
                "qty": int
            }
        }
    """
    products = getProducts()

    for product in products.values():
        while True:
            offer = f"\nWe have {product['name']} for ${product['price']:.2f}"
            print(offer)

            quantity_str = input("How many would you like? ")

            if not quantity_str:
                # Check if user input is empty
                print("\nQuantity cannot be empty.")
                continue
            elif not quantity_str.isdigit():
                # Check if input is a digit
                print("\nQuantity must be an integer greater than 0.")
                continue
            
            quantity = int(quantity_str)

            if quantity < 0:
                print("\nQuantity must be greater than 0.")
                continue
            else:
                product['qty'] = int(quantity_str)
                break
   
    return products

def getUserDiscount():
    """
    Prompts the user to enter a discount percentage.

    Returns:
        float: Discount percentage entered
    """
    while True:
        discount_str = input("\nWhat is your discount? (0-100 percent) ")

        if not discount_str:
            print("\nDiscount cannot be empty.")
            continue
        elif not discount_str.isdigit():
            print("\nDiscount must be a number between 0-100")
            continue

        discount = int(discount_str)

        if 0 <= discount <= 100:
            return discount
        else:
            print("Please enter a number between 0 and 100.")
            continue

def calcUserSubtotal(shopping_cart):
    """
    Calculates the subtotal cost of all items in the shopping cart.

    Returns:
        float: The subtotal amount before tax and discounts.
    """
    bill_subtotal = 0
    for item in shopping_cart.values():
        price = item['price']
        qty = item['qty']
        total = price * qty
        bill_subtotal += total

    return bill_subtotal


def calcUserBill(shopping_cart, discount):
    """
    Calculates all billing amounts including tax, discount, and total.

    Returns:
        tuple: (
            subtotal_before_tax (float),
            hst_amount (float),
            subtotal_after_tax (float),
            discount_amount (float),
            amount_due (float)
        )
    """
    HST_RATE = 0.13 # Ontario HST rate

    subtotal1 = round(calcUserSubtotal(shopping_cart), 2)
    hst_amount = round(subtotal1 * HST_RATE, 2)
    subtotal2 = round(subtotal1 + hst_amount, 2)
    discount_amount = round(subtotal2 * (discount / 100), 2)
    amount_due = round(subtotal2 - discount_amount, 2)

    return subtotal1, hst_amount, subtotal2, discount_amount, amount_due

def printUserReceipt(info, shopping_cart, bill, discount):
    """
    Prints a formatted receipt showing customer information,
    purchased items, and billing totals.

    Returns:
        None
    """
    STORE_NAME = "The Potion Shop"
    STORE_ADDRESS = "4 Private Dr"
    STORE_PHONE = "905-849-0870"
    user_name, user_phone, user_postal_code = info
    (subtotal1, hst_amount, subtotal2, discount_amount, amount_due) = bill


    WIDTH = 70
    print("=" * WIDTH)
    print(f"| {STORE_NAME:^20} | Customer: {user_name:>33} |")
    print(f"| {STORE_ADDRESS:^20} | {user_phone:>43} |")
    print(f"| {STORE_PHONE:^20} | {user_postal_code:>43} |")
    print(f"| {'=' * (WIDTH - 4)} |")
    print(f"| {'PRODUCT | QUANTITY | UNIT PRICE | TOTAL PRICE |':>{WIDTH - 2}}")

    for item in shopping_cart.values():
        product = item['name']
        quantity = item['qty']
        unit_price = item['price']
        total_price = quantity * unit_price

        print(f"| {product:>28} | {quantity:^8} | {unit_price:>10.2f} | {total_price:>11.2f} |")

    print(f"| {'-' * 52} | {'-' * 11} |")

    billing_items = [
        ('Sub Total 1', f"{subtotal1:.2f}"),
        ('H.S.T', f"{hst_amount:.2f}"),
        ('Sub Total 2', f"{subtotal2:.2f}"),
        (f'Discount ({discount}%)', f"{discount_amount:.2f}"),
        ('Amount Due', f"{amount_due:.2f}")
    ]

    for label, amount in billing_items:
        print(f"| {label:>52} | {amount:>11} |")

    print(f"| {'=' * (WIDTH - 4)} |")

def main():
    printGreetMsg()

    # INPUT
    user_info = getUserInfo()
    user_shopping_cart = collectOrder()
    user_discount = getUserDiscount()

    # PROCESSING
    user_bill = calcUserBill(user_shopping_cart, user_discount)

    # OUTPUT
    printUserReceipt(user_info, user_shopping_cart, user_bill, user_discount)


if __name__ == "__main__":
    main()
