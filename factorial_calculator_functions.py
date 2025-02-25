def get_non_negative_integer() -> int:
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0:
                return n
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
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
