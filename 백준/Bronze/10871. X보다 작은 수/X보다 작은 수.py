num1, num2 = map(int, input().split())
array1 = list(map(int, input().split()))

for i in array1:
    if i < num2:
        print(i, end=' ')