clock_cycles = [int(num) for num in input().split(", ")]
stop = int(input())
sum_of_cycles = 0


for index in range(len(clock_cycles)):
    sum_of_cycles += min(clock_cycles)
    if clock_cycles.index(min(clock_cycles)) == stop:
        break
    clock_cycles[clock_cycles.index(min(clock_cycles))] = 60000


print(sum_of_cycles)
