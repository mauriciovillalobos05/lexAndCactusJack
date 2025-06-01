import csv
import numpy as np

# Tablero 10x10
map_field = np.zeros(shape=(10, 10), dtype=int)

# Direcciones como vectores (N, E, S, O)
DIRECTIONS = ['N', 'E', 'S', 'W']
DIR_VECTORS = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'

    def turn(self, degrees):
        # Turn right in steps of 90 degrees
        steps = (degrees // 90) % 4
        current_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_idx + steps) % 4]
        print(f"Turned {degrees} degrees. Now facing {self.direction}.")

    def move_forward(self, blocks):
        dx, dy = DIR_VECTORS[self.direction]
        for _ in range(blocks):
            new_x = self.x + dx
            new_y = self.y + dy
            if 0 <= new_x < 10 and 0 <= new_y < 10:
                self.x = new_x
                self.y = new_y
                map_field[self.x][self.y] = 1  # Marca paso del robot
            else:
                print("Move ignored: out of bounds.")
                break
        print(f"Moved {blocks} blocks forward to ({self.x}, {self.y})")

def do_instruction(robot, inst):
    command = inst[0].strip().lower()
    if "turn" in command:
        degrees = int(command.split()[-2])  # Assumes: "turn 90 degrees"
        robot.turn(degrees)
    elif "move" in command:
        blocks = int(command.split()[-3])  # Assumes: "move 3 blocks forward"
        robot.move_forward(blocks)
    else:
        print(f"Unknown instruction: {inst}")

def read_file():
    inst_list = []
    with open('instructions.asm') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            inst_list.append(row)
    return inst_list

def main():
    print("=== Starting Robot Simulation ===")
    robot = Robot()
    inst_list = read_file()
    for inst in inst_list:
        do_instruction(robot, inst)
        print(map_field)

if __name__ == "__main__":
    main()
