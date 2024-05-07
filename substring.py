# Function to recursively check if a substring exists in a given string
def substringMatch(s, sub, i, answer):
    # Base case: if we have reached the end of the string, return
    if i == len(s):
        return
    
    # Extract a substring of the same length as 'sub' starting from position i
    check = s[i + 1 - len(sub):i + 1]
    
    # Check if the extracted substring is equal to the k substring 'sub'
    if check == sub:
        # If a match is found, update the answer list with True
        answer[0] = True
    
    # Recursively call substringMatch with the next index i+1
    substringMatch(s, sub, i + 1, answer)

# Main function
def main():
    # Input the main string
    s = input("Enter the main string: ")
    # Input the substring to search for
    sub = input("Enter the substring to search for: ")
    
    # Initialize a list to store the answer (True/False)
    answer = [False]
    
    # Call the substringMatch function with initial index len(sub) - 1
    substringMatch(s, sub, len(sub) - 1, answer)
    
    # Print the final answer
    print("Substring exists:", answer[0])

# Entry point of the program
if __name__ == '__main__':
    main()
