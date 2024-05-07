# Function to solve the Tower of Hanoi problem recursively
def twh(n, source, aux, dest):
    # Base case: if there is only one disk to move, directly move it from source to destination
    if n <= 1:
        print(f"Move disk from {source} to {dest}")
        return
    
    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary peg (using destination peg as auxiliary)
    twh(n - 1, source, dest, aux)
    
    # 2. Move the largest disk from source to destination peg
    print(f"Move disk from {source} to {dest}")
    
    # 3. Move n-1 disks from auxiliary peg to destination peg (using source peg as auxiliary)
    twh(n - 1, aux, source, dest)

# Main function
def main():
    # Input the number of disks
    n = int(input("Enter number of disks: "))
    # Call the twh function to solve the Tower of Hanoi problem
    twh(n, "source", "aux", "dest")

# Entry point of the program
if __name__ == '__main__':
    main()
