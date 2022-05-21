from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    queue.append(list(map(int, input().split())))

for i in range(n):
    petrol_total = 0
    kms_total = 0
    initial = queue.popleft()
    petrol = initial[0]
    kms = initial[1]
    if petrol < kms:
        queue.append(initial)
    else:
        queue.append(initial)
        len_queue = len(queue)
        petrol_total += petrol
        kms_total += kms
        for j in range(len_queue):
            # next_stop = queue.popleft()
            next_stop = queue[j]
            petrol_total += next_stop[0]
            kms_total += next_stop[1]
            if petrol_total < kms_total:
                # queue.append(next_stop)
                break
            else:
                if j == len_queue - 1:
                    print(i)
                    exit()
        # queue.append(initial)