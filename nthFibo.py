# Function to calculate the nth Fibonacci number recursively
def fibo(n):
    # Base case: if n is non-positive, return (no valid Fibonacci number)
    if n <= 0:
        return
    # Base case: if n is 1, return the first Fibonacci number (0)
    elif n == 1:
        return 0
    # Base case: if n is 2, return the second Fibonacci number (1)
    elif n == 2:
        return 1
    
    # Recursive case: return the sum of the (n-1)th and (n-2)th Fibonacci numbers
    return fibo(n - 1) + fibo(n - 2)

# Main function
def main():
    # Input the value of n
    n = int(input("Enter n: "))
    # Call the fibo function to calculate the nth Fibonacci number and print the result
    print([fibo(i) for i in range(1,n+1)])

# Entry point of the program
if __name__ == '__main__':
    main()
