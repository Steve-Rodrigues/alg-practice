##Lab 2: Searching Algorithms
import random, time

##Part 1******************************************

##Linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    #If could not find element
    return -1

##Binary Search
def binary_search(arr,target):
    low,high = 0,len(arr)-1

    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1

    #if not found
    return -1

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j = i
        while((arr[j] < arr[j-1]) and (j>0)):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr

##Part 2*************************************************
if __name__ == '__main__':
    array = [random.randint(1,100_000)for i in range(10_000)]
    ##using diff list so its not sorting for linear as well
    sorted_arr = sorted(array)
    #these will be in the list
    t1,t2 = [array[random.randint(0,len(array)-1)] for i in range(2)]
    #this target is not in the list
    t3 = 100_001

    ##Linear testing
    #t1
    start = time.perf_counter()
    linear_search_1 = linear_search(array,t1)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t1}, value: {array[linear_search_1]}')
    #t2
    start = time.perf_counter()
    linear_search_2 = linear_search(array, t2)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t2}, value: {array[linear_search_2]}')
    #t3
    start = time.perf_counter()
    linear_search_3 = linear_search(array, t3)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t3}, value: {linear_search_3}')

    ##binary testing
    #t1
    start = time.perf_counter()
    binary_search_1 = binary_search(sorted_arr, t1)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t1}, value: {sorted_arr[binary_search_1]}')
    #t2
    start = time.perf_counter()
    binary_search_2 = binary_search(sorted_arr, t2)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t2}, value: {sorted_arr[binary_search_2]}')
    #t3
    start = time.perf_counter()
    binary_search_3 = binary_search(sorted_arr, t3)
    end = time.perf_counter()
    print(f'Took {end-start}s to find element with {t3}, value: {binary_search_3}')











