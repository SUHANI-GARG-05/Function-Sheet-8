def sum_array(A):
    total = 0
    for x in A:
        total = total + x
    return total

N = int(input())
A = list(map(int, input().split()))
print(sum_array(A))
