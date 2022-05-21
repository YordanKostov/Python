queue = int(input())
current_state = [int(x) for x in input().split()]

for index in range(1, 5):
    while current_state[index - 1] < 4 and queue > 0:
        queue -= 1
        current_state[index - 1] += 1

current_state = [str(x) for x in current_state]

if queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")
    print(' '.join(current_state))
else:
    print('The lift has empty spots!')
    print(' '.join(current_state))
