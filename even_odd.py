import sys

if len(sys.argv) > 1:
    numbers = [int(x) for x in sys.argv[1:]]
else:
    numbers = [10, 15, 22, 33, 40, 55, 60]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers:",numbers)
print("Even Numbers Count:",even_count)
print("Odd Numbers Count:",odd_count)
