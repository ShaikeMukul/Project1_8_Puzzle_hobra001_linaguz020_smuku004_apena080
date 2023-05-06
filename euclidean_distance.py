from queue import PriorityQueue
from math import sqrt

class EuclideanDistance:
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
    
    def coords(self, state):
        coords = {}
        for i in range(len(state)):
            if state[i] != '0':
                x = i // 3
                y = i % 3
                coords[state[i]] = (x,y)
        return coords
    
    def heuristic(self, state, goal_state):
        state_coords = self.coords(state)
        goal_coords = self.coords(goal_state)
        distance_sum = 0
        for i in state:
            if(i != '0'):
                x1, y1 = state_coords[i]
                x2, y2 = goal_coords[i]
                distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                distance_sum += distance or 0
        return distance_sum
    
    def a_star_with_euclidean_distance_heuristic(self, initial_state, goal_state):
        frontier = PriorityQueue()
        frontier.put((0, initial_state))
        explored = set()
        max_queue_size = 0
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
                    g = cost + 1
                    f = g + self.heuristic(neighbor, goal_state)
                    frontier.put((f, neighbor))
            if frontier.qsize() > max_queue_size:
                max_queue_size = frontier.qsize()
        return -1