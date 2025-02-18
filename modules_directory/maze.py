import random as rand
import keyboard

class MazeNode:
    def __init__(self, row, col):
        self.col = row
        self.row = col
        self.visited = False
        '''
        Creates array of tuple. Neighboring MazeNodes and a boolean to idicate if the
        neighboring MazeNodes are connected.
        '''
        self.neighbors = [(MazeNode, bool)]

#Create data structure
def maze_array_init() -> list[list[MazeNode]]:
    num_rows = 9
    num_cols = 19
    maze_node_list = [MazeNode]
    #Make 2D list of maze nodes
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            node = MazeNode(i, j)
            maze_node_list[i][j] = node

    #Link neighbors. Need to ensure maze nodes don't have neighbors out of bounds.
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            neighbors_check = [(i+1,j), (i, j+1), (i-1, j), (i, j-1)]

            for k in range(0, neighbors_check.len):
                if(neighbors_check[k][0] < num_rows and neighbors_check[k][0] >= 0):
                    if(neighbors_check[k][1] < num_cols and neighbors_check[k][1] >= 0):
                        maze_node_list[i][j].neighbors.append(maze_node_list[neighbors_check[k][0]][neighbors_check[k][1]], False)
                    else:
                        maze_node_list[i][j].neighbors.append(None, False)
                else:
                    maze_node_list[i][j].neighbors.append(None, False)
                    
    return maze_node_list
            
#Maze generation algo
def maze_generator() -> list[list[MazeNode]]:
        num_rows = 9
        num_cols = 19

        def visit_node(visited_node : MazeNode) -> None:
            visited_node.visited = True
            rand.shuffle(visited_node.neighbors)
            for i in range(0, visited_node.neighbors.len):
                if(visited_node.neighbors[i][0].visited):
                    continue
                else:
                    #Connect nodes
                    visited_node.neighbors[i][1] = True
                    visit_node(visited_node.neighbors[i][0])
            return None
        
        mazeNodes = maze_array_init()
        visit_node(mazeNodes[0][0])
        

        return mazeNodes

#Use data structure to create string form of maze to print to terminal
def maze_data_to_string() -> str:
    
    pass

def maze_input():
    in_maze = True
    while in_maze == True:
        input = keyboard.read_key()
        if input == "up":
            if maze_str[xPos[0]-1][xPos[1]] != "-":
                maze_str[xPos[0]][xPos[1]] = " "
                maze_str[xPos[0]-2][xPos[1]] = "@"
                xPos[0] -= 2
        if input == "down":
            if maze_str[xPos[0]+1][xPos[1]] != "-":
                maze_str[xPos[0]][xPos[1]] = " "
                maze_str[xPos[0]+2][xPos[1]] = "@"
                xPos[0] += 2
        if input == "left":
            if maze_str[xPos[0]][xPos[1]-1] != "|":
                maze_str[xPos[0]][xPos[1]] = " "
                maze_str[xPos[0]][xPos[1]-2] = "@"
                xPos[1] -= 2
        if input == "right":
            if maze_str[xPos[0]][xPos[1]+1] != "|":
                maze_str[xPos[0]][xPos[1]] = " "
                maze_str[xPos[0]][xPos[1]+2] = "@"
                xPos[1] += 2
        if maze_str[1][38+maze_off] == "@":
            in_maze = False
'''
+ +
|X
+-+
input as string, resolves in "for" loop to be able to type many directions at once (use wait or sleep command to force it to stop between)
'''