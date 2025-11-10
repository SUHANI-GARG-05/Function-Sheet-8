def print_squares(x, y):
    i = x
    while i <= y:
        print(i * i, end=" ")
        i = i + 1

x = int(input())
y = int(input())
print_squares(x, y)
