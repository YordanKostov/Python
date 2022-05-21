number = float(input())
first_conv = input()
second_conv = input()

if first_conv == "mm":
    number_mm = number
elif first_conv == "cm":
    number_mm = number * 10
else:
    number_mm = number * 1000

if second_conv == "mm":
    output_number = number_mm
elif second_conv == "cm":
    output_number = number_mm / 10
else:
    output_number = number_mm / 1000

print(f"{output_number: .3f}")