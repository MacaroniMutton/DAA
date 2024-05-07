import random

def selectionSort(arr):
    n = len(arr)
    c1 = 0
    c2 = 0
    for i in range(n-1):
        c1 += 1
        min = i
        for j in range(i+1,n):
            c1 += 1
            if arr[j]<arr[min]:
                min = j
                c1 += 1
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            c2 += 1
    return arr, c1, c2

def insertionSort(arr):
    n = len(arr)
    c1 = 0
    c2 = 0
    for i in range(1,n):
        c1 += 1
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            c1 += 1
            arr[j+1] = arr[j]
            c2 += 1
            j -= 1
        arr[j+1] = temp
    return arr, c1, c2

def main():
    r = 49
    arr = [r+(r+1)*i for i in range(11)]
    random.shuffle(arr)
    while True:
        print("Before Sorting: ", end="")
        print(arr)
        print("Choose a sorting algorithm:")
        print("1. Insertion Sort")
        print("2. Selection Sort")
        choice = int(input("Enter 1 or 2:"))
        if choice==1:
            newarr, c1, c2 = insertionSort(arr.copy())
            print("After Insertion Sort: ", newarr)
            print("No of comparisons: ", c1)
            print("No of exchanges: ", c2)
            if input("Press y to try again:")!='y':
                break
        elif choice==2:
            newarr, c1, c2 = selectionSort(arr.copy())
            print("After Selection Sort: ", newarr)
            print("No of comparisons: ", c1)
            print("No of exchanges: ", c2)  
            if input("Press y to try again:")!='y':
                break
        else:
            print("Wrong Choice.")

if __name__=='__main__':
    main()