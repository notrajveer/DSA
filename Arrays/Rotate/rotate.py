# Given an integer array nums, rotate the array to the left by one.

def rotate_left(arr): #Simpler approach using pop() function, not the general solution.
    num = arr.pop(0)
    arr.append(num)
    return arr

class Solution: #General solution
    def alt_rotate(self, arr):
       temp = arr[0]
       for i in range (1, len(arr)):
           arr[i - 1] = arr[i]
       arr[-1] = temp
    
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    print (rotate_left(arr1)) #Simpler method execution
    
    solution = Solution()
    solution.alt_rotate(arr1)
    print (arr1) #Alternate Method Execution