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

array = [random.randint(1,20) for i in range(10)]
print(bubble_sort(array))



