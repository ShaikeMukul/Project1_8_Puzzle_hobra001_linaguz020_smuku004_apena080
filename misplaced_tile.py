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

    # counts number of misplaced tiles
    def num_misplaced(self, initial_state, goal_state):
        misplaced = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if initial_state[i * 3 + j] != goal_state[i * 3 + j] and initial_state[i * 3 + j] != '0':
                    misplaced += 1
        return misplaced

    def a_star_with_misplaced_tile_heuristic(self, initial_state, goal_state):
        frontier = PriorityQueue()
        frontier.put((0, initial_state))
        explored = set()
        max_queue_size = 1
        nodes_expanded = 0
        while not frontier.empty():
            cost, state = frontier.get()
            nodes_expanded += 1
            if state == goal_state:
                print("Goal!!!")
                print("To solve this problem the search algorithm expanded a total of:", nodes_expanded, "nodes.")
                print("The maximum number of nodes in the queue at any one time:", max_queue_size)
                print("The depth of the goal node was:", cost)
                return cost
            explored.add(state)
            for neighbor in self.get_neighbors(state):
                if neighbor not in explored:
                    frontier.put((self.num_misplaced(neighbor, goal_state) + cost + 1, neighbor))
            if frontier.qsize() > max_queue_size:
                max_queue_size = frontier.qsize()
        return -1  # if frontier is empty return -1