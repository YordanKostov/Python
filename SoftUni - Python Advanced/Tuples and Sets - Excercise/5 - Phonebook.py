contact = input()
dic = {}
while not contact.isdigit():
    contact = contact.split("-")
    name = contact[0]
    number = contact[1]
    if name not in dic:
        dic[name] = number
    else:
        dic[name] = number
    contact = input()

for _ in range(int(contact)):
    contact = input()
    if contact not in dic:
        print(f"Contact {contact} does not exist.")
    else:
        print(f'{contact} -> {dic[contact]}')