## ------------------------------------------------------------------------------------------
#                                  Breath First Search [Empty Map]
## ------------------------------------------------------------------------------------------

'''
Author: Jai Sharma
Task: implement Breath First Search [BFS] algorithm on an empty 10 x 10 map between a given start and goal node
        
'''

## ------------------------------------------------------------------------------------------
#                                        Import Libraries
## ------------------------------------------------------------------------------------------

import time
import copy
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
        state: state of the node
        parent: parent of the node
    '''
    
    def __init__(self, state, parent):
        self.state = state     # current node in the tree
        self.parent = parent   # parent of current node
        
    def __repr__(self):         # special method used to represent a class’s objects as string
        return(f'[ state: {self.state}, parent: {self.parent} ]')
    
    def moveUp(self, pos): # Swap node with the node Above
        row, col = pos[0], pos[1]
        if col < 10:  # node above exists
            upNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  # parent is also a Node in form (state, parent)
            upNode.state[0], upNode.state[1]  = row, col + 1
            return(upNode)    # Up is possible
        else:
            return(False)       # Up not possible
    
    def moveDown(self, pos): # Swap node with the node Below
        row, col = pos[0], pos[1]
        if col > 1:  # node below exists
            downNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent)) 
            downNode.state[0], downNode.state[1]  = row, col - 1
            return(downNode)    # Down is possible         
        else:
            return(False)       # Down not possible

    def moveLeft(self, pos): # Swap node with the node on Left
        row, col = pos[0], pos[1]
        if row > 1:  # node to right exists
            leftNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            leftNode.state[0], leftNode.state[1]  = row - 1, col
            return(leftNode)    # Left is possible
        else:       
            return(False)       # Left not possible

    def moveRight(self, pos): # Swap node with the node on Right
        row, col = pos[0], pos[1]
        if row < 10: # node to left exists
            rightNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            rightNode.state[0], rightNode.state[1]  = row + 1, col
            return(rightNode)    # Right is possible         
        else:
            return(False)       # Right not possible
    
    def getNeighbours(self, pos): # check for neighbours in the 4 directions
        neighbours = []
        up = self.moveUp(pos)
        down = self.moveDown(pos)
        left = self.moveLeft(pos)
        right = self. moveRight(pos)
      
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
    screen = pygame.display.set_mode(((13)*magf, (13)*magf))
    screen.fill((30,30,30))

    startNode = Node(s, None)
    goalNode = Node(g, None)

    queue = deque()               # all nodes to be explored in the order they are in
    visitedList = []              # all visited states
    queue.append(startNode)       # add start node to queue

    while queue != []:
        currentNode = queue.popleft()  # pop last node 
        
        if currentNode.state not in visitedList:         # new state is not goal state and not in visited list
            position = currentNode.state # [x,y] of current node, same as state
            visitedList.append((currentNode.state))

            time.sleep(0.15)
            pygame.draw.circle(screen, (0,128,0), (magf*(1 + goalNode.state[0]), 12*magf-magf*goalNode.state[1]), 16)   # Goal Node
            pygame.draw.circle(screen, (255,0,0), (magf*(1 + startNode.state[0]), 12*magf-magf*startNode.state[1]), 16) # Start Node
            pygame.draw.circle(screen, (255,255,255), (magf*(1 + currentNode.state[0]), 12*magf-magf*currentNode.state[1]), 9)   # Current Node
            pygame.display.update()

            if currentNode.state == g:  # check if goal state reached
                print("Goal Reached! Backtracked Path is:") 
                backTrackList = backtrack(currentNode, startNode)  # backtrack list is goal to start
                reversed_backTrackList = backTrackList[::-1] # reversed --> list is start to goal
                print(backTrackList)
                prev = reversed_backTrackList[0]

                for route in reversed_backTrackList:   # visualize the search algorithm
                    pygame.draw.circle(screen, (0,0,250), (magf*(1 + route[0]), 12*magf-magf*route[1]), 7)   # Current Node     
                    pygame.draw.line(screen, (255, 255, 0), (magf*(1 + route[0]), 12*magf-magf*route[1]), (magf*(1 + prev[0]), 12*magf-magf*prev[1]),5)
                    pygame.draw.circle(screen, (0,0,250), (magf*(1 + prev[0]), 12*magf-magf*prev[1]), 7)   # Current Node     
                    pygame.display.update()
                    prev = route
                time.sleep(2)
                break
            
            else: # if not goal, add neigbours to queue
                Neighbours = currentNode.getNeighbours(position)  # get next layer
                for child in Neighbours:
                    if child not in queue:
                        if child.state not in visitedList:
                            queue.append(child)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return(None)
        
        
## ------------------------------------------------------------------------------------------
#                                  Backtracking Function
## ------------------------------------------------------------------------------------------

def backtrack(current, start):
    backtrackList = [current.state]   # new list to collect backtracked list
    while(current.state != start.state):
        current = current.parent
        backtrackList.append(current.state)
    return(backtrackList)
        
## ------------------------------------------------------------------------------------------
#                                       Main Function
## ------------------------------------------------------------------------------------------

if __name__== "__main__":
    
    s = [5,5] # Start State
    g = [10,10] # Goal State

    # Map Size is set as:
    mapWidth = 10
    mapHeight = 10
    
    # Build a Map
    mapCord = []
    for x in range(1, mapWidth + 1, 1):
        for y in range(1, mapHeight + 1,1):
            mapCord.append([x,y])

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

print("===============================================================================================")
print("Time to Find Solution Path", round((end_time - start_time), 3), "seconds")
print("===============================================================================================")

print('\n')
