def factorial(n):
    if n == 0:
      return 1
    else:
        return n * factorial(n - 1)
num = int(input("value of n:"))
result = factorial(num)
print(result)