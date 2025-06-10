import ply.lex as lex
import ply.yacc as yacc
import re
from graphviz import Digraph

# === Robot State ===
GRID_SIZE = 10
DIRECTIONS = ['north', 'east', 'south', 'west']
robot = {'x': 0, 'y': 0, 'dir': 0}
step_count = 0

def print_state():
    print(f"Robot is at ({robot['x']}, {robot['y']}), facing {DIRECTIONS[robot['dir']]}")
    draw_board()

def rotate(degrees):
    steps = (degrees // 90) % 4
    robot['dir'] = (robot['dir'] + steps) % 4
    print(f"Rotated {degrees}° -> Now facing {DIRECTIONS[robot['dir']]}")

def move(blocks):
    dx, dy = 0, 0
    if DIRECTIONS[robot['dir']] == 'north': dy = -1
    elif DIRECTIONS[robot['dir']] == 'east': dx = 1
    elif DIRECTIONS[robot['dir']] == 'south': dy = 1
    elif DIRECTIONS[robot['dir']] == 'west': dx = -1

    for _ in range(blocks):
        new_x, new_y = robot['x'] + dx, robot['y'] + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            robot['x'], robot['y'] = new_x, new_y
        else:
            print(f"Error: move out of bounds at ({new_x}, {new_y}).")
            break
    print(f"Moved {blocks} blocks -> Now at ({robot['x']}, {robot['y']})")

def draw_board():
    global step_count
    dot = Digraph(format='png')
    for y in reversed(range(GRID_SIZE)):
        with dot.subgraph() as s:
            s.attr(rank='same')
            for x in range(GRID_SIZE):
                label = "↑" if (x, y) == (robot['x'], robot['y']) else "·"
                s.node(f"{x},{y}", label=label)
    filename = f"ply_robot_step_{step_count}"
    dot.render(filename, cleanup=True)
    print(f"Generated: {filename}.png")
    step_count += 1

# === Lexer ===

tokens = (
    'NOUN', 'POLITE', 'CONJ',
    'ROTATE', 'MOVE',
    'DEG', 'BLOCK',
    'INT', 'REAL', 'DOT'
)

t_NOUN = r'Robot|robot'
t_POLITE = r'please|kindly|would\s+you\s+please'
t_CONJ = r',\s*(and\s+then|then)'
t_ROTATE = r'rotate|turn'
t_MOVE = r'move'
t_DEG = r'degrees?|deg'
t_BLOCK = r'blocks?'
t_DOT = r'\.'

t_ignore = ' \t'

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\/\/[^\n]*'
    pass

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# === Parser ===

def p_program(p):
    'program : statement_list'
    print("End of instruction.")

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    'statement : NOUN POLITE instruction_seq DOT'
    pass

def p_instruction_seq(p):
    '''instruction_seq : instruction
                       | instruction_seq CONJ instruction'''
    pass

def p_instruction(p):
    '''instruction : rotate_instr
                   | move_instr'''
    pass

def p_rotate_instr(p):
    'rotate_instr : ROTATE value DEG'
    deg = p[2]
    if deg in (90, 180, 270):
        rotate(deg)
        print_state()
    else:
        print("Error: only 90, 180, 270 degrees allowed.")

def p_move_instr(p):
    'move_instr : MOVE value BLOCK'
    blocks = p[2]
    if 1 <= blocks <= 10:
        move(blocks)
        print_state()
    else:
        print("Error: blocks must be 1–10.")

def p_value(p):
    '''value : INT
             | REAL'''
    p[0] = int(p[1]) 

def p_error(p):
    print(f"Syntax error at {p.value!r}" if p else "Syntax error at EOF")

parser = yacc.yacc()

# === Main ===

if __name__ == '__main__':
    print("Enter robot instructions (end each with '.'): ")
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        if not s:
            continue
        parser.parse(s)
