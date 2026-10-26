a = int(input())
b = int(input())

for num in range(a, b + 1):
    s = str(num)
    if s == s[::-1]:
        print(num)