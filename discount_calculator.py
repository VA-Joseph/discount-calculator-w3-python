# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompting user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Discount applied! The final price is: {final_price}")
    else:
        print(f"No discount applied. The price remains: {final_price}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
