N = int(input("Enter positive integer N: "))

numbers = []
print("Enter", N, "numbers:")
for i in range(N):
  num = int(input())
  numbers.append(num)

X = int(input("Enter integer X: "))

print(numbers.index(X) + 1 if X in numbers else -1)
