def power(A, B):
    result = 1
    i = 1
    while i <= B:
        result = result * A
        i = i + 1
    return result

A = int(input())
B = int(input())
print(power(A, B))
