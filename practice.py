# 1. Median salary. A company has an unsorted list of n employee salaries. HR wants
# the median salary but doesn't want to pay for a full sort. Design an algorithm that
# finds it in expected O(n) time. (This is the classic motivation for quickselect —
# you don't need the whole array sorted, just one position.)
from random import randint
def median_salary(salaries: list[int]) -> float:
    median_index = len(salaries) //2
    #base case is when the median index is sorted--all elements below are less than and all elements above are greater
    #try checking if it is equal to the pivot at the end, so the less than holder
    def quickselect(salaries, start, end):
        pivot_idx = randint(start, end)
        pivot_element = salaries[pivot_idx]
        #swap to the end so its not in the way
        salaries[end],salaries[pivot_idx] = salaries[pivot_idx],salaries[end]
        ##loop through list from start to end(pivot) and set less than holder 
        less_than_holder = start
        for i in range(start, end):
            if salaries[i] < pivot_element:
                salaries[i],salaries[less_than_holder] = salaries[less_than_holder],salaries[i]
                less_than_holder+=1
        #move pivot to the current holder and put that at the end so the pivot is sorted
        salaries[end],salaries[less_than_holder] = salaries[less_than_holder],salaries[end]
        #base case check-- if element at median_index is sorted in place return that element
        if median_index == less_than_holder:
            return pivot_element
        #else only continue on the part that has the index of the median index
        else:
            #if the median index is on the left of pivot then continue on that side
            if median_index < less_than_holder:
                return quickselect(salaries, start, end=less_than_holder-1)
            else:
                return quickselect(salaries, start=less_than_holder+1, end=end)
    return quickselect(salaries, 0, len(salaries)-1)


print(median_salary([50000, 60000, 40000, 70000, 55000]))


