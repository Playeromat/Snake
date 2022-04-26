class Food:

    def __init__(self, x, y):
        self.pos = [0, 0]
        self.pos[0] = x
        self.pos[1] = y
        self.picked = False

    def get_pos(self):
        return self.pos

    def is_picked(self):
        return self.picked

    def set_picked(self):
        self.picked = True