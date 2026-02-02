print("Enter 3 integers:")
int1 = int(input())
int2 = int(input())
int3 = int(input())

intList = [int1, int2, int3]

maxNumb = 0
for num in intList:
    if num > maxNumb:
        maxNumb = num

print(f"The maximum number is {maxNumb}")