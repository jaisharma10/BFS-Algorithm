# Breath First Search [BFS] Algorithm

### Task:

Implement Breath First Search [BFS] algorithm on a map between a given start and goal node. The repository contains 3 files:

- **BFS_emptyMap.py** - The 10 x 10 map is empty. The script finds BFS generated path between two nodes.
- **BFS_obsMap.py** - The 10 x 10 map has obstacles. The script finds the BFS generated path between the two nodes while avoiding obstacle space. There algorithm can be mplemented on two maps.  Set the variable 'mapNumber' to 1 or to 2 in the main function to switch between maps.
- **BFS_Maze.py** - Maze Map of size 16 x 8. The script finds BFS generated path between two nodes.
        
### Path is visualized using pygame. 
- Start Node is Red
- Goal Node is Green
- Solution Path is in Blue/Yellow
- Explored Nodes are in White

### 4 action steps. Search Sequence: 
<p align="center">
        Up --> Right --> Down --> Left
</p>

## Breath First Search 

### Tree Exploration Sequence: 

BFS is a graph traversing algorithm. The traversal occurs layerwise, the neighbour nodes are visited first. The queue works on the FIFO model. The breathwise exploration is shown in the illustration below: 

<p align="center">
        <img src = "https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif" width = "210">
</p>

## Empty Map Results 

Start Node:(1,1) --> Goal Node:(5,5) |  Start Node:(7,9) --> Goal Node:(1,2)| Start Node:(6,6) --> Goal Node:(10,10)
:-------------------------:|:-------------------------:|:-------------------------:
<img src = "Images/1,1 to 5,5.PNG" width = "250">  |  <img src = "Images/7,9 to 1,2.PNG" width = "250">| <img src = "Images/66_1010.PNG" width = "250">

## Obstacle Map Results 

Map 1: (1,10) --> (10,1)   |  Map 2: (1,10) --> (10,1) 
:-------------------------:|:-------------------------:
<img src = "Images/obsMap1.PNG" width = "350">  |  <img src = "Images/obsMap2.PNG" width = "350">

## Maze Map Results

<p align="center">
        Start Node:(1,1) --> Goal Node:(16,1)
</p>

<p align="center">
       <img src = "Images/bfs_maze.PNG" width = "600">
</p>


## Support
For any questions, email me at jaisharm@umd.edu
