while True:
    saved = 0
    destination = input()
    if destination == "End":
        break
    minimum_budget = float(input())
    while saved < minimum_budget:
        saved += float(input())
    print("Going to " + destination + "!")




