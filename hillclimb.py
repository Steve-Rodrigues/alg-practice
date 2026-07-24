#simple hill climbing: takes a 1-d objective function to maximizie the output by finding the best state
#check neighboors and set the current best state = to that neighboor, the best neighboor is found by taking
#the max of the smaller and bigger state
from math import e
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

#implementing simulated annealing:
#hill climbing except it allows room to explore local optimum values rather than getting stuck.
#it checks the value of the change in E (newE-currE) and if thats positive we except just like hillclimb since positive change
#if negative we need to check the probability of selecting it using the formula of e^(delta E / T) where T is the current temperatre
#this will only be used to return negative numbers to e which means the value will be between 0,1 and the smaller the value--the closer to 1
#so its better when T is a higher value, hence when its exploring more options, and E jumping big will cause lower prob because will be closer to T causing the number to increase
#just change T each time it changes with neigbor because it means the temperatuer is decreasing
def simulatedAnnealing(step=0.1):
    #first random x choice and corresponding state to go with it
    x = random.randint(-10,10)
    currentState = objectiveFunction(x)
    #set the starting T value--high temp first for lots of exploration
    T = 100
    #now exploring starts--runs until T=0 because temperature sets them in place at that point
    while T > 0:
        #randomly choose neighbor value to explore potentially. either going left or right
        neighborDirection = random.choice([-1,1])
        #get the neighbor coordinate to use
        neighbor = (x + (step*neighborDirection), objectiveFunction(x+(step*neighborDirection)))
        #now get the change in E values-- the states
        changeE = neighbor[1] - currentState
        #if positive change always accept, if negative run check against probability and move temp down
        if changeE > 0:
            x,currentState = neighbor[0],neighbor[1]
        #get probability to continue exploring and if random generated is greater than that, then stop
        else:
            prob = e**(changeE/T)
            probCheck = random.random()
            if probCheck < prob:
                x,currentState = neighbor[0], neighbor[1]
        T-=1
    return (x,currentState)
#could add a max iterations check to make sure it doesnt get stuck endlessly going up a hill






