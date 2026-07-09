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
print(array)
print(insertion_sort(array))



