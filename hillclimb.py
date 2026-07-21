#simple hill climbing: takes a 1-d objective function to maximizie the output by finding the best state
#check neighboors and set the current best state = to that neighboor, the best neighboor is found by taking
#the max of the smaller and bigger state
import random
#this takes in state (x) and returns the value based on the function
def objectiveFunction(x):
    return -(x**2 - 4)**2 + 0.5*x
#algorithm to move state to best option given what is visible at each step(increase or decrease)
def hillclimbing(step=0.1):
    ##choose random starting point value to plug into function
    x = random.randint(-10,10)
    currentState = objectiveFunction(x)
    
    #get neighboor on each side
    left_neigboor = (x-step ,objectiveFunction(x - step))
    right_neighboor = (x+step ,objectiveFunction(x + step))
    #grab biggest y value(state) which is value given from function given the input x
    largestNeighboor = max(left_neigboor, right_neighboor, key=lambda point: point[1])
    #if largest is smaller than current state than stop and return current state(we found a local max)
    numMoves = 0
    while currentState < largestNeighboor[1]:
        x = largestNeighboor[0]
        currentState = largestNeighboor[1]
        numMoves+=1
        
        #run again until the value given is smaller
        left_neigboor = (x-step, objectiveFunction(x-step))
        right_neighboor = (x+step, objectiveFunction(x+step))
        largestNeighboor = max(left_neigboor, right_neighboor, key=lambda point: point[1])
    return (x,currentState)
#random restart allows us to restart n number of times once we get stuck(find a optimum point). this decreases
#the possibility that we just started at a bad spot
#it returns each value to array and then returns the biggest state in it(y value)
def randomRestart(n):
    results = []

    for i in range(n):
        results.append(hillclimbing())
    biggest_point = max(results, key=lambda point: point[1])
    return biggest_point
if __name__ == '__main__':
    print(hillclimbing())
    print(randomRestart(8))
