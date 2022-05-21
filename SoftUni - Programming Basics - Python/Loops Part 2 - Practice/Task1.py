book = input()
number = int(input())
index = 0

while index < number:
    current_book = input()
    if current_book == book:
        print(f'You checked {index} books and found it.')
        break
    index += 1

if index >= number:
    print(f"The book you search is not here!")
    print(f'You checked {index} books.')