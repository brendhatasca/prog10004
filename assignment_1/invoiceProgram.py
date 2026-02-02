"""
Virtual Potion Shop - A retail invoice program.
Author: Brendha Tasca Jakubiak
Date: January 31st, 2025
"""

def printGreetMsg():
    """
    Displays a greeting message in the console.

    Returns:
        None
    """
    print("Hello, traveler! Welcome to the virtual Potion Shop!")


def getUserInfo():
    """
    Collects basic user information via console input.

    Returns:
        tuple: (user_name, phone_number, postal_code)
    """
    MESSAGE = "Please tell me your name, phone number, and postal code:"
    print(MESSAGE)
    user_name = input("Name: ")
    phone_number = input("Phone number (XXX-XXX-XXXX): ")
    postal_code = input("Postal code (A1B 2C3): ")

    return user_name, phone_number, postal_code

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
        offer = f"We have {product['name']} for ${product['price']:.2f}"
        print(offer)
        quantity = int(input("How many would you like? "))
        product['qty'] = quantity

    return products

def getUserDiscount():
    """
    Prompts the user to enter a discount percentage.

    Returns:
        float: Discount percentage entered
    """
    while True:
        discount = int(input("What is your discount? (0-100 percent) "))
        if 0 <= discount <= 100:
            return discount
        print("Please choose a number between 0 and 100.")

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

    print(f"| {'Sub Total 1':>52} | {subtotal1:>11} |")
    print(f"| {'H.S.T':>52} | {hst_amount:>11} |")
    print(f"| {'Sub Total 2':>52} | {subtotal2:>11} |")
    print(f"| {f'Discount ({discount})%':>52} | {discount_amount:>11} |")
    print(f"| {'Amount Due':>52} | {amount_due:>11} |")

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
