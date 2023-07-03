import time
from typing import Dict
import copy
import random
from mad.data_structures import GoalNode, fay_level_order_transversal
from mad.optimize._goal_allocation import jonathan_algorithm
from mad.optimize import test_goal_allocation, _score_allocation


def _random_cost(m: int, n: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        The starting point of the range
    n: int
        The ending point of the range
    
    Returns
    -------
    
    Dict[str,int]
        A dictionary with the agents as keys and corresponding costs as values
    
    """
    
    d = {}
    d["grace"] = random.randint(m,n)
    d["remus"] = random.randint(m,n)
    d["franklin"] = random.randint(m,n)
    #print(d)
    return d

# Test case
def test_algorithm_efficiency():

    #TEST CASE 1: SAME MAX RESOURCES

    # Create a sample goal tree
    print("Test case 1:\n")
    initial_goal_tree = GoalNode("G1", _random_cost(50, 70))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode("G2", _random_cost(25, 40))

    G3 = GoalNode("G3",_random_cost(25,40))

    G4 = GoalNode("G4",_random_cost(25,40))

    G5 = GoalNode("G5",_random_cost(15,30))

    G6 = GoalNode("G6",_random_cost(15,30))

    G7 = GoalNode("G7",_random_cost(15,30))

    G8 = GoalNode("G8",_random_cost(15,30))

    G9 = GoalNode("G9",_random_cost(15,30))

    G10 = GoalNode("G10",_random_cost(5,10))

    G11 = GoalNode("G11",_random_cost(5,10))

    G12 = GoalNode("G12",_random_cost(5,10))

    G13 = GoalNode("G13",_random_cost(5,10))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G3.add_child(G9)
    
    G4.add_child(G10)
    G4.add_child(G11)
    G4.add_child(G12)
    G4.add_child(G13)


    goal_tree = copy.deepcopy(initial_goal_tree)

    # Set the maximum resources for each agent
    max_resources = [50,50,50] #Every agent has the same max_resources

    # Test jonathan_algorithm
    print("Jonathan's algorithm \n")
    start_time = time.time()
    score = _score_allocation(jonathan_algorithm(goal_tree, max(max_resources),1))
    print("Total resources used: ", score[0])
    jonathan_algorithm_time = time.time() - start_time
    print('\n' * 4)

    # Test fay_initial_goal_allocation
    print("Fay's algorithm \n")

    goal_tree = copy.deepcopy(initial_goal_tree)
    start_time = time.time()
    if goal_tree is None:
            return

    q = []
    q.append((goal_tree, None)) # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while len(q) > 0:  # Iterate over the current level
            node, parent = q.pop(0)
            node.initial_agent_assign()
            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

    test_goal_allocation(goal_tree, max_resources)
    fay_initial_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Execution Time - jonathan_algorithm:", jonathan_algorithm_time)
    print("Execution Time - fay_initial_goal_allocation:", fay_initial_goal_allocation_time)

#TEST CASE 2: DIFFERENT MAX RESOURCES

    # Create a sample goal tree
    print("Test case 2:\n")
    initial_goal_tree = GoalNode("G1", _random_cost(60, 80))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode("G2", _random_cost(25, 45)) # level 2

    G3 = GoalNode("G3",_random_cost(25,45))

    G4 = GoalNode("G4",_random_cost(25,45))

    G5 = GoalNode("G5",_random_cost(15,30)) # level 3

    G6 = GoalNode("G6",_random_cost(15,30))

    G7 = GoalNode("G7",_random_cost(15,30))

    G8 = GoalNode("G8",_random_cost(15,30))

    G9 = GoalNode("G9",_random_cost(15,30)) 

    G10 = GoalNode("G10",_random_cost(5,15)) # level 4

    G11 = GoalNode("G11",_random_cost(5,15))

    G12 = GoalNode("G12",_random_cost(5,15))

    G13 = GoalNode("G13",_random_cost(5,15))

    G14 = GoalNode("G14",_random_cost(1,10)) # level 5

    G15 = GoalNode("G15",_random_cost(1,10))

    G16 = GoalNode("G16",_random_cost(1,10))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G2.add_child(G9)

    G6.add_child(G10)
    G6.add_child(G13)
    G9.add_child(G12)
    G9.add_child(G11)
    
    G11.add_child(G14)
    G11.add_child(G16)
    G11.add_child(G15)

    goal_tree = copy.deepcopy(initial_goal_tree)

    # Set the maximum resources for each agent
    max_resources = [50,60,55] #Every agent has the different max_resources

    # Test jonathan_algorithm
    print("Jonathan's algorithm \n")
    start_time = time.time()
    score = _score_allocation(jonathan_algorithm(goal_tree, max(max_resources),1))
    print("Total resources used: ", score[0])
    jonathan_algorithm_time = time.time() - start_time
    print('\n' * 4)

    # Test fay_initial_goal_allocation
    print("Fay's algorithm \n")

    goal_tree = copy.deepcopy(initial_goal_tree)
    start_time = time.time()
    if goal_tree is None:
            return

    q = []
    q.append((goal_tree, None)) # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while len(q) > 0:  # Iterate over the current level
            node, parent = q.pop(0)
            node.initial_agent_assign()
            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

    test_goal_allocation(goal_tree, max_resources)
    fay_initial_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Execution Time - jonathan_algorithm:", jonathan_algorithm_time)
    print("Execution Time - fay_initial_goal_allocation:", fay_initial_goal_allocation_time)
    #print("Execution Time - maheen_algorithm:", maheen_alogrithm)

    print("Test case 3:\n")
    initial_goal_tree = GoalNode("G1", _random_cost(40, 60))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode("G2", _random_cost(20, 30)) # level 2

    G3 = GoalNode("G3",_random_cost(20,30))

    G4 = GoalNode("G4",_random_cost(20,30))

    G5 = GoalNode("G5",_random_cost(10,15)) # level 3

    G6 = GoalNode("G6",_random_cost(10,15))

    G7 = GoalNode("G7",_random_cost(10,15))

    G8 = GoalNode("G8",_random_cost(10,15))

    G9 = GoalNode("G9",_random_cost(10,15)) 

    G10 = GoalNode("G10",_random_cost(5,10)) # level 4

    G11 = GoalNode("G11",_random_cost(5,10))

    G12 = GoalNode("G12",_random_cost(5,10))

    G13 = GoalNode("G13",_random_cost(5,10))

    G14 = GoalNode("G14",_random_cost(1,5)) # level 5

    G15 = GoalNode("G15",_random_cost(1,5))

    G16 = GoalNode("G16",_random_cost(1,5))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G2.add_child(G9)

    G6.add_child(G10)
    G6.add_child(G13)
    G9.add_child(G12)
    G9.add_child(G11)

    G11.add_child(G14)
    G11.add_child(G16)
    G11.add_child(G15)

    goal_tree = copy.deepcopy(initial_goal_tree)

    # Set the maximum resources for each agent
    max_resources = [30, 40, 35] # Every agent has different max_resources

    # Test jonathan_algorithm
    print("Jonathan's algorithm \n")
    start_time = time.time()
    score = _score_allocation(jonathan_algorithm(goal_tree, max_resources[0],1))
    print("Total resources used: ", score[0])
    jonathan_algorithm_time = time.time() - start_time
    print('\n' * 4)

    # Test fay_initial_goal_allocation
    print("Fay's algorithm \n")

    goal_tree = copy.deepcopy(initial_goal_tree)
    start_time = time.time()
    if goal_tree is None:
            return

    q = []
    q.append((goal_tree, None)) # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while len(q) > 0:  # Iterate over the current level
            node, parent = q.pop(0)
            node.initial_agent_assign()
            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

    test_goal_allocation(goal_tree, max_resources)
    fay_initial_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Execution Time - jonathan_algorithm:", jonathan_algorithm_time)
    print("Execution Time - fay_initial_goal_allocation:", fay_initial_goal_allocation_time)


    print("Test case 4 (Edge case):\n")

    max_resources = [30, 40, 35] # Every agent has different max_resources

    # Test jonathan_algorithm
    print("Jonathan's algorithm \n")
    start_time = time.time()
    score = _score_allocation(jonathan_algorithm(None, max(max_resources),1))
    print("Total resources used: ", score[0])
    jonathan_algorithm_time = time.time() - start_time
    print('\n' * 4)

    # Test fay_initial_goal_allocation
    print("Fay's algorithm \n")

    
    start_time = time.time()

    test_goal_allocation(None, max_resources)
    fay_initial_goal_allocation_time = time.time() - start_time

# Run the test cases
test_algorithm_efficiency()

"""
Fay's comment:
Jonathan's algorithm if more efficient when the goal tree has a balanced structure and the resource constraints are not too tight.

Fay's algorithm is more efficient when the goal tree has a skewed structure or when there are significant variations in the costs of goals. 

Two algorithms all throw the exception in the edge case (empty goal tree)
"""