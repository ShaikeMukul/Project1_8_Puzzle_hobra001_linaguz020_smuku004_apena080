class Puzzle:
    def __init__(self):
        self.student_id = "xxx"
        self.puzzle = []
        self.goal = ""

    def welcome(self):
        print(f"Welcome to {self.student_id} 8 puzzle solver\n") #change xxx this to your student ID




if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.welcome()