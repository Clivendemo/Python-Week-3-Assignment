# Function that checks whether dicount is 20% or more
# If it is 20% or more then it calculates and applies the discount
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompts user to enter original price
try:
    price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percentage)

    if discount_percentage>= 20:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")
except ValueError:
    print("Please enter valid amount and discount.")