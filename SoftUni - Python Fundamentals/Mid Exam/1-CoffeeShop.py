n = int(input())
total = 0

for index in range(n):
    price_capsule = float(input())
    days = int(input())
    capsules = int(input())
    orderPrice = price_capsule * days * capsules
    print(f"The price for the coffee is: ${orderPrice:.2f}")
    total += orderPrice

print(f"Total: ${total:.2f}")