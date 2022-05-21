customers = [int(num) for num in input().split(", ")]
taxis = [int(num) for num in input().split(", ")]
total_time = 0

for taxi in taxis[::-1]:
    if customers[0] > taxi:
        taxis.pop()
    else:
        total_time += customers[0]
        customers.pop(0)
        taxis.pop()

if len(customers) > 0:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str,customers))}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")