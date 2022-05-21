sum_of_prime = 0
sum_of_nonprime = 0
while True:
    number = input()
    if number == 'stop':
        print(f'Sum of all prime numbers is: {sum_of_prime}')
        print(f'Sum of all non prime numbers is: {sum_of_nonprime}')
        break
    elif int(number) < 0:
        print("Number is negative.")
        continue
    isPrime = True
    if int(number) >= 0:
        for index in range(2, int(number)):
            if int(number) % index == 0:
                isPrime = False
                break
        if isPrime:
            sum_of_prime += int(number)
        else:
            sum_of_nonprime += int(number)
