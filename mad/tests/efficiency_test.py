from mad.data_structures import GoalNode, GoalNode2, level_order_transversal
from mad.optimize import optimized_goal_allocation, dfs_goal_allocation
from typing import Dict, Tuple, List
import random
import copy
import numpy as np
import matplotlib.pyplot as plt



def _random_cost(m: int, n: int, agents: int = 3) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        The starting point of the range
    n: int
        The ending point of the range
    agents: int
        Number of available agents
    
    Returns
    -------
    
    Dict[str,int]
        A dictionary with the agents as keys and corresponding costs as values
    
    """
    
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy"]

    d = {}
    for i in range(agents):
        d[AGENTS[i]] = random.randint(m,n)

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
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy"]

    d = {}
    cost = random.randint(m,n)
    for i in range(agents):
        d[AGENTS[i]] = cost

    return d


#RANDOM TREES

def random_binary_symmetric(num_agents = 3):

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

def random_binary_left(num_agents = 3):

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

def random_binary_right(num_agents = 3):

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

def random_root(num_agents = 3):

    root = root = GoalNode("Main Goal", _random_cost(25, 30, num_agents))

    return root

def random_tree_symmetric(num_agents = 3):

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

def random_tree_left_right(num_agents = 3):

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

def random_large_binary_tree(num_agents = 3):
    
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

def random_large_tree(num_agents = 3):

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

def random_tree_1(num_agents = 3):

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

def random_tree_2(num_agents = 3):

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

#EQUAL TREES

def equal_binary_symmetric(num_agents = 3):

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

def equal_binary_left(num_agents = 3):

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

def equal_binary_right(num_agents = 3):

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

def equal_root(num_agents = 3):

    root = root = GoalNode("Main Goal", _equal_cost(25, 45, num_agents))

    return root

def equal_tree_symmetric(num_agents = 3):

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

def equal_tree_left_right(num_agents = 3):

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

def equal_large_binary_tree(num_agents = 3):
    
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

def equal_large_tree(num_agents = 3):

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

def equal_tree_1(num_agents = 3):

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

def equal_tree_2(num_agents = 3):

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

#__RUNNING THE EFFICIENCY TEST AND PLOTTING__
def efficiency_test(goal_tree, max_res: List):
    
    level_order_transversal(goal_tree)

    AGENT = list(goal_tree.data.keys())
    
    max_resources_j = {}
    max_resources_f = max_res
    for i in range(len(AGENT)):
        max_resources_j[AGENT[i]] = max_res[i]

    print(max_resources_f, "\n", max_resources_j)

    #__FAY'S ALGORITHM__
    print("\nFay's Algorithm:\n")

    goal_tree2 = copy.deepcopy(goal_tree)

    q = []
    q.append((goal_tree2, None)) 

    while len(q) != 0:
        level_size = len(q)

        while len(q) > 0:  
            node, parent = q.pop(0)
            node.initial_agent_assign()
            children = node.get_children()
            for child in children:
                q.append((child, node)) 
    
    result = optimized_goal_allocation(goal_tree2, max_resources_f)
    if result:
        fresult, fresources = result
    # Rest of the code to process jresult and include it in the total
    else:
        return
    
    f_agent_cost = []
    f_agent_goals = []
    
    f_total_resources = 0

    for _ in range(len(AGENT)):
        f_agent_cost.append(0)
        f_agent_goals.append(0)

    for agent, goals in fresult.items():
        for goal in goals:
            print(goal.name + ": " + agent + " " + str(goal.cost))
            f_total_resources += goal.cost
            i = AGENT.index(agent)
            f_agent_cost[i] += goal.cost
            f_agent_goals[i] += 1


    

    #__JONATHAN'S ALGORITHM__
    goal_tree1 = copy.deepcopy(goal_tree)
    print("\n\nJonathan's Algorithm:")
    try:
        jresult = dfs_goal_allocation(goal_tree1, max_resources_j, 0)
    except ValueError as e:
        # Handle the error raised in the inner function of dfs_goal_allocation()
        print(f"Error encountered in inner function of dfs_goal_allocation(): {str(e)}")
        return

    j_agent_cost = []
    j_agent_goals = []

    j_total_resources = 0

    for _ in range(len(AGENT)):
        j_agent_cost.append(0)
        j_agent_goals.append(0)

    # Get the number of goals each agent assigned and cost consumed
    for agent, goals in jresult.items():
        for goal in goals:
            print(goal.name + ": " + agent + " " + str(goal.cost))
            j_total_resources += goal.cost
            i = AGENT.index(agent)
            j_agent_cost[i] += goal.cost
            j_agent_goals[i] += 1
    
    return f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total_resources, j_total_resources, AGENT

        
def bar_chart_plotting(Results: Tuple, title):
    # Define the algorithm names and total resource utilization values
    algorithm_names = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm']

    f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total_resources, j_total_resources, AGENTS = Results

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # Plot 1: Resource Cost Comparison
    # Set the positions of the bars on the x-axis
    x = np.arange(len(f_agent_goals))

    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, j_agent_cost, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, f_agent_cost, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(j_agent_cost), max(f_agent_cost)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Agents')
    ax1.set_ylabel('Resource Cost')
    ax1.set_title(f'{title} - COST COMPARISON BY AGENT')
    ax1.set_xticks(x + bar_width / 2)
    ax1.set_xticklabels(AGENTS)
    ax1.legend()

    # Add annotations for the resource cost
    for rect in rects1:
        height = rect.get_height()
        ax1.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    for rect in rects2:
        height = rect.get_height()
        ax1.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        

    # Plot 2: Goal Count Comparison

    rects3 = ax2.bar(x, j_agent_goals, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax2.bar(x + bar_width, f_agent_goals, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    ax2.set_ylim(0, max(max(j_agent_goals), max(f_agent_goals)) + 5)
    # Set the labels and title
    ax2.set_xlabel('Agents')
    ax2.set_ylabel('Number of Goals')
    ax2.set_title(f'{title} - COST COMPARISON BY AGENT')
    ax2.set_xticks(x + bar_width / 2)
    ax2.set_xticklabels(AGENTS)
    ax2.legend()

    # Add annotations for the resource cost
    for rect in rects3:
        height = rect.get_height()
        ax2.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    for rect in rects4:
        height = rect.get_height()
        ax2.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=1)  # Increase the hspace value to increase spacing between subplots
    plt.show()
    
def plot_stacked_bar_chart(fay_averages, jonathan_averages, iteration, scenario):
    # Color of each algorithm
    colors = ['peachpuff', 'lightblue', 'khaki']
    algorithms = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm', 'Maheen\'s Algorithm']

    # Plot the stacked bar chart
    x = range(1, iteration + 2) 
    # width of the bars
    width = 0.1 
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the bars for Fay's averages
    ax.bar(x, fay_averages, width, label="Fay's Algorithm", color=colors[0])

    # Plot the bars for Jonathan's averages
    ax.bar(x, jonathan_averages, width, bottom=fay_averages, label="Jonathan's Algorithm", color=colors[1])

    # Add labels and title
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Efficiency')
    ax.set_title(scenario)
    ax.set_xticks(x)
    ax.legend()

    # Add annotations to each stack of the bars
    for i in range(len(x)):
        fay_value = fay_averages[i]
        jonathan_value = jonathan_averages[i]
        total_value = fay_value + jonathan_value

        # Calculate the center position of the stack for each algorithm
        fay_center = fay_value / 2
        jonathan_center = fay_value + jonathan_value / 2

        # Add the annotations at the center positions
        ax.annotate(f"{fay_value:.2f}",
                    xy=(x[i], fay_center),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    va='bottom')

        ax.annotate(f"{jonathan_value:.2f}",
                    xy=(x[i], jonathan_center),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    va='bottom')

    plt.show()
   

def main():
    test_cases = [[(random_binary_symmetric, "RANDOM BINARY SYMMETRIC TREE"),
        (random_binary_left, "RANDOM BINARY LEFT TREE"),
        (random_binary_right, "RANDOM BINARY RIGHT TREE"),
        (random_root, "RANDOM ROOT-ONLY TREE"),
        (random_tree_symmetric, "RANDOM SYMMETRIC TREE"),
        (random_tree_left_right, "RANDOM LEFT RIGHT TREE"),
        (random_large_binary_tree, "RANDOM LARGE BINARY TREE"),
        (random_large_tree, "RANDOM LARGE TREE"),
        (random_tree_1, "RANDOM TREE 1"),
        (random_tree_2, "RANDOM TREE 2"),],
        [(equal_binary_symmetric, "EQUAL BINARY SYMMETRIC TREE"),
        (equal_binary_left, "EQUAL BINARY LEFT TREE"),
        (equal_binary_right, "EQUAL BINARY RIGHT TREE"),
        (equal_root, "EQUAL ROOT-ONLY TREE"),
        (equal_tree_symmetric, "EQUAL SYMMETRIC TREE"),
        (equal_tree_left_right, "EQUAL LEFT RIGHT TREE"),
        (equal_large_binary_tree, "EQUAL LARGE BINARY TREE"),
        (equal_large_tree, "EQUAL LARGE TREE"),
        (equal_tree_1, "EQUAL TREE 1"),
        (equal_tree_2, "EQUAL TREE 2"),]
   
    ]

    # Color of each algorithm
    colors = ['peachpuff', 'lightblue', 'khaki']
    algorithms = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm', 'Maheen\'s Algorithm']
    
    """
        SCENARIO 1: 
            - Same agent cost
            - Ten trees
            - 3 Agents

    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_1_a = "Same Agent Cost - 3 Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[1]):
            tree = generate_tree()
            
            # Run each goal tree
            result = efficiency_test(tree, [40,40,40])
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_1_a)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_1_b = "Same Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[1]):
            tree = generate_tree()
            
            # Run each goal tree
            result = efficiency_test(tree, [20,40,60])
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_1_b)


    """
        SCENARIO 2: 
        - Various agent cost
        - Ten trees
        - 3 Agents
    """

    # SUB CASE: SAME MAX RESOURCES
    scenario_2_a = "Random Agent Cost - 3 Agents - Same Max Resources"
    # Test for 10 times each scenario
    starting, ending = 3, 5
    max_res_starting = 20
    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[0]):
            # Exclude the equal agent cost tree
            tree = generate_tree()
            
            # Run each goal tree
            result = efficiency_test(tree, [40,40,40])
            if not result:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)

    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_2_a)
        
    # SUB CASE: DIFFERENT MAX RESOURCES
    scenario_2_b = "Random Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[0]):
            # Exclude the equal agent cost tree
            tree = generate_tree()
            
            # Run each goal tree
            result = efficiency_test(tree, [20,40,60])            
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)

    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_2_b)


    """
        SCENARIO 3: 
        - Vary number of agents
        - Ten trees -> hundred trees
        - Same agent cost

    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_3_a = "Same Agent Cost - Many Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0
        for i, (generate_tree, title) in enumerate(test_cases[1]):
            no_agents = random.randint(3,8)
            tree = generate_tree(no_agents)

            # Run each goal tree
            result = efficiency_test(tree, [25] * no_agents)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_3_a)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_3_b = "Same Agent Cost - Many Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[1]):
            no_agents = random.randint(3,8)
            tree = generate_tree(no_agents)
            # Provide different max resources to each agent
            starting_resources = 15
            resources = []
            for _ in range(no_agents):
                resources.append(starting_resources)
                starting_resources += 5
            result = efficiency_test(tree, resources)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_3_b)


    """
        SCENARIO 4: 
        - Vary number of agents
        - Ten trees -> hundred trees
        - Vary agent cost

    """
    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_4_a = "Different Agent Cost - Many Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[0]):
            no_agents = random.randint(3,8)
            tree = generate_tree(no_agents)
            # Run each goal tree
            result = efficiency_test(tree, [25] * no_agents)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_4_a)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_4_b = "Different Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        no_trees = 0

        for i, (generate_tree, title) in enumerate(test_cases[0]):
            no_agents = random.randint(3,8)
            tree = generate_tree(no_agents)
            # Provide different max resources to each agent
            starting_resources = 15
            resources = []
            for _ in range(no_agents):
                resources.append(starting_resources)
                starting_resources += 5
            result = efficiency_test(tree, resources)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees

        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        
    plot_stacked_bar_chart(fay_averages, jonathan_averages, j, scenario_4_b)

        
if __name__ == "__main__":
    main()


