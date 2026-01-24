# Python program to check if a given array is sorted in accending.

def is_it_sorted(arr, n):
    for i in range (0, n-1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    n = len(arr1)
    print (is_it_sorted(arr1, n))
    
#same programme can be used to to check if a given array is descending or not through minor altercations