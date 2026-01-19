def second_max(arr, n):
    if n < 2:
        return -1
    
    int_max = arr[0]
    int_min = 0
    
    for i in range (1, n):
        if arr[i] > int_max:
            int_min = int_max
            int_max = arr[i]
        
        elif arr[i] < int_max and arr[i] > int_min:
            int_min = arr[i]
    return int_min

if __name__ == "__main__":
    arr1 = [1, 9.4, 3.5, 10, 7, 8.27]
    n = len(arr1)
    print ("The second highest number in the given array is: ", second_max(arr1, n))
    
# Same programme can be used with small alterations to find the second smallest value in any given array