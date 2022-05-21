first_number = int(input())
second_number = int(input())
magical_number = int(input())
check_seq = 0
found = False

for start in range(first_number, second_number + 1):
    if not found:
        for stop in range(first_number, second_number + 1):
            check_seq += 1
            if start + stop == magical_number:
                print(f'Combination N:{check_seq} ({start} + {stop} = {start + stop})')
                found = True
                break
    else:
        break
if not found:
    print(f'{check_seq} combinations - neither equals {magical_number}')