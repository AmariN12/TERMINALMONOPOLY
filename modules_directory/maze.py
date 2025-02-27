import random as rand
import keyboard
import time
from style import set_cursor, set_cursor_str

class MazeNode:

    def __init__(self, row, col):
        self.col = row
        self.row = col

        RIGHT = (row, col+1)
        LEFT = (row, col-1)
        UP = (row-1, col)
        DOWN = (row+1, col)

        self.visited = False
        '''
        Creates array of tuple. Neighboring MazeNodes and a boolean to idicate if the
        neighboring MazeNodes are connected.
        '''
        '''
        (i+1,j) -> Maze node below
        (i, j+1) -> Maze node to right
        (i-1, j) -> Maze node above
        (i, j-1) -> Maze node left
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
'''
Use data structure to create string form of maze to print to terminal
Terminal space: 75*20 chars
Maze space: 39*19 chars with row 20 being fully spaces
num rows: 9
num cols: 19
Maze offset: 18

Will print all of terminal space
MazeNode[0][0] is bottom left
maze_nodes: list[list[MazeNode]]
'''
def maze_data_to_string() -> list[list[str]]:
    #maze_str = [[' '] * 75]*20
    maze_str = [[' ' for i in range(75)] for j in range(20)]
    corner = '+'
    verticalBar = '|'
    horizontalBar = '-'
    space = ' '

    #Generate corners - i is rows, j is cols
    for i in range(0, 19, 2):
        for j in range(0, 39, 2):
            maze_str[i][j+maze_off] = corner
    
    for i in range(0, 19, 2):
        for j in range(1, 39, 2):
            if j == 1:
                continue
            maze_str[i][j+maze_off] = horizontalBar
    
    for i in range(1, 19, 2):
        for j in range(0, 39, 2):
            if i == 1:
                continue
            maze_str[i][j+maze_off] = verticalBar
    
    #Maze entrance
    maze_str[17][-3+maze_off] = '-'
    maze_str[17][-2+maze_off] = '-'
    maze_str[17][-1+maze_off] = '>'
    maze_str[17][0+maze_off] = space
    maze_str[17][1+maze_off] = '@'

    #Maze exit
    maze_str[1][38+maze_off] = space
    maze_str[1][38+maze_off+2] = '-'
    maze_str[1][38+maze_off+3] = '-'
    maze_str[1][38+maze_off+4] = '>'
    
    '''
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            neighbors_check = [(i-1, j), (i, j+1)]
            for k in range(0, neighbors_check.len):
            
    '''
    return maze_str
    

def maze_input():
    print("You've been trapped in a maze! Use the arrow keys to move and escape!")
    maze_str = maze_data_to_string()
    print_maze(maze_str)
    xPos = [17, 1 + maze_off]
    in_maze = True
    while in_maze == True:
        if maze_str[1][39+maze_off] == "@":
            print("You escaped!")
            break
        key = keyboard.read_key()
        set_cursor(xPos[1], xPos[0])
        if key == 'up':
            if maze_str[xPos[0]-1][xPos[1]] != "-":
                print(" ")
                set_cursor(xPos[1], xPos[0] - 2)
                print("@")
                xPos[0] -= 2
        elif key == 'down':
            if maze_str[xPos[0]+1][xPos[1]] != "-":
                print(" ")
                set_cursor(xPos[1], xPos[0] + 2)
                print("@")
                xPos[0] += 2
        elif key == 'left':
            if maze_str[xPos[0]][xPos[1]-1] != "|":
                print(" ")
                set_cursor(xPos[1] - 2, xPos[0])
                print("@")
                xPos[1] -= 2
        elif key == 'right':
            if maze_str[xPos[0]][xPos[1]+1] != "|":
                print(" ")
                set_cursor(xPos[1] + 2, xPos[0])
                print("@")
                xPos[1] += 2
        elif key == 'esc':
            break
        time.sleep(0.1)

def print_maze(maze):
    for i in range(0, 20):
        for j in range(0, 75):
            print(maze[i][j], end = "")
            if(j == 74):
                print("Line ", i)
    print()

'''
+ +
|X
+-+
input as string, resolves in "for" loop to be able to type many directions at once (use wait or sleep command to force it to stop between)
'''
maze_off = 18
num_rows = 9
num_cols = 19
maze_input()