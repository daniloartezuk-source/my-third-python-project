n = int(input())
total = 0

for _ in range(n):
    total += int(input())

average = total / n
print(f"{average:.2f}")