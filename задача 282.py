count = 0
prev = int(input())

if prev != 0:
    curr = int(input())
    while curr != 0:
        if curr > prev:
            count += 1
        prev = curr
        curr = int(input())

print(count)
