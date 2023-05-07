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
        for i in range(0,3):
            for j in range(0,3):
                if initial_state[i * 3 + j] != goal_state[i * 3 + j]:
                    misplaced+=1
        return misplaced

    # TODO: fix for loop
    def a_star_with_misplaced_tile_heuristic(self, initial_state, goal_state):
        frontier = PriorityQueue()
        frontier_set = set() # use to keep track of items in the queue
        frontier.put((initial_state, 0)) # initalize frontier with initial state
        frontier_set.add((initial_state, 0))
        explored = set() # initialize explored set to be empty
        expanded = 0 # keep track of expanded nodes
        max_queue_size = 0
        while not frontier.empty():
            state, cost = frontier.get() # choose a leaf node, also removes from queue
            expanded += 1
            if state == goal_state: # if node contains goal state
                print("Goal!!!")
                print("To solve this problem the search algorithm expanded a total of:", expanded, "nodes.")
                print("The maximum number of nodes in the queue at any one time:", max_queue_size)
                print("The depth of the goal node was:", cost)
                return cost
            explored.add(state) # add node to explored set
            for neighbor in self.get_neighbors(state): # expand chosen node
                if neighbor not in explored: # add resulting nodes to frontier
                   frontier.put((neighbor, cost + self.num_misplaced(neighbor, goal_state) + 1)) 
                   frontier_set.add((neighbor, cost + self.num_misplaced(neighbor, goal_state) + 1))
            if frontier.qsize() >= max_queue_size:
                max_queue_size = frontier.qsize()
        return -1 #if frontier is empty return -1