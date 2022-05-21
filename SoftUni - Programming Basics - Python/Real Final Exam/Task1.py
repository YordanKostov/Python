from math import ceil
from math import floor

students = int(input())
tasks = int(input())

normal = students * ceil(tasks * 2.8)
extra = students * floor(tasks / 3)

submissions = normal + extra
memory = 5 * ceil(submissions / 10)

print(f"{memory} KB needed")
print(f"{submissions} submissions")