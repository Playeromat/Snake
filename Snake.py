from SETTINGS import SETTINGS


class Snake:

    def __init__(self):
        self.pos = SETTINGS.INIT_POS[:]
        self.vel = [0, 0]
        self.tail_length = 0
        self.pos_history = []

    def move(self):
        self.pos_history.insert(0, self.pos[:])
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def get_pos(self):
        return self.pos

    def set_pos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def get_pos_history(self):
        return self.pos_history

    def get_tail_length(self):
        return self.tail_length

    def set_tail_length(self, new_length):
        self.tail_length = new_length

    def set_vel(self, new_vel):
        self.vel = new_vel

    def get_vel(self):
        return self.vel

    def reset(self):
        self.pos = SETTINGS.INIT_POS[:]
        self.pos_history = []
        self.vel = [0, 0]
        self.tail_length = 0
