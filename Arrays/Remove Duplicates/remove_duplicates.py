# Function to remove duplicates from sorted array in-place

def no_dupli(arr):
    if not arr:
        return 0
    arr1 = []
    current = 0
    for i in range (len(arr)):
        if arr[i] != current:
            arr1.append(arr[i])
            current = arr[i]
    return arr1

if __name__ == "__main__":
    num = [1, 1, 3, 3, 5, 5, 7, 8]
    print (no_dupli(num))