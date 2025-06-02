import sys
import re

# Board configuration
GRID_SIZE = 10
DIRECTIONS = ['north', 'east', 'south', 'west']  # Clockwise

# Robot state
robot = {
    'x': 0,
    'y': 0,
    'dir': 0  # 0 = north, 1 = east, 2 = south, 3 = west
}

def print_state():
    print(f"Robot is at ({robot['x']}, {robot['y']}), facing {DIRECTIONS[robot['dir']]}")

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
