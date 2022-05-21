city = input().title()
sales = float(input())
comission = 0

if 0 <= sales <= 500:
    if city == 'Sofia':
        comission = sales * 0.05
    elif city == 'Plovdiv':
        comission = sales * 0.055
    elif city == 'Varna':
        comission = sales * 0.045

elif 500 < sales <= 1000:
    if city == 'Sofia':
        comission = sales * 0.07
    elif city == 'Plovdiv':
        comission = sales * 0.08
    elif city == 'Varna':
        comission = sales * 0.075

elif 1000 < sales <= 10000:
    if city == 'Sofia':
        comission = sales * 0.08
    elif city == 'Plovdiv':
        comission = sales * 0.12
    elif city == 'Varna':
        comission = sales * 0.1

elif 10000 < sales:
    if city == 'Sofia':
        comission = sales * 0.12
    elif city == 'Plovdiv':
        comission = sales * 0.145
    elif city == 'Varna':
        comission = sales * 0.13


if comission == 0:
    print('error')
else:
    print(f"{comission:.2f}")