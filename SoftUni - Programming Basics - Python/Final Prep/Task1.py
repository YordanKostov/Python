income = float(input())
months = int(input())
bills = float(input())
save = 0

save_per_month = income - (bills + (income * 0.3))
to_percent = (save_per_month / income) * 100
total = save_per_month * months

print(f'She can save {to_percent:.2f}')
print(total)