from Queue import PriorityQueue

def unweighted(state, neighbor):
    """
    The unweighted graph cost function.
    """
    return 1

class Graph:
    """
    A Graph consists of a neighbor function and a cost function.

    neighbors --
        Either...
        - A dictionary that maps a state to an iterable of neighbor states
        - A function that takes in a state and returns an iterable of neighbor states
    cost --
        Either...
        - Unspecified (Default: unweighted cost function)
        - A dictionary that maps a 2-tuple of states to an associated cost
        - A function that takes in two states and returns an associated cost

    If a dict is chosen for either of the above, it is wrapped behind a function.
    """
    def __init__(self, neighbors, cost=unweighted):
        self.neighbors = (lambda x: neighbors[x]) if isinstance(neighbors, dict) else neighbors
        self.cost = (lambda x, y: cost[(x, y)]) if isinstance(cost, dict) else cost

def trivial(state):
    """
    The trivial graph search heuristic.
    """
    return 0

def a_star_search(graph, start_states, is_goal_state, heuristic=trivial):
    """
    Terminates upon finding a state which satisfies the is_goal_state function, or exhausts all possible states and returns None.

    start_states -- An iterable of initial states.
    is_goal_state -- A binary function which returns true if a given state is a goal state.
    heuristic -- A function which takes in a state and returns an appropriate heuristic value that satisfies the requirements of the A* algorithm.
    
    Upon termination, returns a valid path from the start state to the goal.
    """
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}
    for start in start_states:
        frontier.put((heuristic(start), start))
        came_from[start] = None
        cost_so_far[start] = 0
    while not frontier.empty():
        priority, current = frontier.get()
        if is_goal_state(current):
            return recreate_path(current, came_from)
        for neighbor in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

def recreate_path(goal, came_from):
    path = []
    curr = goal
    while curr != None:
        path.append(curr)
        curr = came_from[curr]
    path.reverse()
    return path
