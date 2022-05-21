import math

income = float(input())
grade = float(input())
salary = float(input())

scholarship = grade * 25
social_scholarship = salary * 0.35

if grade >= 5.50 and income < salary:
    if social_scholarship > scholarship:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
    else:
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")

elif grade >= 5.50:
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")

elif grade > 4.50 and income < salary :
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")

else:
    print("You cannot get a scholarship!")