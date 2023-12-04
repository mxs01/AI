# # Assignment 06 - LRTA

#########################################
# Student1 Name: Maximilian Schnitt
# Matriculation No1: 6040570

# Student2 Name: Jonathan von Rad
# Matriculation No2: 6004279
#########################################
# ## Initialization


class GridNode:
    def __init__(self, name, neighbours=[], dist_neighbours=[], h=None, H=None):
        """
        Args:
            name: The name of this / current node
            neighbours: A list containing of all the neighbour gridnodes
            dist_neighbours: The distance to each neighbor of the node (same order as self.neighbours)
            h: The heuristic h(s)
            H: H(s) the H table cost
        """
        self.neighbours = neighbours
        self.dist_neighbours = dist_neighbours
        self.name = name
        self.h = h
        self.H = H
        assert len(self.dist_neighbours) == len(self.neighbours)

    def get_distance(self, neighbour_node):
        """
        function to calculate the distance between node and its neighbour
        Args:
            neighbour_node: neighbour of the current object (self) whose distance we want to find

        Returns: distance between current node (self) and its neighbour node (neighbour_node)

        """
        idx = self.neighbours.index(neighbour_node)
        dist = self.dist_neighbours[idx]
        return dist

def initialize_all_nodes():
    """
       initialize all the nodes
    """
    node = {}
    node['A'] = GridNode(name='A', h=15, H=15)
    node['B'] = GridNode(name='B', h=12, H=12)
    node['C'] = GridNode(name='C', h=10, H=10)
    node['D'] = GridNode(name='D', h=9, H=9)
    node['E'] = GridNode(name='E', h=7, H=7)
    node['F'] = GridNode(name='F', h=5, H=5)
    node['G'] = GridNode(name='G', h=0, H=0)
    node['H'] = GridNode(name='H', h=0, H=0)
    node['I'] = GridNode(name='I', h=4, H=4)
    node['J'] = GridNode(name='J', h=10, H=10)
    node['K'] = GridNode(name='K', h=1, H=1)
    node['L'] = GridNode(name='L', h=5, H=5)
    node['M'] = GridNode(name='M', h=3, H=3)
    node['N'] = GridNode(name='N', h=2, H=2)

    node['A'].neighbours = [node['B'], node['I']]
    node['A'].dist_neighbours = [2, 3]
    node['B'].neighbours = [node['A'], node['C'], node['I'], node['J']]
    node['B'].dist_neighbours = [2, 3, 2, 5]
    node['C'].neighbours = [node['B'], node['D'], node['J']]
    node['C'].dist_neighbours = [3, 1, 3]
    node['D'].neighbours = [node['C'], node['E'], node['K']]
    node['D'].dist_neighbours = [1, 2, 1]
    node['E'].neighbours = [node['D'], node['F'], node['L']]
    node['E'].dist_neighbours = [2, 1, 2]
    node['F'].neighbours = [node['E'], node['G'], node['M']]
    node['F'].dist_neighbours = [1, 4, 4]
    node['G'].neighbours = [node['F'], node['H'], node['M'], node['N']]
    node['G'].dist_neighbours = [4, 5, 4, 5]
    node['H'].neighbours = [node['G'], node['N']]
    node['H'].dist_neighbours = [5, 2]
    node['I'].neighbours = [node['A'], node['B'], node['J']]
    node['I'].dist_neighbours = [3, 2, 5]
    node['J'].neighbours = [node['B'], node['C'], node['I'], node['K']]
    node['J'].dist_neighbours = [5, 3, 5, 5]
    node['K'].neighbours = [node['D'], node['J'], node['L']]
    node['K'].dist_neighbours = [1, 5, 1]
    node['L'].neighbours = [node['E'], node['K'], node['M']]
    node['L'].dist_neighbours = [2, 1, 3]
    node['M'].neighbours = [node['F'], node['G'], node['L'], node['N']]
    node['M'].dist_neighbours = [4, 4, 3, 2]
    node['N'].neighbours = [node['G'], node['H'], node['M']]
    node['N'].dist_neighbours = [5, 2, 2]

    return node


######################################################
# Implement LRTA*-COST() at slide 77 here
######################################################
def lrta_cost(previous_state:GridNode, state:GridNode):
    """
    Function computes  the cost estimate of a node using the distance between
    the nodes (previous state and state) and the H table

    Args:
        previous_state: s
        state: s'

    Returns: The cost estimate

    """
    # TODO: Q2
    if state == None:
        # h(s)
        return previous_state.h
    # c(s,a,s') + H(s')
    return previous_state.get_distance(state) + state.H


######################################################
# Implement LRTA*-AGENT() at slide 77 here
######################################################
def lrta_agent(state:GridNode=None, previous_state:GridNode=None, goal:GridNode=None):
    """
    Function identifies and returns  the next node to be expanded given the current and previous states
    Args:
        state: s'
        goal: goal state
        previous_state: s

    Returns: The next node to be expanded

    """
    # TODO: Q2(b)
    if goal.name == state.name:
        return
    
    # state not in H
    
    # compute min lta* cost estimate
    
   
    if previous_state != None:
        neighbours = previous_state.neighbours
        min_cost= float('inf')
        # for possible_new_state in neighbours:
        #     cost = lrta_cost(state,possible_new_state)
        #     if cost < min_cost:
        #         min_cost=cost
        min_cost = lrta_cost(previous_state,state) 
        previous_state.H = min_cost
    
    possible_actions = {neighbour.name:state.get_distance(neighbour) + neighbour.H for neighbour in state.neighbours}
    
    best_action = min(possible_actions,key=lambda node: possible_actions[node])
    
    previous_state = state
    return best_action


def lrta_graphsearch(start_node:GridNode, goal_node:GridNode):
    """
    Function returns the path and the number of steps taken by the agent from the start node to goal node

    Args:
        start_node:
        goal_node:

    Returns: path: list of names of all the nodes traversed / visited i.e. path taken from 'start_node' to arrive at 'goal_node'
            steps: number of steps taken (nodes visited) from 'start_node' to arrive at 'goal_node'

    """
    steps = 0
    path:list = []
    previous_state:GridNode = None
    current_state:GridNode = start_node
    while (True):
        # TODO: Q2(c)
        
        if (previous_state == None):
            path.append(previous_state)
        path.append(current_state.name)
            
        
        #get best action for current state
        action = lrta_agent(current_state, previous_state,goal_node)
        # goal check
        if action == None:
            return path,steps
        #update states
        previous_state = current_state
        next_state = [next_state for next_state in current_state.neighbours if next_state.name == action]
        
        if len(next_state)>0:
            current_state = next_state[0]
        # increment step size
        steps += 1 



def lrta_till_convergence(start_node, goal_node, nodes):
    """
    Function returns the path and the number of steps taken by the agent from the start node to goal node

    Args:
        start_node:
        goal_node:
        nodes:

    Returns: iteration: how many times lrta was executed 
            path: list of names of all the nodes traversed / visited i.e. path taken from 'start_node' to arrive at 'goal_node'
            steps: number of steps taken (nodes visited) from 'start_node' to arrive at 'goal_node'

    """

    while True:
        path,step_count = lrta_graphsearch(start_node,goal_node)
        


def taskD():
    """
    generates print statements to answer question 2d)
    """
    nodes = initialize_all_nodes()
    start_nodes = [nodes["F"], nodes["I"], nodes["N"], nodes["K"]]
    goal_node = nodes["H"]
    for start_node in start_nodes:
        nodes = initialize_all_nodes()
        path, steps = lrta_graphsearch(start_node, goal_node)
        print("#####################################################################")
        print(f"Start Node: {start_node.name}  Goal: {goal_node.name}")
        print(f"Amount of steps: {steps}")
        print(f"Path: {path}")
        print()



if __name__ == "__main__":
    # driver code for the main algorithm
    nodes = initialize_all_nodes()
    start_node = nodes['A']
    goal_node = nodes['H']
    path, steps = lrta_graphsearch(start_node, goal_node)
    print('\nThe path from', start_node.name, 'to', goal_node.name, 'is:\n', path)
    print('Total number of steps taken:', steps)
    
    taskD()