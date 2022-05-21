student_ticket = 0
kids_ticket = 0
standard_ticket = 0
total_tickets = 0

while True:
    movie = input()
    if movie == "Finish":
        break
    total_places = int(input())
    tickets_for_movie = 0

    for reserve in range(total_places):
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_ticket += 1
        elif type_of_ticket == "kid":
            kids_ticket += 1
        elif type_of_ticket == "standard":
            standard_ticket += 1
        tickets_for_movie += 1
    print(f"{movie} - {(tickets_for_movie / total_places) * 100:.2f}% full.")
    total_tickets += tickets_for_movie

print(f'Total tickets: {total_tickets}')
print(f'{(student_ticket / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_ticket / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kids_ticket / total_tickets) * 100:.2f}% kids tickets.')

