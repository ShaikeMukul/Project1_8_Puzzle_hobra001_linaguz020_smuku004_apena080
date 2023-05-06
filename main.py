from uniform_cost import UniformCost
from misplaced_tile import MisplacedTile
from euclidean_distance import EuclideanDistance

class Problem:
    def __init__(self):
        self.student_id = "xxx"
        self.puzzle = []
        self.goal = ""
        self.uniform_cost = UniformCost()
        self.euclidean_distance = EuclideanDistance()

    def welcome(self):
        print(f"Welcome to {self.student_id} 8 puzzle solver\n") #change xxx this to your student ID
    
    def get_puzzle(self):
        print("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
        choice = input()
        if choice == "1":
            self.default_puzzle()
        elif choice == "2":
            self.custom_puzzle()
        else:
            print("Invalid choice")

    def default_puzzle(self):
        dp = [['1', '2', '3'],
              ['4', '8', '0'],
              ['7', '6', '5']]
        self.puzzle = dp

    def custom_puzzle(self):
        print("Enter your puzzle, use a zero to represent the blank\n")
        for _ in range(3):
            print("Enter the values for row", _ + 1, "separated by spaces")
            row = input().split()
            self.puzzle.append(row)

    def print_puzzle(self):
        for row in self.puzzle:
            print(row)

    def choose_algorithm(self):
        print("Enter your choice of algorithm\n")
        print("1. Uniform Cost Search")
        print("2. A* with the Misplaced Tile heuristic")
        print("3. A* with the Euclidean Distance heuristic")
        choice = input()
        if choice == "1":
            str_puzzle = ""	
            for p in self.puzzle:	
                str_puzzle += "".join(p)	
            cost = self.uniform_cost.uniform_cost_search(str_puzzle, self.goal)	
            if cost == -1:	
                print("No solution found")
        elif choice == "2":
            self.a_star_with_misplaced_tile_heuristic()
        elif choice == "3":
            str_puzzle = ""	
            for p in self.puzzle:	
                str_puzzle += "".join(p)	
            cost = self.euclidean_distance.a_star_with_euclidean_distance_heuristic(str_puzzle, self.goal)	
            if cost == -1:	
                print("No solution found")
        else:
            print("Invalid choice")

    def get_goal(self):
        self.goal = "123456780"



if __name__ == "__main__":
    problem = Problem()
    problem.welcome()
    problem.get_puzzle()
    problem.get_goal()
    problem.print_puzzle()
    problem.choose_algorithm()