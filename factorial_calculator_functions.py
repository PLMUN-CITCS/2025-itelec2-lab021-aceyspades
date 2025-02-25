def get_non_negative_integer() -> int:
    n = int(input("Enter a non-negative integer: "))
    return n

def calculate_factorial(n: int) -> int:
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    n = get_non_negative_integer()
    result = calculate_factorial(n)
    print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()
