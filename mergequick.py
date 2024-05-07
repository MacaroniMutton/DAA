import sys
import random

sys.setrecursionlimit(10**6)
comp = 0
swaps = 0

def mergesort(arr, left, right):
    global comp
    if left>=right:
        return [arr[left]]
    
    mid = left + (right-left)//2
    leftArr = mergesort(arr, left, mid)
    rightArr = mergesort(arr, mid+1, right)
    mergedArr = [0] * (right-left+1)
    i = 0
    j = 0
    k = 0
    while i!=len(leftArr) or j!=len(rightArr):
        if i==len(leftArr):
            mergedArr[k] = rightArr[j]
            j += 1
        elif j==len(rightArr):
            mergedArr[k] = leftArr[i]
            i += 1
        else:
            if leftArr[i]<=rightArr[j]:
                mergedArr[k] = leftArr[i]
                i += 1
            else:
                mergedArr[k] = rightArr[j]
                j += 1
            comp += 1
        k += 1
    return mergedArr


def quicksort(arr, left, right):
    global comp, swaps
    if left>=right:
        return
    
    pivot = left
    yellow = left+1
    green = right
    while yellow<=green:
        while yellow<=right and arr[yellow]<=arr[pivot]:
            comp += 1
            yellow += 1
        while green>pivot and arr[green]>arr[pivot]:
            comp += 1
            green -= 1
        if yellow<=green:
            arr[yellow], arr[green] = arr[green], arr[yellow]
            swaps += 1
    
    arr[pivot], arr[green] = arr[green], arr[pivot]
    swaps += 1
    quicksort(arr, left, green-1)
    quicksort(arr, green+1, right)

def main():
    global comp, swaps
    r = 49
    arr = [r+(r+1)*i for i in range(10,-1,-1)]
    # random.shuffle(arr)
    while True:
        print("Before Sorting: ", end="")
        print(arr)
        print("Choose a sorting algorithm:")
        print("1. Merge Sort")
        print("2. Quick Sort")
        choice = int(input("Enter 1 or 2:"))
        if choice==1:
            comp = 0
            swaps = 0
            newarr = mergesort(arr.copy(), 0, len(arr)-1)
            print("After Merge Sort: ", newarr)
            print("No of comparisons: ", comp)
            print("No of exchanges: ", swaps)
            if input("Press y to try again:")!='y':
                break
        elif choice==2:
            comp = 0
            swaps = 0
            newarr = arr.copy()
            quicksort(newarr, 0, len(newarr)-1)
            print("After Quick Sort: ", newarr)
            print("No of comparisons: ", comp)
            print("No of exchanges: ", swaps)  
            if input("Press y to try again:")!='y':
                break
        else:
            print("Wrong Choice.")

if __name__=='__main__':
    main()