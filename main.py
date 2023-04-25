class Problem:
    def __init__(self):
        self.student_id = "xxx"
        self.puzzle = []
        self.goal = ""

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
            self.uniform_cost_search()
        elif choice == "2":
            self.a_star_with_misplaced_tile_heuristic()
        elif choice == "3":
            self.a_star_with_euclidean_distance_heuristic()
        else:
            print("Invalid choice")

    def default_puzzle(self):
        print("default puzzle")

    def uniform_cost_search(self):
        print("uniform cost search")

    def a_star_with_misplaced_tile_heuristic(self):
        print("a* with misplaced tile heuristic")

    def a_star_with_euclidean_distance_heuristic(self):
        print("a* with euclidean distance heuristic")

    def get_goal(self):
        self.goal = "123456780"




if __name__ == "__main__":
    problem = Problem()
    problem.welcome()
    problem.get_puzzle()
    problem.get_goal()
    problem.print_puzzle()
    problem.choose_algorithm()