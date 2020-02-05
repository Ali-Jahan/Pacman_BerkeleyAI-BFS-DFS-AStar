### Pacman AI - Search
# Project Description:
http://ai.berkeley.edu/search.html
(autograder run by autograder.py)

# Implementation

Ali Jahangirnezhad - Project 1 Search

****** Question 1 ******

DFS 

I started with a Fringe stack, an empty visited array and an empty path array.
Every element in the fringe stack has 3 elements : state, visitedArray, pathArray

While the fringe is not empty, I first check to see if the current state is the goal state (if it is, return path)

Then for all the successors, if they are not Visited before, they are pushed into the fringe stack by modified visited and path parameters.

At the end , the path is returned, and it will contain the depth first search algorithm and path. In the while loop, every state is examined to its deepest successor.

****** Question 2 ******

BFS

Same implementation strategy as before, instead of a stack, I used Queue for the Fringe.

****** Question 3 ******

UCS

This time the fringe is a PriorityQueue to keep track of costs and add them to the priority queue.
I start the fringe state, path, cost And cost again(for priorityQueue), and an added cost (fringe.push((start,path,0),0)). Then the while loop works as before, and at the end the path is returned. The only difference here was that the priority queue is working with the modified costs passed in (cost + successor Cost)

****** Question 4 ******

A*

Fringe as priorityQueue, same other attributes as UCS, this time sorted according to the heuristics. 
For every successor, the total cost is calculated as currentCost + successorCost, and the heuristic is calculated as : total = totalCost + heuristic(successor), and then pushed into the fringe.

****** Question 5 ******

getStartDate returns a list of starting position, and an empty corners list. 
GoalState is determined by going through the visited corners. First, the current state must be a corner to be the goal state. 
So if the current state is in corners AND is not visited before (in the prior list of corners) add it to the visited. If the count of visited corners is 4 (all corners) then we return true, because all corners are examined.
For Successors:	I used the code snippet and then followed it by checking if hitsWall == False, then we check if the Next node is a corner, and not visited, so that we add it to Visited. If not, we go straight to the next part which adds this successor to the successors list (successor = (childState, action, 1)

****** Question 6 ******

First I get the current state and the Visited list. Then I initialized an "unvisited" list, which is the corners not yet explored. Next, I go through the unvisited list to calculate the heuristics. 
For this, I initialized a "distances" list, and for every corner I calculated the distance from current state to the corner, and then the distance between that corner and other corners, and at last removing that corner from the list of unvisited corners. Then, I used the minimum distance found in this way to add to the heuristics (as it would be the shortest manhattanDistance).

****** Question 7 ******

For the food heuristics, I first converted the foodGrid to a list, and then used a very basic for loop to check all the foods for their mazeDistance to the current position.It is wildly inefficient and slow, but gets the job done in least number of nodes expanded. The only check here is that IF the distance was greater than the heuristic, then I would set the heuristic to that.
If the start state is the goal state, then it returns 0, and since mazeDistance always returns positive values, the heuristic will always be >= 0 .
(Maze distance is incredibly slow, but helped)
The write-up mentions that your implementation took 2.5 seconds and expanded 5057 nodes for tinySearch. Mine took 9 seconds (yes I know, much slower) but expanded 2372 nodes.
For tricky search, my algorithm took 54 seconds to run, and expanded 4137 nodes (1/4 the nodes found by your algorithm, but takes about 4 times the time as well. Would love to know if I'm onto something here)

****** Question 8 ******

I implemented the isGoalState in anyFoodSearch with one simple line : return self.food[x][y] (if its food, it is true, and returns true), then used a BFS to find a path to the closest dot (that's why I used BFS, "closest" dot).

