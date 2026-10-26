t = int(input())

cells = 1
hours = 0

while hours + 3 <= t:
    cells *= 2
    hours += 3

print(cells)
