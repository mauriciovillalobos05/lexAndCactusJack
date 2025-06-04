import sys
import re
from graphviz import Digraph

# Board configuration
GRID_SIZE = 10
DIRECTIONS = ['north', 'east', 'south', 'west']  # Clockwise
DIRECTION_ICONS = {'north': '↑', 'east': '→', 'south': '↓', 'west': '←'}

# Robot state
robot = {
    'x': 0,
    'y': 0,
    'dir': 0  # 0 = north, 1 = east, 2 = south, 3 = west
}
step_count = 0  # For visual naming

def print_state():
    print(f"Robot is at ({robot['x']}, {robot['y']}), facing {DIRECTIONS[robot['dir']]}")
    draw_board()

def rotate(degrees):
    steps = (degrees // 90) % 4
    robot['dir'] = (robot['dir'] + steps) % 4
    print(f"Rotated {degrees}° -> Now facing {DIRECTIONS[robot['dir']]}")

def move(blocks):
    dx, dy = 0, 0
    if DIRECTIONS[robot['dir']] == 'north':
        dy = -1
    elif DIRECTIONS[robot['dir']] == 'east':
        dx = 1
    elif DIRECTIONS[robot['dir']] == 'south':
        dy = 1
    elif DIRECTIONS[robot['dir']] == 'west':
        dx = -1

    for _ in range(blocks):
        new_x = robot['x'] + dx
        new_y = robot['y'] + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            robot['x'] = new_x
            robot['y'] = new_y
        else:
            print(f"Error: move out of bounds at ({new_x}, {new_y}). Stopping further movement.")
            break

    print(f"Moved {blocks} blocks -> Now at ({robot['x']}, {robot['y']})")

def draw_board():
    global step_count
    dot = Digraph(format='png')
    dot.attr(rankdir='TB', size='10')  # Top-Bottom para que y aumente hacia abajo

    # Invertimos el orden: primero filas (de arriba a abajo), luego columnas (x)
    for y in reversed(range(GRID_SIZE)):  # y = 9 (arriba) hasta y = 0 (abajo)
        with dot.subgraph() as s:
            s.attr(rank='same')  # misma fila
            for x in range(GRID_SIZE):
                label = " "
                if x == robot['x'] and y == robot['y']:
                    label = DIRECTION_ICONS[DIRECTIONS[robot['dir']]]
                    s.node(f"{x},{y}", label=label, style='filled', fillcolor='lightblue')
                else:
                    s.node(f"{x},{y}", label='·')

    # Alinear nodos horizontalmente (filas)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE - 1):
            dot.edge(f"{x},{y}", f"{x+1},{y}", style='invis')

    # Alinear nodos verticalmente (columnas)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE - 1):
            dot.edge(f"{x},{y}", f"{x},{y+1}", style='invis')

    filename = f"robot_step_{step_count}"
    dot.render(filename, cleanup=True)
    print(f"Generated: {filename}.png")
    step_count += 1

# Regex patterns
rotate_pattern = re.compile(r"Rotate: (\d+) degrees")
move_pattern = re.compile(r"Move: (\d+) blocks forward")

def run():
    print("Starting simulation...\n")
    print_state()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        rot_match = rotate_pattern.search(line)
        mov_match = move_pattern.search(line)

        if rot_match:
            degrees = int(rot_match.group(1))
            rotate(degrees)
            print_state()
        elif mov_match:
            blocks = int(mov_match.group(1))
            move(blocks)
            print_state()
        elif "Instruction completed" in line:
            print("End of instruction.\n")
        elif "Parse error" in line or "Error" in line:
            print(line)
        else:
            print(f"Ignored: {line}")

if __name__ == "__main__":
    run()