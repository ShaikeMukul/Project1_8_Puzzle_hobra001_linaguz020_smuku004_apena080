# Based on Optional Reading 
# "The algorithm [A*] is identical to UNIFORM-COST-SEARCH except that A* uses g + h instead of g."
from queue import PriorityQueue

class MisplacedTile:
    def get_neighbors(self, state):
        neighbors = []
        index = state.index('0')
        if index % 3 > 0:
            # Move left
            neighbor = state[:index - 1] + '0' + state[index - 1] + state[index + 1:]
            neighbors.append(neighbor)
        if index % 3 < 2:
            # Move right
            neighbor = state[:index] + state[index + 1] + '0' + state[index + 2:]
            neighbors.append(neighbor)
        if index // 3 > 0:
            # Move up
            neighbor = state[:index - 3] + '0' + state[index - 2:index] + state[index - 3] + state[index + 1:]
            neighbors.append(neighbor)
        if index // 3 < 2:
            # Move down
            neighbor = state[:index] + state[index + 3] + state[index + 1:index + 3] + '0' + state[index + 4:]
            neighbors.append(neighbor)
        return neighbors
    
    # TODO: finish this function and test
    # returns h(x) for a given state of the puzzle
    # sum of the manhattan distances for every misplaced tile
    def evaluate_heuristic(self, initial_state, goal_state):
        cost = 0
        # doesn't test whether initial_state is equal to goal_state
        # but calculates sum of the manhattan distances for every tile
        for i in range(0,3):
            for j in range(0,3):
                test = initial_state[i][j]
                for a in range(0,3):
                    for b in range(0,3):
                        correct = goal_state[a][b]
                        if test == correct: # if tile is in the correct spot, cost = 0
                            cost += abs(a-i) + abs(b-j)
        return cost

    # TODO: fix for loop
    def a_star_with_misplaced_tile_heuristic(self, initial_state, goal_state):
        frontier = PriorityQueue()
        frontier.put((initial_state, 0))
        explored = set()
        expanded = 0
        while not frontier.empty():
            state, cost = frontier.get()
            expanded += 1
            if state == goal_state:
                print("Goal!!!")
                print("To solve this problem the search algorithm expanded a total of:", expanded, "nodes.")
                print("The depth of the goal node was:", cost)
                return cost
            explored.add(state)
            for neighbor in self.get_neighbors(state):
                if neighbor not in explored:
                   frontier.put((cost, neighbor)) 
        return -1
        pass