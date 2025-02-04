import screenspace as ss
import style as s
from fishing import fishing_game
from socket import socket as Socket
import networking as net
import random as rand

def calculator() -> str:
    """A simple calculator module that can perform basic arithmetic operations."""
    #Uses recursion to calculate.
    def calculate(equation: str) -> float:
        for i in range(0, len(equation)-1):
            if(equation[i] == '+'):
                eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft) + calculate(eqRight)
        
        for i in range(0, len(equation)-1):
            if(equation[i] == '-'):
                #Checks for unary operator '-'
                if(i == 0):
                    eqLeft = "0"
                else:
                    eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft) - calculate(eqRight)
        
        for i in range(0, len(equation)-1):
            if(equation[i] == '*'):
                eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft) * calculate(eqRight)

        for i in range(0, len(equation)-1):
            if(equation[i] == '/'):
                eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft)/calculate(eqRight)
        
        for i in range(0, len(equation)-1):
            if(equation[i] == '%'):
                eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft)%calculate(eqRight) 
            
        for i in range(0, len(equation)-1):
            if(equation[i] == '^'):
                eqLeft = equation[:i]
                eqRight = equation[(i+1):]
                return calculate(eqLeft) ** calculate(eqRight)
        
        return float(equation)

    response = '\nCALCULATOR TERMINAL\n' 
    digit_result = 0
    print("\r", end='')
    equation = input(s.COLORS.GREEN)
    if(equation == "e"):
        return equation
    
    #Trims unnecessary spaces and pads operators with spaces
    equation = equation.replace(" ", "")
    for op in ['+', '-', '*', '/', '%', '^']:
        equation = equation.replace(op, " " + op + " ")
    
    #Removes spaces from negative number
    if(len(equation) > 1 and equation[1] == '-'):
        equation = "-" + equation[3:]

    try:
        digit_result = calculate(equation)
    except:
        return "error"
        
    responseEQ = f'{equation} = {digit_result}'

    #There are 75 columns for each terminal, making any string longer than 75 characters overflow.
    numOverflowingChar = len(responseEQ) - 75
    lineNumber = 0
    wrappedResponse = ""
    while(numOverflowingChar > 0):
        wrappedResponse += responseEQ[(75*lineNumber):(75*(lineNumber + 1))] + '\n'
        lineNumber = lineNumber + 1
        numOverflowingChar = numOverflowingChar - 75
    
    wrappedResponse += responseEQ[(75*lineNumber):(75*(lineNumber + 1)) + numOverflowingChar] + '\n'
    #response += wrappedResponse

    print(s.COLORS.RESET, end='')
    return wrappedResponse

def list_properties() -> str:
    """
    Temporary function to list all properties on the board by calling the property list stored in ascii.txt.
    Can be reworked to add color and better formatting.
    
    Parameters: None
    Returns: None
    """
    ret_val = ""
    props = s.get_graphics().get('properties').split('\n')
    for prop in props:
        if prop == '': 
            ret_val += ' '.center(75) + '\n' 
            continue
        first_word = prop.split()[0]
        color = getattr(s.COLORS, first_word.upper(), s.COLORS.RESET)
        centered_prop = prop.center(75)
        ret_val +=color+ centered_prop + s.COLORS.RESET + '\n'
    return ret_val

def trade():
    pass

def mortgage():
    pass

def roll():
    pass

def gamble():
    pass

def attack():
    pass

def stocks():
    pass

def battleship(server: Socket, gamestate: str) -> str:
    net.send_message(server, 'battleship')

fishing_game_obj = fishing_game()
def fishing(gamestate: str) -> tuple[str, str]:
    """
    Fishing module handler for player.py. Returns tuple of [visual data, gamestate] both as strings.
    """
    stdIn = ''
    match gamestate:
        case 'start':
            return fishing_game_obj.start(), 'playing'
        case 'playing':
            stdIn = fishing_game_obj.get_input()
            if stdIn == 'e':
                return '', 'e'
            return fishing_game_obj.results(), 'e'  
        case 'e':
            return '', 'start'
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

def maze_array_init() -> list[list[MazeNode]]:
    num_rows = 9
    num_cols = 19
    maze_node_list = [MazeNode]
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            node = MazeNode(i, j)
            maze_node_list[i][j] = node

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

def maze_data_to_string() -> str:
    
    pass
    
    

def kill() -> str:
    return s.get_graphics()['skull']

def disable() -> str:
    result = ('X ' * round(ss.cols/2+0.5) + '\n' + 
                (' X' * round(ss.cols/2+0.5)) + '\n'
                ) * (ss.rows//2)
    return result

def make_board(board_pieces) -> list[str]:
    board = [''] * 35
    # Hard coded for board printing specifically
    for i in range(35):
        for j in range(80):
            if board_pieces[i*80+j] != '\n':
                board[i] += (board_pieces[i*80+j])
    return board

