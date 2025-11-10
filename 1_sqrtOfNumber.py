def square_root(A):
    i = 1
    while i * i <= A:
        if i * i == A:
            return i
        i = i + 1
    return -1

A = int(input())
print(square_root(A))
