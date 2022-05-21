square_meters = float(input())
total_price = square_meters * 7.61
discount = total_price * 0.18
price_with_discount = total_price - discount

print(f'The final price is: {price_with_discount:.2f} lv.\n The discount is: {discount:.2f} lv.')