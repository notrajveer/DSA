def findmax(arr, n):
    max = arr[0]
    for i in range (1, n):
        if arr[i] > max:
            max = arr[i]
            
    return max

if __name__ == "__main__":
    arr1 = [1, 5, 7, 10]
    n = len(arr1)
    print ("The highest number in the given array is: ", findmax(arr1, n))
    