# Breath First Search [BFS] Algorithm

### Task:

Implement Breath First Search [BFS] algorithm on an empty 10 x 10 map between a given start and goal node. The repository contains 2 files:

- **BFS_emptyMap.py** - The map is empty. The script finds BFS generated path between the two nodes.
- **BFS_obsMap.py** - The map has obstacles. The script finds the BFS generated path between the two nodes while avoiding obstacle space. There algorithm can be mplemented on two maps.  Set the variable 'mapNumber' to 1 or to 2 in the main function to switch between maps.
        
### Path is visualized using pygame. 
- Start Node is Red
- Goal Node is Green
- Solution Path is in Blue/Yellow
- Explored Nodes are in White

### 4 action steps. Search Sequence: 
<p align="center">
        Up --> Right --> Down --> Left
</p>

## Empty Map Results 

Start Node:(1,1) --> Goal Node:(5,5) |  Start Node:(7,9) --> Goal Node:(1,2)
:-------------------------:|:-------------------------:
<img src = "Images/1,1 to 5,5.PNG" width = "400">  |  <img src = "Images/7,9 to 1,2.PNG" width = "400">

## Obstacle Map Results 

Map 1: (1,10) --> (10,1)   |  Map 2: (1,10) --> (10,1)
:-------------------------:|:-------------------------:
<img src = "Images/obsMap1.PNG" width = "400">  |  <img src = "Images/obsMap2.PNG" width = "400">

## Support
For any questions, email me at jaisharm@umd.edu
