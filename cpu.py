GRID_SIZE = 10

class CPU:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.state_log = []

    def reset(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.state_log.clear()

    def get_state(self):
        return (self.x, self.y, self.angle)

    def execute(self, ast):
        if ast["type"] == "STMT":
            for ins in ast["children"]:
                self.execute(ins)
        elif ast["type"] == "INS":
            self._execute_instruction(ast)

    def _execute_instruction(self, ins_node):
        ins_type = ins_node["ins_type"]
        value = ins_node["value"]

        if ins_type == "INS_MOVE":
            dx, dy = self._get_move_offset(value)
            new_x = self.x + dx
            new_y = self.y + dy

            if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
                self.x = new_x
                self.y = new_y
            else:
                print(f"Ignoring move out of bounds: ({new_x}, {new_y})")

        elif ins_type == "INS_ROTATE":
            if value in [90, 180, 270]:
                self.angle = (self.angle + value) % 360
            else:
                print(f"Invalid rotation angle: {value}")

        self.state_log.append(self.get_state())

    def _get_move_offset(self, blocks):
        angle = self.angle % 360
        if angle == 0:
            return (0, -blocks)
        elif angle == 90:
            return (blocks, 0)
        elif angle == 180:
            return (0, blocks)
        elif angle == 270:
            return (-blocks, 0)
        else:
            return (0, 0)
