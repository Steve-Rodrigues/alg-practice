##bubble sort implementation
import random 

def bubble_sort(arr):
    n = len(arr)
    print('Starting list: ', arr)
    ##outer loop goes to n in case we need to fix 'n' times (wors case)
    for i in range(n):
        print(f'*******************Pass number {i} out of {n} possible passes')
        swap = False
        ##inner loop goes from 0 to n-1-i since we don't need last element and subtract i because thats already sorted(number of sorts so far--no need to check those later elements)
        for j in range(n-1-i):
            if (arr[j]>arr[j+1]):
                print(f'Swapped {arr[j]} and {arr[j+1]}')
                ##swap if prev is greater than next element
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swap = True
            else:
                continue
        ##if entire iteration results in 0 swaps it is fully sorted because it works from small to big
        print(f'Current list order: {arr}')
        if (swap==False):
            break
    return arr

##array = [random.randint(1,20) for i in range(10)]
##print(bubble_sort(array))

##selection sort implementation
def selection_sort(arr):
    print(f'Starting array: {arr}')
    n = len(arr)
    ##outer loop runs n passes to make sure very element gets sorted
    ##every pass will sort an element to the left hand side. i is the number of elements sorted on the left 
    for i in range(n):
        ##set min index = i since thats the checker
        min_index = i
        ##inner loops from i+1 to n so it skips over i and the sorted half of the array
        for j in range(i+1,n):
            ##condition checking for minindex
            if arr[j] < arr[min_index]:
                min_index = j
        ##swaps the single lowest val from unsorted side onto the ith posiiton to extend sorted section
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr
##array = [random.randint(1,25) for i in range(10)]
##print(selection_sort(array))

##Insertion sort implementation
def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        print(f'Sorted portion ends at index {i}\nCurrent array is (sorted):{arr[0:i]}********(unsorted):{arr[i:]}')
        j=i
        while (arr[j]<arr[j-1]) and (j>0):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr
array = [random.randint(1,25) for i in range(10)]


##******************************Searching:

##binary search implementation
def binary_search(arr,target):
    low,high = 0, len(arr)-1

    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid

        elif target<arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

##factorial recursion example
def factorial(n):
    #base case(stopping point for working back up the returns)
    #this is when the paused functions are released from the call stack
    if n==1:
        return 1
    else:
        return n*(factorial(n-1))


def sumlst(arr):
    #base case-- returns that arrays element at last index
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sumlst(arr[1:])

def reverse(s):
    #base case is when the length is equal to 1, you are on the last letter
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])
def power(base, exp):
    #base is when the exp is equal to 1 since it is just the base returned, then we multiply everything by that
    if exp == 1:
        return base
    else:
        return base * power(base, (exp-1))
def sum_dig(n):
    string = str(n)
    if len(string) == 1:
        return int(string)
    else:
        return int(string[0]) + sum_dig(string[1:])
def palindrome(s):
    if s == '':
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

def fib(n):
    ##double base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


##merge sort
def mergesort(arr):
    #base case checks if the length is 1
    #this will return that single element array to whichever side variable called it in a recursive function
    if len(arr) <= 1:
        return arr
    else:
        #split the array in half--this will happen logn times
        middle = len(arr) //2
        #create the left/right sorted arrs, these will call mergesort to further divide
        #each call will return a merged arr to the variable calling it
        left_sorted = mergesort(arr[:middle])
        right_sorted = mergesort(arr[middle:])

        #return a single merged array in order from smalles to largest
        return merge(left_sorted, right_sorted)
##merge helper function-- merges together the 2 arrays by comparing pointers
def merge(left, right):
    #create indexes for the pointers which will be incremented each time one is added to result
    j,i = 0,0
    result = []
    #loop until one is empty
    while (i < len(right)) and (j < len(left)):
        if left[j] < right[i]:
            result.append(left[j])
            j+=1
        else:
            result.append(right[i])
            i+=1
    #if empty dump onto the list since the rest is sorted from prev calls
    if left:
        result.extend(left[j:])
    else:
        result.extend(right[i:])
    #return the merged array in sorted order
    return result


    
    



