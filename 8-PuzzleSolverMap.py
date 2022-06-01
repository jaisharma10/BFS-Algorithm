## ------------------------------------------------------------------------------------------
#                                   8 - Puzzle Solver [BFS]
## ------------------------------------------------------------------------------------------

'''
Author: Jai Sharma
Task: implement Breath First Search [BFS] algorithm to solve an 8-puzzle problem

--> Search order is Up, Right, Down, Left
--> Uses pygame for visualization
--> 

'''

## ------------------------------------------------------------------------------------------
#                                        Import Libraries
## ------------------------------------------------------------------------------------------

import time
from collections import deque
import pygame
import sys

start_time = time.time()
print("=======================================================================")

## ------------------------------------------------------------------------------------------
#                                     Node Class
## ------------------------------------------------------------------------------------------

class Node:
    
    '''
    Attributes:
        x: row position of the node
        y: column position of the node
        xP: row position of the Parent node
        yP: column position of the Parent node
    '''
    
    def __init__(self, x, y, xP, yP):
        self.x = x
        self.y = y
        self.xP = xP
        self.yP = yP
                     
    def __repr__(self):    # special method used to represent a class’s objects as string
        return(f'X: {self.x},Y: {self.y}')
            
    def moveRight(self, currentNode): 
        nodeNew = (currentNode.x + 1, currentNode.y) 
        output = (nodeNew) if nodeNew[0] <= 10 else (None)
        return(output)

    def moveLeft(self, currentNode): 
        nodeNew = (currentNode.x - 1, currentNode.y)
        output = (nodeNew) if nodeNew[0] > 0 else (None)
        return(output)

    def moveUp(self, currentNode): 
        nodeNew = (currentNode.x, currentNode.y + 1)
        output = (nodeNew) if nodeNew[1] <= 10 else (None)
        return(output)
    
    def moveDown(self, currentNode): 
        nodeNew = (currentNode.x, currentNode.y - 1)
        output = (nodeNew) if nodeNew[1] > 0 else (None)
        return(output)
    
    def getNeighbours(self, node): # check for neighbours in the 4 directions
        neighbours = []
        up = self.moveUp(node)
        down = self.moveDown(node)
        left = self.moveLeft(node)
        right = self. moveRight(node)
      
        neighbours.append(up) if up else None
        neighbours.append(right) if right else None
        neighbours.append(down) if down else None
        neighbours.append(left) if left else None
        
        return(neighbours)

## ------------------------------------------------------------------------------------------
#                                         BFS Function
## ------------------------------------------------------------------------------------------

def bfs(s, g):
    
    pygame.init()
    magf = 50 # magnification factor
    screen = pygame.display.set_mode(((11)*magf, (11)*magf))
        
    startNode = Node(s[0], s[1], None, None)
    goalNode = Node(g[0], g[1], None, None)
    queue = deque()               # all neighbour states to explore
    visitedList = []              # all visited states

    # add start node to visited list and queue
    queue.append([startNode.x, startNode.y])    

    while queue != []:
        time.sleep(0.5)
        screen.fill((25,25,25))
        currentNode = queue.popleft()  # pop first node in

        if currentNode not in visitedList:         # new state is not goal state and not in visited list
            visitedList.append(currentNode)
            currentNode = Node(currentNode[0], currentNode[1], None, None)

            for point in visitedList:   # visualize the search algorithm
                pygame.draw.circle(screen, (0,200,0), (magf*goalNode.x, 11*magf-magf*goalNode.y), 16)   # Goal Node
                pygame.draw.circle(screen, (255,255,255), (magf*point[0], 11*magf-magf*point[1]), 11)   # Current Node
                pygame.draw.circle(screen, (255,0,0), (magf*startNode.x, 11*magf-magf*startNode.y), 16) # Start Node
                pygame.display.update()
                
            if (currentNode.x,currentNode.y)  == (goalNode.x, goalNode.y):  #  if goal state reached
                print("=======================================================================")
                print("Goal Reached! Backtracked Path is:") 
                backtrack(currentNode, startNode)
                time.sleep(5)
                break
            
            else: # if not goal, add neigbours to queue
                Neighbours = currentNode.getNeighbours(currentNode)  # get next layer
                for child in Neighbours:
                    child = Node(child[0], child[1], currentNode.x, currentNode.y)
                    # print("child", child.x, child.y, child.xP, child.yP)
                    if [child.x, child.y] not in queue:
                        if [child.x, child.y] not in visitedList:
                            queue.append([child.x, child.y])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    return(None)
        
        
## ------------------------------------------------------------------------------------------
#                                  Backtracking Function
## ------------------------------------------------------------------------------------------

def backtrack(current, start):
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("G:", (current.x, current.y))  # backtrack to start node
    print("G_parent:", (current.xP, current.yP))  # backtrack to start node

    while (current.x != start.x) and (current.y != start.y):
        current.x = current.xP
        current.y = current.yP
        print((current.x, current.y))
        time.sleep(0.5)
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    return(None)
        
## ------------------------------------------------------------------------------------------
#                                       Main Function
## ------------------------------------------------------------------------------------------

if __name__== "__main__":
    s = (2,2) # Start Node
    g = (3,4) # Goal Node
    
    print(f" The start node is {s} and the goal node is {g}.")
    print("=======================================================================")

    # Map Size is set as:
    mapWidth = 10
    mapHeight = 10
    
    # Build a Map
    mapCord = []
    for x in range(1, mapWidth + 1, 1):
        for y in range(1, mapHeight + 1,1):
            mapCord.append((x,y))

    # checks if inputs are Valid
    if s not in mapCord:
        print("Start Node outside Map")
    elif g not in mapCord:
        print("Goal Node outside Map")
    elif s == g: # Check if start node is goal node
        print("Start node is Goal Node!!")
    else: 
        print("Implementing Breath First Search")
        bfs(s, g)
    
## ------------------------------------------------------------------------------------------
#                                Display --> Forward and Backward Path
## ------------------------------------------------------------------------------------------

end_time = time.time()

print("=======================================================================")
print("Time to Solve 8-Puzzle Problem:", round((end_time - start_time), 3), "seconds")
print("=======================================================================")

print('\n')
