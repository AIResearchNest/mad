from mad.data_structures import GoalNode, print_goal_tree, print_tree_and_agents
from mad.optimize import dfs_goal_allocation, optimized_goal_allocation
from typing import Dict
import random as r
import matplotlib.pyplot as plt

# Helper Functions
def _random_cost(m: int, n: int, agents: int) -> Dict[str, int]:
    
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
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "trent", "karen"]

    d = {}
    for i in range(agents):
        d[AGENTS[i]] = r.randint(m,n)

    return d

def _equal_cost(m: int, n: int, agents: int) -> Dict[str, int]:
    
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
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "trent", "karen"]

    d = {}
    cost = r.randint(m,n)
    for i in range(agents):
        d[AGENTS[i]] = cost

    return d

# Scoring
def get_total_cost(agents_and_goals):

    total_cost = 0

    for agent in agents_and_goals.keys():

        for goal in agents_and_goals[agent]:
            total_cost += goal.cost

    return total_cost

# Equal Trees
def equal_binary_symmetric(num_agents):

    root = GoalNode("Main Goal", _equal_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(5, 15, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(5, 15, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(5, 15, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def equal_binary_left(num_agents):

    root = GoalNode("Main Goal", _equal_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(5, 15, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def equal_binary_right(num_agents):

    root = GoalNode("Main Goal", _equal_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(5, 15, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    return root

def equal_root(num_agents):

    root = root = GoalNode("Main Goal", _equal_cost(25, 45, num_agents))

    return root

def equal_tree_symmetric(num_agents):

    root = GoalNode("Main Goal", _equal_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(15, 25, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(5, 10, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(5, 10, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(5, 10, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(5, 10, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(5, 10, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(5, 10, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _equal_cost(5, 10, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _equal_cost(5, 10, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _equal_cost(5, 10, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    return root

def equal_tree_left_right(num_agents):

    root = GoalNode("Main Goal", _equal_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(15, 25, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(5, 10, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(5, 10, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(5, 10, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(5, 10, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(5, 10, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(5, 10, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    return root

def equal_large_binary_tree(num_agents):
    
    x = 40
    y = 60
    root = GoalNode("Main Goal", _equal_cost(x, y, num_agents))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(x, y, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(x, y, num_agents))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(x, y, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(x, y, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(x, y, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(x, y, num_agents))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(x, y, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(x, y, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(x, y, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _equal_cost(x, y, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _equal_cost(x, y, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _equal_cost(x, y, num_agents))
    subgoal13 = GoalNode("Sub Goal 13", _equal_cost(x, y, num_agents))
    subgoal14 = GoalNode("Sub Goal 14", _equal_cost(x, y, num_agents))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _equal_cost(x, y, num_agents)) 
    subgoal16 = GoalNode("Sub Goal 16", _equal_cost(x, y, num_agents))
    subgoal17 = GoalNode("Sub Goal 17", _equal_cost(x, y, num_agents))
    subgoal18 = GoalNode("Sub Goal 18", _equal_cost(x, y, num_agents))
    subgoal19 = GoalNode("Sub Goal 19", _equal_cost(x, y, num_agents))
    subgoal20 = GoalNode("Sub Goal 20", _equal_cost(x, y, num_agents))
    subgoal21 = GoalNode("Sub Goal 21", _equal_cost(x, y, num_agents))
    subgoal22 = GoalNode("Sub Goal 22", _equal_cost(x, y, num_agents))
    subgoal23 = GoalNode("Sub Goal 23", _equal_cost(x, y, num_agents))
    subgoal24 = GoalNode("Sub Goal 24", _equal_cost(x, y, num_agents))
    subgoal25 = GoalNode("Sub Goal 25", _equal_cost(x, y, num_agents))
    subgoal26 = GoalNode("Sub Goal 26", _equal_cost(x, y, num_agents))
    subgoal27 = GoalNode("Sub Goal 27", _equal_cost(x, y, num_agents))
    subgoal28 = GoalNode("Sub Goal 28", _equal_cost(x, y, num_agents))
    subgoal29 = GoalNode("Sub Goal 29", _equal_cost(x, y, num_agents))
    subgoal30 = GoalNode("Sub Goal 30", _equal_cost(x, y, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    return root

def equal_large_tree(num_agents):

    x = 40
    y = 60
    root = GoalNode("Main Goal", _equal_cost(x, y, num_agents))
    
    x = 13
    y = 20
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(x, y, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(x, y, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(x, y, num_agents))

    x = 4
    y = 7
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(x, y, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(x, y, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(x, y, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(x, y, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(x, y, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(x, y, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _equal_cost(x, y, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _equal_cost(x, y, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _equal_cost(x, y, num_agents))
    
    x = 1
    y = 3
    
    subgoal13 = GoalNode("Sub Goal 13", _equal_cost(x, y, num_agents))
    subgoal14 = GoalNode("Sub Goal 14", _equal_cost(x, y, num_agents))
    subgoal15 = GoalNode("Sub Goal 15", _equal_cost(x, y, num_agents)) 
    subgoal16 = GoalNode("Sub Goal 16", _equal_cost(x, y, num_agents))
    subgoal17 = GoalNode("Sub Goal 17", _equal_cost(x, y, num_agents))
    subgoal18 = GoalNode("Sub Goal 18", _equal_cost(x, y, num_agents))
    subgoal19 = GoalNode("Sub Goal 19", _equal_cost(x, y, num_agents))
    subgoal20 = GoalNode("Sub Goal 20", _equal_cost(x, y, num_agents))
    subgoal21 = GoalNode("Sub Goal 21", _equal_cost(x, y, num_agents))
    subgoal22 = GoalNode("Sub Goal 22", _equal_cost(x, y, num_agents))
    subgoal23 = GoalNode("Sub Goal 23", _equal_cost(x, y, num_agents))
    subgoal24 = GoalNode("Sub Goal 24", _equal_cost(x, y, num_agents))
    subgoal25 = GoalNode("Sub Goal 25", _equal_cost(x, y, num_agents))
    subgoal26 = GoalNode("Sub Goal 26", _equal_cost(x, y, num_agents))
    subgoal27 = GoalNode("Sub Goal 27", _equal_cost(x, y, num_agents))
    subgoal28 = GoalNode("Sub Goal 28", _equal_cost(x, y, num_agents))
    subgoal29 = GoalNode("Sub Goal 29", _equal_cost(x, y, num_agents))
    subgoal30 = GoalNode("Sub Goal 30", _equal_cost(x, y, num_agents))
    subgoal31 = GoalNode("Sub Goal 28", _equal_cost(x, y, num_agents))
    subgoal32 = GoalNode("Sub Goal 29", _equal_cost(x, y, num_agents))
    subgoal33 = GoalNode("Sub Goal 30", _equal_cost(x, y, num_agents))
    subgoal34 = GoalNode("Sub Goal 28", _equal_cost(x, y, num_agents))
    subgoal35 = GoalNode("Sub Goal 29", _equal_cost(x, y, num_agents))
    subgoal36 = GoalNode("Sub Goal 30", _equal_cost(x, y, num_agents))
    subgoal37 = GoalNode("Sub Goal 28", _equal_cost(x, y, num_agents))
    subgoal38 = GoalNode("Sub Goal 29", _equal_cost(x, y, num_agents))
    subgoal39 = GoalNode("Sub Goal 30", _equal_cost(x, y, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)

    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)

    subgoal4.add_child(subgoal13)
    subgoal4.add_child(subgoal14)
    subgoal4.add_child(subgoal15)
    subgoal5.add_child(subgoal16)
    subgoal5.add_child(subgoal17)
    subgoal5.add_child(subgoal18)
    subgoal6.add_child(subgoal19)
    subgoal6.add_child(subgoal20)
    subgoal6.add_child(subgoal21)
    subgoal7.add_child(subgoal22)
    subgoal7.add_child(subgoal23)
    subgoal7.add_child(subgoal24)
    subgoal8.add_child(subgoal25)
    subgoal8.add_child(subgoal26)
    subgoal8.add_child(subgoal27)
    subgoal9.add_child(subgoal28)
    subgoal9.add_child(subgoal29)
    subgoal9.add_child(subgoal30)
    subgoal10.add_child(subgoal31)
    subgoal10.add_child(subgoal32)
    subgoal10.add_child(subgoal33)
    subgoal11.add_child(subgoal34)
    subgoal11.add_child(subgoal35)
    subgoal11.add_child(subgoal36)
    subgoal12.add_child(subgoal37)
    subgoal12.add_child(subgoal38)
    subgoal12.add_child(subgoal39)

    return root

def equal_tree_1(num_agents):

    root = GoalNode("Main Goal", _equal_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(1, 8, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(1, 8, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(1, 8, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(1, 8, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(5, 15, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(5, 15, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(1, 6, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _equal_cost(1, 6, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _equal_cost(1, 6, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _equal_cost(1, 6, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)

    return root

def equal_tree_2(num_agents):

    root = GoalNode("Main Goal", _equal_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _equal_cost(6, 12, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _equal_cost(6, 12, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _equal_cost(6, 12, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _equal_cost(6, 12, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _equal_cost(3, 6, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _equal_cost(3, 6, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _equal_cost(3, 6, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _equal_cost(3, 6, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _equal_cost(3, 6, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _equal_cost(3, 6, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _equal_cost(3, 6, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _equal_cost(3, 6, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    root.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    return root

# Unequal Trees
def random_binary_symmetric(num_agents):

    root = GoalNode("Main Goal", _random_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 15, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 15, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def random_binary_left(num_agents):

    root = GoalNode("Main Goal", _random_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def random_binary_right(num_agents):

    root = GoalNode("Main Goal", _random_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    return root

def random_root(num_agents):

    root = root = GoalNode("Main Goal", _random_cost(25, 30, num_agents))

    return root

def random_tree_symmetric(num_agents):

    root = GoalNode("Main Goal", _random_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(5, 10, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(5, 10, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(5, 10, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    return root

def random_tree_left_right(num_agents):

    root = GoalNode("Main Goal", _random_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    return root

def random_large_binary_tree(num_agents):
    
    x = 40
    y = 60
    root = GoalNode("Main Goal", _random_cost(x, y, num_agents))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(x, y, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(x, y, num_agents))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(x, y, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(x, y, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(x, y, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(x, y, num_agents))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(x, y, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(x, y, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(x, y, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(x, y, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(x, y, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(x, y, num_agents))
    subgoal13 = GoalNode("Sub Goal 13", _random_cost(x, y, num_agents))
    subgoal14 = GoalNode("Sub Goal 14", _random_cost(x, y, num_agents))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_cost(x, y, num_agents)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_cost(x, y, num_agents))
    subgoal17 = GoalNode("Sub Goal 17", _random_cost(x, y, num_agents))
    subgoal18 = GoalNode("Sub Goal 18", _random_cost(x, y, num_agents))
    subgoal19 = GoalNode("Sub Goal 19", _random_cost(x, y, num_agents))
    subgoal20 = GoalNode("Sub Goal 20", _random_cost(x, y, num_agents))
    subgoal21 = GoalNode("Sub Goal 21", _random_cost(x, y, num_agents))
    subgoal22 = GoalNode("Sub Goal 22", _random_cost(x, y, num_agents))
    subgoal23 = GoalNode("Sub Goal 23", _random_cost(x, y, num_agents))
    subgoal24 = GoalNode("Sub Goal 24", _random_cost(x, y, num_agents))
    subgoal25 = GoalNode("Sub Goal 25", _random_cost(x, y, num_agents))
    subgoal26 = GoalNode("Sub Goal 26", _random_cost(x, y, num_agents))
    subgoal27 = GoalNode("Sub Goal 27", _random_cost(x, y, num_agents))
    subgoal28 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal29 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal30 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    return root

def random_large_tree(num_agents):

    x = 40
    y = 60
    root = GoalNode("Main Goal", _random_cost(x, y, num_agents))
    
    x = 13
    y = 20
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(x, y, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(x, y, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(x, y, num_agents))

    x = 4
    y = 7
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(x, y, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(x, y, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(x, y, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(x, y, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(x, y, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(x, y, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(x, y, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(x, y, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(x, y, num_agents))
    
    x = 1
    y = 3
    
    subgoal13 = GoalNode("Sub Goal 13", _random_cost(x, y, num_agents))
    subgoal14 = GoalNode("Sub Goal 14", _random_cost(x, y, num_agents))
    subgoal15 = GoalNode("Sub Goal 15", _random_cost(x, y, num_agents)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_cost(x, y, num_agents))
    subgoal17 = GoalNode("Sub Goal 17", _random_cost(x, y, num_agents))
    subgoal18 = GoalNode("Sub Goal 18", _random_cost(x, y, num_agents))
    subgoal19 = GoalNode("Sub Goal 19", _random_cost(x, y, num_agents))
    subgoal20 = GoalNode("Sub Goal 20", _random_cost(x, y, num_agents))
    subgoal21 = GoalNode("Sub Goal 21", _random_cost(x, y, num_agents))
    subgoal22 = GoalNode("Sub Goal 22", _random_cost(x, y, num_agents))
    subgoal23 = GoalNode("Sub Goal 23", _random_cost(x, y, num_agents))
    subgoal24 = GoalNode("Sub Goal 24", _random_cost(x, y, num_agents))
    subgoal25 = GoalNode("Sub Goal 25", _random_cost(x, y, num_agents))
    subgoal26 = GoalNode("Sub Goal 26", _random_cost(x, y, num_agents))
    subgoal27 = GoalNode("Sub Goal 27", _random_cost(x, y, num_agents))
    subgoal28 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal29 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal30 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    subgoal31 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal32 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal33 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    subgoal34 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal35 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal36 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    subgoal37 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal38 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal39 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)

    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)

    subgoal4.add_child(subgoal13)
    subgoal4.add_child(subgoal14)
    subgoal4.add_child(subgoal15)
    subgoal5.add_child(subgoal16)
    subgoal5.add_child(subgoal17)
    subgoal5.add_child(subgoal18)
    subgoal6.add_child(subgoal19)
    subgoal6.add_child(subgoal20)
    subgoal6.add_child(subgoal21)
    subgoal7.add_child(subgoal22)
    subgoal7.add_child(subgoal23)
    subgoal7.add_child(subgoal24)
    subgoal8.add_child(subgoal25)
    subgoal8.add_child(subgoal26)
    subgoal8.add_child(subgoal27)
    subgoal9.add_child(subgoal28)
    subgoal9.add_child(subgoal29)
    subgoal9.add_child(subgoal30)
    subgoal10.add_child(subgoal31)
    subgoal10.add_child(subgoal32)
    subgoal10.add_child(subgoal33)
    subgoal11.add_child(subgoal34)
    subgoal11.add_child(subgoal35)
    subgoal11.add_child(subgoal36)
    subgoal12.add_child(subgoal37)
    subgoal12.add_child(subgoal38)
    subgoal12.add_child(subgoal39)

    return root

def random_tree_1(num_agents):

    root = GoalNode("Main Goal", _random_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(1, 8, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(1, 8, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(1, 8, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(1, 8, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 15, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 15, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(1, 6, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(1, 6, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(1, 6, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(1, 6, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)

    return root

def random_tree_2(num_agents):

    root = GoalNode("Main Goal", _random_cost(30, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(6, 12, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(6, 12, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(6, 12, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(6, 12, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(3, 6, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(3, 6, num_agents))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(3, 6, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(3, 6, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(3, 6, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(3, 6, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(3, 6, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(3, 6, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    root.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    return root

# Scenario 1
def Test1(total_tests, seed):
    """
    3 agents
    Equal Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        TREES = [equal_binary_symmetric(3),
                 equal_binary_left(3), 
                 equal_binary_right(3), 
                 equal_root(3), 
                 equal_tree_symmetric(3), 
                 equal_tree_left_right(3), 
                 equal_large_binary_tree(3), 
                 equal_tree_1(3), 
                 equal_tree_2(3),
                 equal_large_tree(3)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 30, "remus": 30, "franklin": 30})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 2
def Test2(total_tests, seed):
    """
    3 agents
    Equal Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        TREES = [equal_binary_symmetric(3),
                 equal_binary_left(3), 
                 equal_binary_right(3), 
                 equal_root(3), 
                 equal_tree_symmetric(3), 
                 equal_tree_left_right(3), 
                 equal_large_binary_tree(3), 
                 equal_tree_1(3), 
                 equal_tree_2(3),
                 equal_large_tree(3)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 20, "remus": 15, "franklin": 25})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 3
def Test3(total_tests, seed):
    """
    3 agents
    Varying Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        TREES = [random_binary_symmetric(3),
                 random_binary_left(3), 
                 random_binary_right(3), 
                 random_root(3), 
                 random_tree_symmetric(3), 
                 random_tree_left_right(3), 
                 random_large_binary_tree(3), 
                 random_tree_1(3), 
                 random_tree_2(3),
                 random_large_tree(3)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 30, "remus": 30, "franklin": 30})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 4
def Test4(total_tests, seed):
    """
    3 agents
    Varying Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        TREES = [random_binary_symmetric(3),
                 random_binary_left(3), 
                 random_binary_right(3), 
                 random_root(3), 
                 random_tree_symmetric(3), 
                 random_tree_left_right(3), 
                 random_large_binary_tree(3), 
                 random_tree_1(3), 
                 random_tree_2(3),
                 random_large_tree(3)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 20, "remus": 15, "franklin": 25})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 5
def Test5(total_tests, seed):
    """
    Varying agents
    Equal Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        num_agents += 1
        TREES = [equal_binary_symmetric(num_agents),
                 equal_binary_left(num_agents), 
                 equal_binary_right(num_agents), 
                 equal_root(num_agents), 
                 equal_tree_symmetric(num_agents), 
                 equal_tree_left_right(num_agents), 
                 equal_large_binary_tree(num_agents), 
                 equal_tree_1(num_agents), 
                 equal_tree_2(num_agents),
                 equal_large_tree(num_agents)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 30, "remus": 30, "franklin": 30, "john": 30, "alice": 30, "jake": 30, "anna": 30, "tommy": 30, "trent": 30, "karen": 30})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 6
def Test6(total_tests, seed):
    """
    Varying agents
    Equal Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        num_agents += 1
        TREES = [equal_binary_symmetric(num_agents),
                 equal_binary_left(num_agents), 
                 equal_binary_right(num_agents), 
                 equal_root(num_agents), 
                 equal_tree_symmetric(num_agents), 
                 equal_tree_left_right(num_agents), 
                 equal_large_binary_tree(num_agents), 
                 equal_tree_1(num_agents), 
                 equal_tree_2(num_agents),
                 equal_large_tree(num_agents)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 20, "remus": 15, "franklin": 20, "john": 30, "alice": 32, "jake": 24, "anna": 17, "tommy": 21, "trent": 28, "karen": 10})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 7
def Test7(total_tests, seed):
    """
    Varying agents
    Varying Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        num_agents += 1
        TREES = [random_binary_symmetric(num_agents),
                 random_binary_left(num_agents), 
                 random_binary_right(num_agents), 
                 random_root(num_agents), 
                 random_tree_symmetric(num_agents), 
                 random_tree_left_right(num_agents), 
                 random_large_binary_tree(num_agents), 
                 random_tree_1(num_agents), 
                 random_tree_2(num_agents),
                 random_large_tree(num_agents)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 30, "remus": 30, "franklin": 30, "john": 30, "alice": 30, "jake": 30, "anna": 30, "tommy": 30, "trent": 30, "karen": 30})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Scenario 8
def Test8(total_tests, seed):
    """
    Varying agents
    Varandom Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_tests):
        r.seed(curr_seed)
        num_agents += 1
        TREES = [random_binary_symmetric(num_agents),
                 random_binary_left(num_agents), 
                 random_binary_right(num_agents), 
                 random_root(num_agents), 
                 random_tree_symmetric(num_agents), 
                 random_tree_left_right(num_agents), 
                 random_large_binary_tree(num_agents), 
                 random_tree_1(num_agents), 
                 random_tree_2(num_agents),
                 random_large_tree(num_agents)]

        curr_avg_cost = 0
        curr_failures = []
        num_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            root = TREES[tree_idx]

            try:
                dfs_agents_and_goals = dfs_goal_allocation(root, {"grace": 20, "remus": 15, "franklin": 20, "john": 30, "alice": 32, "jake": 24, "anna": 17, "tommy": 21, "trent": 28, "karen": 10})
                curr_avg_cost += get_total_cost(dfs_agents_and_goals)
                num_trees_passed += 1
            except ValueError:
                curr_failures.append(test_num)

        if num_trees_passed != 0:
            dfs_avg_costs.append(curr_avg_cost / num_trees_passed)
            fails.append(curr_failures)
        else:
            dfs_avg_costs.append(0)
            fails.append(curr_failures)

        curr_seed += 1

    return dfs_avg_costs, fails

# Plot Results
def plot_results(scenario, avg_costs, fails):

    for i in range(len(avg_costs)):
        print(f"Test {i}: {avg_costs[i]}, {fails[i]}")

    # Data for the bar chart
    num_tests = range(1, len(avg_costs) + 1)

    # Create the bar chart
    plt.bar(num_tests, avg_costs)

    plt.xticks(num_tests, [f'F: {len(i)}' for i in fails])

    # Add labels and title
    plt.xlabel('Test Group and Failed Trees')
    plt.ylabel('Average Cost')
    plt.title(f'Scenario {scenario}')

    # Display the chart
    plt.show()

def main():
    
    avg_costs1, fails1 = Test1(10, 1)
    plot_results(1, avg_costs1, fails1)

    avg_costs2, fails2 = Test2(10, 1)
    plot_results(2, avg_costs2, fails2)

    avg_costs3, fails3 = Test3(10, 1)
    plot_results(3, avg_costs3, fails3)

    avg_costs4, fails4 = Test4(10, 1)
    plot_results(4, avg_costs4, fails4)

    avg_costs5, fails5 = Test5(10, 1)
    plot_results(5, avg_costs5, fails5)

    avg_costs6, fails6 = Test6(10, 1)
    plot_results(6, avg_costs6, fails6)
    
    avg_costs7, fails7 = Test7(10, 1)
    plot_results(7, avg_costs7, fails7)

    avg_costs8, fails8 = Test8(10, 1)
    plot_results(8, avg_costs8, fails8)

if __name__ == '__main__':
    main()
