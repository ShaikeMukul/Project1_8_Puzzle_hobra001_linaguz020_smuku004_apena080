# Based on Optional Reading 
# "The algorithm [A*] is identical to UNIFORM-COST-SEARCH except that A* uses g + h instead of g."
from queue import PriorityQueue
class MisplacedTile:
    # TODO: write code for finding neighbors
    def find_neighbors(self, state):
        neighbors = []
        return neighbors
    
    # TODO: finish this function and test
    # returns h(x) for a given state of the puzzle
    # sum of the manhattan distances for every misplaced tile
    def evaluate_heuristic(self, state, goal_state):
        cost = 0
        return cost

    # TODO: fix for loop
    def a_star_with_misplaced_tile_heuristic(self, initial_state, goal_state):
        frontier = PriorityQueue()
        frontier.put(initial_state, 0)
        explored = set()
        while not frontier.empty():
            state, cost = frontier.get()
            expanded += 1
            if state == goal_state:
                print("Goal!!!")
                print("To solve this problem the search algorithm expanded a total of:", expanded, "nodes.")
                print("The depth of the goal node was:", cost)
                return cost
            explored.put(state, cost)
            for neighbor in self.find_neighbors:
                if neighbor not in explored:
                    frontier.put(neighbor.evaluate_heuristic(), neighbor)
        pass