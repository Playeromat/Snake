class ScoreHandler:

    def __init__(self):
        self.current_score = 0
        self.highscore = 0

    def add_score(self, score):
        self.current_score += score
        print("score: " + str(self.current_score))
        if self.current_score > self.highscore:
            self.highscore = self.current_score

    def get_score(self):
        return self.current_score

    def reset_score(self):
        self.current_score = 0