#Dynamic Programming is an optimization strategy used to turn very slow algorithms, possibly exponential, into polyunomail time efficiencies
#You have to evaluate whether your problem has optimal substructure which means the optimal solution of your input is made up of the optimal solutions of the smaller sub-problem inputs
#If that is true, it also needs to contain overlapping subproblems because the whole idea is we are going to be caching the results of the subproblem calls for later use
#this makes it so we do not have to continue to call a subproblem after we have solved it once becasue that result is cached in the array at that n index
#If a problem has optimal substructuring but not overlapping subproblems, then each problem is indpendent of the last which means Divided and conquer rather than DP because DP deals with dependent subproblems(not creating reusing)
#The 2 approaches for DP is top to bottom (memoization) or bottom to top(tabulation)
#Memoization uses the same recursive structure but it only calls the recursive call if we have not already encountered it and cached it in the array which will be checked each time
#this can be dangerous for large inputs because the call stack can overflow due to the recursive calling
#Tabulation works bottom to top and doesn't actually call the smaller functoins on the inside. We store the base cases in the array and loop iteratively from 1 past the base case up to the version you are calling
#this is safer because we only call the function once(the outer call) and just use each cached result in the array to store the result of each sub-problem

#lets do a simple example using the fibonacci sequence: we can use it here because its definition is made of subproblems(overlapping) and the optimal solution is made of the subproblems optimal solutions
#Memoization- top-bottom first, still using recursion but only O(n) times
#defined as f(0), f(1) = 0,1 and the rest is fib(n-2) + fib(n-1)
import time


def memFib(n, cache=None):
    if cache is None:
        cache = {}
    #base cases
    if n == 0:
        cache[0] = 0
        return 0
    if n == 1:
        cache[1] = 1
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = memFib(n-2, cache=cache) + memFib(n-1, cache=cache)
            return cache[n]
#Here we continue to call the actual function until we get to the point that all n have been called, then as it works down continuosly, those results were cached so we just return those cached results instead

#now going to use tabulation(safer approach due to no call stack since we are using previous values every sinlge time)
#we solve the small subproblems from bottom up and use that to solve the next ones. This also ONLY runs n times because we just need the loop to run 
def tabFib(n):
    dp_table = [-1 for i in range(n)]
    #base cases are filled right away becasue its one call and works bottom up
    dp_table[0] = 0
    dp_table[1] = 1
    #in this case we loop from 2 to n because teh base cases end at n=1 so the indices after are being computed as we go upwards
    for i in range(2, n):
        dp_table[i] = dp_table[i-2] + dp_table[i-1] #results are retrieved in constant time by index lookup from prev results as we build up
    return dp_table[n-2] + dp_table[n-1]


if __name__ == '__main__':
    #timing the two functions now
    start = time.time()
    #print(memFib(3005))
    end = time.time()
    start2 = time.time()
    print(memFib(10095))
    end2 = time.time()
    print(f'{end-start}\n{end2-start2}')