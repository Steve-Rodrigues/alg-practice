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


# 2. Top k earners. Same company, but now they want a list of the k highest-paid
# employees, in any order (not necessarily sorted among themselves). Can you avoid
# fully sorting the array? What does your solution look like when k is very small
# compared to n vs. when k is close to n?
def top_k_earners(salaries: list[int], k: int) -> list[int]:
    pass


# 3. Pass/fail split. A teacher has an unsorted list of exam scores and a passing
# threshold (say, 60). Rearrange the array in place, in one pass, so all passing scores
# come before all failing scores -- no extra array. (This is literally a two-way
# partition step, just with an external threshold instead of a pivot drawn from the data.)
def pass_fail_split(scores: list[int], threshold: int = 60) -> list[int]:
    pass


# 4. Sorting paint cans. You have cans of paint labeled only red, white, or blue,
# arranged randomly on a shelf. Rearrange them in one pass, O(1) extra space, so all
# reds come first, then whites, then blues. (Dutch national flag -- a 3-way
# generalization of partitioning.)
def sort_paint_cans(cans: list[str]) -> list[str]:
    pass
