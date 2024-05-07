import numpy as np
# Function to perform bubble sort on an array
def bubblesort(arr, n):
    # Base case: if there is only one element or none, return
    if n <= 1:
        return
    # Call helper function to bubble up the maximum element to its correct position
    bubbleMax(arr, n, 0)
    # Recursively call bubblesort with the reduced array size
    bubblesort(arr, n - 1)

# Helper function to bubble up the maximum element to its correct position
def bubbleMax(arr, n, i):
    # Base case: if we have reached the end of the array, return
    if i == n - 1:
        return
    # Swap adjacent elements if they are in the wrong order
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]   
    # Recursively call bubbleMax on the next pair of elements
    bubbleMax(arr, n, i + 1)

# Main function
def main():
    # Generate a random array of 20 integers between 1 and 100 using numpy
    arr = np.random.randint(1, 101, 20)
    print("Original array:", arr)
    
    # Call bubblesort function to sort the array
    bubblesort(arr, len(arr))
    
    # Print the sorted array
    print("Sorted array:", arr)

# Entry point of the program
if __name__ == '__main__':
    main()
