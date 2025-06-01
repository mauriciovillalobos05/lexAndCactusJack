import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Constants
GRID_SIZE = 10
DIRECTIONS = ['N', 'E', 'S', 'W']
ARROWS = {'N': '↑', 'E': '→', 'S': '↓', 'W': '←'}

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction_index = 0  # Starts facing North

    def position(self):
        return (self.x, self.y)

    def direction(self):
        return DIRECTIONS[self.direction_index]
    
    def is_valid_move(self, blocks):
        # Simulate new position
        dx, dy = 0, 0
        if self.direction() == 'N': dy = blocks
        elif self.direction() == 'S': dy = -blocks
        elif self.direction() == 'E': dx = blocks
        elif self.direction() == 'W': dx = -blocks

        new_x = self.x + dx
        new_y = self.y + dy

        return 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE

    def move(self, blocks):
        if self.is_valid_move(blocks):  # <-- Fixed here
            if self.direction() == 'N':
                self.y += blocks
            elif self.direction() == 'S':
                self.y -= blocks
            elif self.direction() == 'E':
                self.x += blocks
            elif self.direction() == 'W':
                self.x -= blocks

    def turn(self, degrees):
        steps = (degrees // 90) % 4
        self.direction_index = (self.direction_index + steps) % 4

def draw_grid(robot):
    fig, ax = plt.subplots()
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_xticks(range(GRID_SIZE + 1))
    ax.set_yticks(range(GRID_SIZE + 1))
    ax.grid(True)

    # Draw robot
    x, y = robot.position()
    arrow = ARROWS[robot.direction()]
    ax.text(x + 0.5, y + 0.5, arrow, fontsize=30, ha='center', va='center', color='red')

    # Draw border
    ax.set_aspect('equal')
    plt.title(f'Robot at ({x}, {y}), facing {robot.direction()}')
    plt.show()

# Example usage
if __name__ == "__main__":
    bot = Robot()
    draw_grid(bot)

    # Simulate a few commands
    bot.move(3)
    draw_grid(bot)

    bot.turn(90)
    bot.move(2)
    draw_grid(bot)

    bot.turn(180)
    bot.move(1)
    draw_grid(bot)