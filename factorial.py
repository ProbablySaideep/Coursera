def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)

n=int(input("Enter your number: "))
print(f"Fact of {n} is: {factorial(n)}")
