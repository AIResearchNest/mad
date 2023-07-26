from mad.data_structures import GoalNode, GoalNode2, level_order_transversal, level_order_transversal_two
from mad.optimize._goal_allocation import optimized_goal_allocation, dfs_goal_allocation, cost_node, agent_goal_m
from typing import Dict, Tuple, List
import random
import copy
import numpy as np
import matplotlib.pyplot as plt



def _random_cost(m: int, n: int, agents: int) -> Dict[str, int]:
    
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
    
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "julia", "rose"]
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
    
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "julia", "Rose"]
    d = {}
    cost = random.randint(m,n)
    for i in range(agents):
        d[AGENTS[i]] = cost

    return d

# Trees
def binary_symmetric(random=False, num_agents = 3):
    if random:
        root_agents = _random_cost(25, 45, num_agents)
        subgoal1_agents = _random_cost(15, 20, num_agents)
        subgoal2_agents = _random_cost(15, 20, num_agents)
        subgoal3_agents = _random_cost(5, 15, num_agents)
        subgoal4_agents = _random_cost(5, 15, num_agents)
        subgoal5_agents = _random_cost(5, 15, num_agents)
        subgoal6_agents = _random_cost(5, 15, num_agents)
    else:
        root_agents = _equal_cost(25, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 20, num_agents)
        subgoal2_agents = _equal_cost(15, 20, num_agents)
        subgoal3_agents = _equal_cost(5, 15, num_agents)
        subgoal4_agents = _equal_cost(5, 15, num_agents)
        subgoal5_agents = _equal_cost(5, 15, num_agents)
        subgoal6_agents = _equal_cost(5, 15, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0 )
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0 )
    subgoal6m = GoalNode2("Sub Goal 6", 0 )

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    subgoal1m.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal2m.add_child(subgoal5m)
    subgoal2m.add_child(subgoal6m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)

    return (root,rootm)

def binary_left(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(25, 45, num_agents)
        subgoal1_agents = _random_cost(15, 20, num_agents)
        subgoal2_agents = _random_cost(15, 20, num_agents)
        subgoal3_agents = _random_cost(5, 15, num_agents)
        subgoal4_agents = _random_cost(5, 15, num_agents)
    else:
        root_agents = _equal_cost(25, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 20, num_agents)
        subgoal2_agents = _equal_cost(15, 20, num_agents)
        subgoal3_agents = _equal_cost(5, 15, num_agents)
        subgoal4_agents = _equal_cost(5, 15, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0 )
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    subgoal1m.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)

    return (root,rootm)

def binary_right(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(25, 45, num_agents)
        subgoal1_agents = _random_cost(15, 20, num_agents)
        subgoal2_agents = _random_cost(15, 20, num_agents)
        subgoal3_agents = _random_cost(5, 15, num_agents)
        subgoal4_agents = _random_cost(5, 15, num_agents)
    else:
        root_agents = _equal_cost(25, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 20, num_agents)
        subgoal2_agents = _equal_cost(15, 20, num_agents)
        subgoal3_agents = _equal_cost(5, 15, num_agents)
        subgoal4_agents = _equal_cost(5, 15, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0 )
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    subgoal2m.add_child(subgoal3m)
    subgoal2m.add_child(subgoal4m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)

    return (root,rootm)

def root(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(25, 45, num_agents)
    else:
        root_agents = _equal_cost(25, 45, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)

    rootm.agents = root_agents

    cost_node(rootm)

    return (root,rootm)

def tree_symmetric (random=False, num_agents = 3):
    if random:
        root_agents = _random_cost(30, 45, num_agents)
        subgoal1_agents = _random_cost(15, 25, num_agents)
        subgoal2_agents = _random_cost(15, 25, num_agents)
        subgoal3_agents = _random_cost(15, 25, num_agents)
        subgoal4_agents = _random_cost(5, 10, num_agents)
        subgoal5_agents = _random_cost(5, 10, num_agents)
        subgoal6_agents = _random_cost(5, 10, num_agents)
        subgoal7_agents = _random_cost(5, 10, num_agents)
        subgoal8_agents = _random_cost(5, 10, num_agents)
        subgoal9_agents = _random_cost(5, 10, num_agents)
        subgoal10_agents = _random_cost(5, 10, num_agents)
        subgoal11_agents = _random_cost(5, 10, num_agents)
        subgoal12_agents = _random_cost(5, 10, num_agents)
    else:
        root_agents = _equal_cost(30, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 25, num_agents)
        subgoal2_agents = _equal_cost(15, 25, num_agents)
        subgoal3_agents = _equal_cost(15, 25, num_agents)
        subgoal4_agents = _equal_cost(5, 10, num_agents)
        subgoal5_agents = _equal_cost(5, 10, num_agents)
        subgoal6_agents = _equal_cost(5, 10, num_agents)
        subgoal7_agents = _equal_cost(5, 10, num_agents)
        subgoal8_agents = _equal_cost(5, 10, num_agents)
        subgoal9_agents = _equal_cost(5, 10, num_agents)
        subgoal10_agents = _equal_cost(5, 10, num_agents)
        subgoal11_agents = _equal_cost(5, 10, num_agents)
        subgoal12_agents = _equal_cost(5, 10, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)
    subgoal10 = GoalNode("Sub Goal 10", subgoal10_agents)
    subgoal11 = GoalNode("Sub Goal 11", subgoal11_agents)
    subgoal12 = GoalNode("Sub Goal 12", subgoal12_agents)

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

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)
    subgoal10m = GoalNode2("Sub Goal 10", 0)
    subgoal11m = GoalNode2("Sub Goal 11", 0)
    subgoal12m = GoalNode2("Sub Goal 12", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    rootm.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal1m.add_child(subgoal5m)
    subgoal1m.add_child(subgoal6m)
    subgoal2m.add_child(subgoal7m)
    subgoal2m.add_child(subgoal8m)
    subgoal2m.add_child(subgoal9m)
    subgoal3m.add_child(subgoal10m)
    subgoal3m.add_child(subgoal11m)
    subgoal3m.add_child(subgoal12m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents
    subgoal10m.agents = subgoal10_agents
    subgoal11m.agents = subgoal11_agents
    subgoal12m.agents = subgoal12_agents


    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)
    cost_node(subgoal10m)
    cost_node(subgoal11m)
    cost_node(subgoal12m)

    return (root,rootm)

def tree_left_right(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(30, 45, num_agents)
        subgoal1_agents = _random_cost(15, 25, num_agents)
        subgoal2_agents = _random_cost(15, 25, num_agents)
        subgoal3_agents = _random_cost(15, 25, num_agents)
        subgoal4_agents = _random_cost(5, 10, num_agents)
        subgoal5_agents = _random_cost(5, 10, num_agents)
        subgoal6_agents = _random_cost(5, 10, num_agents)
        subgoal7_agents = _random_cost(5, 10, num_agents)
        subgoal8_agents = _random_cost(5, 10, num_agents)
        subgoal9_agents = _random_cost(5, 10, num_agents)
    else:
        root_agents = _equal_cost(30, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 25, num_agents)
        subgoal2_agents = _equal_cost(15, 25, num_agents)
        subgoal3_agents = _equal_cost(15, 25, num_agents)
        subgoal4_agents = _equal_cost(5, 10, num_agents)
        subgoal5_agents = _equal_cost(5, 10, num_agents)
        subgoal6_agents = _equal_cost(5, 10, num_agents)
        subgoal7_agents = _equal_cost(5, 10, num_agents)
        subgoal8_agents = _equal_cost(5, 10, num_agents)
        subgoal9_agents = _equal_cost(5, 10, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    rootm.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal1m.add_child(subgoal5m)
    subgoal1m.add_child(subgoal6m)
    subgoal3m.add_child(subgoal7m)
    subgoal3m.add_child(subgoal8m)
    subgoal3m.add_child(subgoal9m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)

    return (root,rootm)

def large_binary_tree(random = False, num_agents = 3):
    
    if random:
        root_agents = _random_cost(40, 60, num_agents)
        subgoal1_agents = _random_cost(23, 30, num_agents)
        subgoal2_agents = _random_cost(23, 30, num_agents)
        subgoal3_agents = _random_cost(10, 20, num_agents)
        subgoal4_agents = _random_cost(10, 20, num_agents)
        subgoal5_agents = _random_cost(10, 20, num_agents)
        subgoal6_agents = _random_cost(10, 20, num_agents)
        subgoal7_agents = _random_cost(5, 10, num_agents)
        subgoal8_agents = _random_cost(5, 10, num_agents)
        subgoal9_agents = _random_cost(5, 10, num_agents)
        subgoal10_agents = _random_cost(5, 10, num_agents)
        subgoal11_agents = _random_cost(5, 10, num_agents)
        subgoal12_agents = _random_cost(5, 10, num_agents)
        subgoal13_agents = _random_cost(5, 10, num_agents)
        subgoal14_agents = _random_cost(5, 10, num_agents)
        subgoal15_agents = _random_cost(3, 6, num_agents)
        subgoal16_agents = _random_cost(3, 6, num_agents)
        subgoal17_agents = _random_cost(3, 6, num_agents)
        subgoal18_agents = _random_cost(3, 6, num_agents)
        subgoal19_agents = _random_cost(3, 6, num_agents)
        subgoal20_agents = _random_cost(3, 6, num_agents)
        subgoal21_agents = _random_cost(3, 6, num_agents)
        subgoal22_agents = _random_cost(3, 6, num_agents)
        subgoal23_agents = _random_cost(3, 6, num_agents)
        subgoal24_agents = _random_cost(3, 6, num_agents)
        subgoal25_agents = _random_cost(3, 6, num_agents)
        subgoal26_agents = _random_cost(3, 6, num_agents)
        subgoal27_agents = _random_cost(3, 6, num_agents)
        subgoal28_agents = _random_cost(3, 6, num_agents)
        subgoal29_agents = _random_cost(3, 6, num_agents)
        subgoal30_agents = _random_cost(3, 6, num_agents)
    else:
        root_agents = _equal_cost(40, 60, num_agents)
        subgoal1_agents = _equal_cost(23, 30, num_agents)
        subgoal2_agents = _equal_cost(23, 30, num_agents)
        subgoal3_agents = _equal_cost(10, 20, num_agents)
        subgoal4_agents = _equal_cost(10, 20, num_agents)
        subgoal5_agents = _equal_cost(10, 20, num_agents)
        subgoal6_agents = _equal_cost(10, 20, num_agents)
        subgoal7_agents = _equal_cost(5, 10, num_agents)
        subgoal8_agents = _equal_cost(5, 10, num_agents)
        subgoal9_agents = _equal_cost(5, 10, num_agents)
        subgoal10_agents = _equal_cost(5, 10, num_agents)
        subgoal11_agents = _equal_cost(5, 10, num_agents)
        subgoal12_agents = _equal_cost(5, 10, num_agents)
        subgoal13_agents = _equal_cost(5, 10, num_agents)
        subgoal14_agents = _equal_cost(5, 10, num_agents)
        subgoal15_agents = _equal_cost(3, 6, num_agents)
        subgoal16_agents = _equal_cost(3, 6, num_agents)
        subgoal17_agents = _equal_cost(3, 6, num_agents)
        subgoal18_agents = _equal_cost(3, 6, num_agents)
        subgoal19_agents = _equal_cost(3, 6, num_agents)
        subgoal20_agents = _equal_cost(3, 6, num_agents)
        subgoal21_agents = _equal_cost(3, 6, num_agents)
        subgoal22_agents = _equal_cost(3, 6, num_agents)
        subgoal23_agents = _equal_cost(3, 6, num_agents)
        subgoal24_agents = _equal_cost(3, 6, num_agents)
        subgoal25_agents = _equal_cost(3, 6, num_agents)
        subgoal26_agents = _equal_cost(3, 6, num_agents)
        subgoal27_agents = _equal_cost(3, 6, num_agents)
        subgoal28_agents = _equal_cost(3, 6, num_agents)
        subgoal29_agents = _equal_cost(3, 6, num_agents)
        subgoal30_agents = _equal_cost(3, 6, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)
    subgoal10 = GoalNode("Sub Goal 10", subgoal10_agents)
    subgoal11 = GoalNode("Sub Goal 11", subgoal11_agents)
    subgoal12 = GoalNode("Sub Goal 12", subgoal12_agents)
    subgoal13 = GoalNode("Sub Goal 13", subgoal13_agents)
    subgoal14 = GoalNode("Sub Goal 14", subgoal14_agents)
    subgoal15 = GoalNode("Sub Goal 15", subgoal15_agents) 
    subgoal16 = GoalNode("Sub Goal 16", subgoal16_agents)
    subgoal17 = GoalNode("Sub Goal 17", subgoal17_agents)
    subgoal18 = GoalNode("Sub Goal 18", subgoal18_agents)
    subgoal19 = GoalNode("Sub Goal 19", subgoal19_agents)
    subgoal20 = GoalNode("Sub Goal 20", subgoal20_agents)
    subgoal21 = GoalNode("Sub Goal 21", subgoal21_agents)
    subgoal22 = GoalNode("Sub Goal 22", subgoal22_agents)
    subgoal23 = GoalNode("Sub Goal 23", subgoal23_agents)
    subgoal24 = GoalNode("Sub Goal 24", subgoal24_agents)
    subgoal25 = GoalNode("Sub Goal 25", subgoal25_agents)
    subgoal26 = GoalNode("Sub Goal 26", subgoal26_agents)
    subgoal27 = GoalNode("Sub Goal 27", subgoal27_agents)
    subgoal28 = GoalNode("Sub Goal 28", subgoal28_agents)
    subgoal29 = GoalNode("Sub Goal 29", subgoal29_agents)
    subgoal30 = GoalNode("Sub Goal 30", subgoal30_agents)
    
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

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)
    subgoal10m = GoalNode2("Sub Goal 10", 0)
    subgoal11m = GoalNode2("Sub Goal 11", 0)
    subgoal12m = GoalNode2("Sub Goal 12", 0)
    subgoal13m = GoalNode2("Sub Goal 13", 0)
    subgoal14m = GoalNode2("Sub Goal 14", 0)
    subgoal15m = GoalNode2("Sub Goal 15", 0)
    subgoal16m = GoalNode2("Sub Goal 16", 0)
    subgoal17m = GoalNode2("Sub Goal 17", 0)
    subgoal18m = GoalNode2("Sub Goal 18", 0)
    subgoal19m = GoalNode2("Sub Goal 19", 0)
    subgoal20m = GoalNode2("Sub Goal 20", 0)
    subgoal21m = GoalNode2("Sub Goal 21", 0)
    subgoal22m = GoalNode2("Sub Goal 22", 0)
    subgoal23m = GoalNode2("Sub Goal 23", 0)
    subgoal24m = GoalNode2("Sub Goal 24", 0)
    subgoal25m = GoalNode2("Sub Goal 25", 0)
    subgoal26m = GoalNode2("Sub Goal 26", 0)
    subgoal27m = GoalNode2("Sub Goal 27", 0)
    subgoal28m = GoalNode2("Sub Goal 28", 0)
    subgoal29m = GoalNode2("Sub Goal 29", 0)
    subgoal30m = GoalNode2("Sub Goal 30", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    subgoal1m.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal2m.add_child(subgoal5m)
    subgoal2m.add_child(subgoal6m)
    subgoal3m.add_child(subgoal7m)
    subgoal3m.add_child(subgoal8m)
    subgoal4m.add_child(subgoal9m)
    subgoal4m.add_child(subgoal10m)
    subgoal5m.add_child(subgoal11m)
    subgoal5m.add_child(subgoal12m)
    subgoal6m.add_child(subgoal13m)
    subgoal6m.add_child(subgoal14m)
    subgoal7m.add_child(subgoal15m)
    subgoal7m.add_child(subgoal16m)
    subgoal8m.add_child(subgoal17m)
    subgoal8m.add_child(subgoal18m)
    subgoal9m.add_child(subgoal19m)
    subgoal9m.add_child(subgoal20m)
    subgoal10m.add_child(subgoal21m)
    subgoal10m.add_child(subgoal22m)
    subgoal11m.add_child(subgoal23m)
    subgoal11m.add_child(subgoal24m)
    subgoal12m.add_child(subgoal25m)
    subgoal12m.add_child(subgoal26m)
    subgoal13m.add_child(subgoal27m)
    subgoal13m.add_child(subgoal28m)
    subgoal14m.add_child(subgoal29m)
    subgoal14m.add_child(subgoal30m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents
    subgoal10m.agents = subgoal10_agents
    subgoal11m.agents = subgoal11_agents
    subgoal12m.agents = subgoal12_agents
    subgoal13m.agents = subgoal13_agents
    subgoal14m.agents = subgoal14_agents
    subgoal15m.agents = subgoal15_agents
    subgoal16m.agents = subgoal16_agents
    subgoal17m.agents = subgoal17_agents
    subgoal18m.agents = subgoal18_agents
    subgoal19m.agents = subgoal19_agents
    subgoal20m.agents = subgoal20_agents
    subgoal21m.agents = subgoal21_agents
    subgoal22m.agents = subgoal22_agents
    subgoal23m.agents = subgoal23_agents
    subgoal24m.agents = subgoal24_agents
    subgoal25m.agents = subgoal25_agents
    subgoal26m.agents = subgoal26_agents
    subgoal27m.agents = subgoal27_agents
    subgoal28m.agents = subgoal28_agents
    subgoal29m.agents = subgoal29_agents
    subgoal30m.agents = subgoal30_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)
    cost_node(subgoal10m)
    cost_node(subgoal11m)
    cost_node(subgoal12m)
    cost_node(subgoal13m)
    cost_node(subgoal14m)
    cost_node(subgoal15m)
    cost_node(subgoal16m)
    cost_node(subgoal17m)
    cost_node(subgoal18m)
    cost_node(subgoal19m)
    cost_node(subgoal20m)
    cost_node(subgoal21m)
    cost_node(subgoal22m)
    cost_node(subgoal23m)
    cost_node(subgoal24m)
    cost_node(subgoal25m)
    cost_node(subgoal26m)
    cost_node(subgoal27m)
    cost_node(subgoal28m)
    cost_node(subgoal29m)
    cost_node(subgoal30m)

    return (root,rootm)

def large_tree(random = False, num_agents = 3):
    
    if random:
        root_agents = _random_cost(40, 60, num_agents)
        subgoal1_agents = _random_cost(13, 20, num_agents)
        subgoal2_agents = _random_cost(13, 20, num_agents)
        subgoal3_agents = _random_cost(13, 20, num_agents)
        subgoal4_agents = _random_cost(4, 7, num_agents)
        subgoal5_agents = _random_cost(4, 7, num_agents)
        subgoal6_agents = _random_cost(4, 7, num_agents)
        subgoal7_agents = _random_cost(4, 7, num_agents)
        subgoal8_agents = _random_cost(4, 7, num_agents)
        subgoal9_agents = _random_cost(4, 7, num_agents)
        subgoal10_agents = _random_cost(4, 7, num_agents)
        subgoal11_agents = _random_cost(4, 7, num_agents)
        subgoal12_agents = _random_cost(4, 7, num_agents)
        subgoal13_agents = _random_cost(1, 3, num_agents)
        subgoal14_agents = _random_cost(1, 3, num_agents)
        subgoal15_agents = _random_cost(1, 3, num_agents)
        subgoal16_agents = _random_cost(1, 3, num_agents)
        subgoal17_agents = _random_cost(1, 3, num_agents)
        subgoal18_agents = _random_cost(1, 3, num_agents)
        subgoal19_agents = _random_cost(1, 3, num_agents)
        subgoal20_agents = _random_cost(1, 3, num_agents)
        subgoal21_agents = _random_cost(1, 3, num_agents)
        subgoal22_agents = _random_cost(1, 3, num_agents)
        subgoal23_agents = _random_cost(1, 3, num_agents)
        subgoal24_agents = _random_cost(1, 3, num_agents)
        subgoal25_agents = _random_cost(1, 3, num_agents)
        subgoal26_agents = _random_cost(1, 3, num_agents)
        subgoal27_agents = _random_cost(1, 3, num_agents)
        subgoal28_agents = _random_cost(1, 3, num_agents)
        subgoal29_agents = _random_cost(1, 3, num_agents)
        subgoal30_agents = _random_cost(1, 3, num_agents)
        subgoal31_agents = _random_cost(1, 3, num_agents)
        subgoal32_agents = _random_cost(1, 3, num_agents)
        subgoal33_agents = _random_cost(1, 3, num_agents)
        subgoal34_agents = _random_cost(1, 3, num_agents)
        subgoal35_agents = _random_cost(1, 3, num_agents)
        subgoal36_agents = _random_cost(1, 3, num_agents)
        subgoal37_agents = _random_cost(1, 3, num_agents)
        subgoal38_agents = _random_cost(1, 3, num_agents)
        subgoal39_agents = _random_cost(1, 3, num_agents)
    else:
        root_agents = _equal_cost(40, 60, num_agents)
        subgoal1_agents = _equal_cost(13, 20, num_agents)
        subgoal2_agents = _equal_cost(13, 20, num_agents)
        subgoal3_agents = _equal_cost(13, 20, num_agents)
        subgoal4_agents = _equal_cost(4, 7, num_agents)
        subgoal5_agents = _equal_cost(4, 7, num_agents)
        subgoal6_agents = _equal_cost(4, 7, num_agents)
        subgoal7_agents = _equal_cost(4, 7, num_agents)
        subgoal8_agents = _equal_cost(4, 7, num_agents)
        subgoal9_agents = _equal_cost(4, 7, num_agents)
        subgoal10_agents = _equal_cost(4, 7, num_agents)
        subgoal11_agents = _equal_cost(4, 7, num_agents)
        subgoal12_agents = _equal_cost(4, 7, num_agents)
        subgoal13_agents = _equal_cost(1, 3, num_agents)
        subgoal14_agents = _equal_cost(1, 3, num_agents)
        subgoal15_agents = _equal_cost(1, 3, num_agents)
        subgoal16_agents = _equal_cost(1, 3, num_agents)
        subgoal17_agents = _equal_cost(1, 3, num_agents)
        subgoal18_agents = _equal_cost(1, 3, num_agents)
        subgoal19_agents = _equal_cost(1, 3, num_agents)
        subgoal20_agents = _equal_cost(1, 3, num_agents)
        subgoal21_agents = _equal_cost(1, 3, num_agents)
        subgoal22_agents = _equal_cost(1, 3, num_agents)
        subgoal23_agents = _equal_cost(1, 3, num_agents)
        subgoal24_agents = _equal_cost(1, 3, num_agents)
        subgoal25_agents = _equal_cost(1, 3, num_agents)
        subgoal26_agents = _equal_cost(1, 3, num_agents)
        subgoal27_agents = _equal_cost(1, 3, num_agents)
        subgoal28_agents = _equal_cost(1, 3, num_agents)
        subgoal29_agents = _equal_cost(1, 3, num_agents)
        subgoal30_agents = _equal_cost(1, 3, num_agents)
        subgoal31_agents = _equal_cost(1, 3, num_agents)
        subgoal32_agents = _equal_cost(1, 3, num_agents)
        subgoal33_agents = _equal_cost(1, 3, num_agents)
        subgoal34_agents = _equal_cost(1, 3, num_agents)
        subgoal35_agents = _equal_cost(1, 3, num_agents)
        subgoal36_agents = _equal_cost(1, 3, num_agents)
        subgoal37_agents = _equal_cost(1, 3, num_agents)
        subgoal38_agents = _equal_cost(1, 3, num_agents)
        subgoal39_agents = _equal_cost(1, 3, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)
    subgoal10 = GoalNode("Sub Goal 10", subgoal10_agents)
    subgoal11 = GoalNode("Sub Goal 11", subgoal11_agents)
    subgoal12 = GoalNode("Sub Goal 12", subgoal12_agents)
    subgoal13 = GoalNode("Sub Goal 13", subgoal13_agents)
    subgoal14 = GoalNode("Sub Goal 14", subgoal14_agents)
    subgoal15 = GoalNode("Sub Goal 15", subgoal15_agents) 
    subgoal16 = GoalNode("Sub Goal 16", subgoal16_agents)
    subgoal17 = GoalNode("Sub Goal 17", subgoal17_agents)
    subgoal18 = GoalNode("Sub Goal 18", subgoal18_agents)
    subgoal19 = GoalNode("Sub Goal 19", subgoal19_agents)
    subgoal20 = GoalNode("Sub Goal 20", subgoal20_agents)
    subgoal21 = GoalNode("Sub Goal 21", subgoal21_agents)
    subgoal22 = GoalNode("Sub Goal 22", subgoal22_agents)
    subgoal23 = GoalNode("Sub Goal 23", subgoal23_agents)
    subgoal24 = GoalNode("Sub Goal 24", subgoal24_agents)
    subgoal25 = GoalNode("Sub Goal 25", subgoal25_agents)
    subgoal26 = GoalNode("Sub Goal 26", subgoal26_agents)
    subgoal27 = GoalNode("Sub Goal 27", subgoal27_agents)
    subgoal28 = GoalNode("Sub Goal 28", subgoal28_agents)
    subgoal29 = GoalNode("Sub Goal 29", subgoal29_agents)
    subgoal30 = GoalNode("Sub Goal 30", subgoal30_agents)
    subgoal31 = GoalNode("Sub Goal 31", subgoal31_agents)
    subgoal32 = GoalNode("Sub Goal 32", subgoal32_agents)
    subgoal33 = GoalNode("Sub Goal 33", subgoal33_agents)
    subgoal34 = GoalNode("Sub Goal 34", subgoal34_agents)
    subgoal35 = GoalNode("Sub Goal 35", subgoal35_agents)
    subgoal36 = GoalNode("Sub Goal 36", subgoal36_agents)
    subgoal37 = GoalNode("Sub Goal 37", subgoal37_agents)
    subgoal38 = GoalNode("Sub Goal 38", subgoal38_agents)
    subgoal39 = GoalNode("Sub Goal 39", subgoal39_agents)
    
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

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)
    subgoal10m = GoalNode2("Sub Goal 10", 0)
    subgoal11m = GoalNode2("Sub Goal 11", 0)
    subgoal12m = GoalNode2("Sub Goal 12", 0)
    subgoal13m = GoalNode2("Sub Goal 13", 0)
    subgoal14m = GoalNode2("Sub Goal 14", 0)
    subgoal15m = GoalNode2("Sub Goal 15", 0)
    subgoal16m = GoalNode2("Sub Goal 16", 0)
    subgoal17m = GoalNode2("Sub Goal 17", 0)
    subgoal18m = GoalNode2("Sub Goal 18", 0)
    subgoal19m = GoalNode2("Sub Goal 19", 0)
    subgoal20m = GoalNode2("Sub Goal 20", 0)
    subgoal21m = GoalNode2("Sub Goal 21", 0)
    subgoal22m = GoalNode2("Sub Goal 22", 0)
    subgoal23m = GoalNode2("Sub Goal 23", 0)
    subgoal24m = GoalNode2("Sub Goal 24", 0)
    subgoal25m = GoalNode2("Sub Goal 25", 0)
    subgoal26m = GoalNode2("Sub Goal 26", 0)
    subgoal27m = GoalNode2("Sub Goal 27", 0)
    subgoal28m = GoalNode2("Sub Goal 28", 0)
    subgoal29m = GoalNode2("Sub Goal 29", 0)
    subgoal30m = GoalNode2("Sub Goal 30", 0)
    subgoal31m = GoalNode2("Sub Goal 31", 0)
    subgoal32m = GoalNode2("Sub Goal 32", 0)
    subgoal33m = GoalNode2("Sub Goal 33", 0)
    subgoal34m = GoalNode2("Sub Goal 34", 0)
    subgoal35m = GoalNode2("Sub Goal 35", 0)
    subgoal36m = GoalNode2("Sub Goal 36", 0)
    subgoal37m = GoalNode2("Sub Goal 37", 0)
    subgoal38m = GoalNode2("Sub Goal 38", 0)
    subgoal39m = GoalNode2("Sub Goal 39", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    rootm.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal1m.add_child(subgoal5m)
    subgoal1m.add_child(subgoal6m)
    subgoal2m.add_child(subgoal7m)
    subgoal2m.add_child(subgoal8m)
    subgoal2m.add_child(subgoal9m)
    subgoal3m.add_child(subgoal10m)
    subgoal3m.add_child(subgoal11m)
    subgoal3m.add_child(subgoal12m)
    subgoal4m.add_child(subgoal13m)
    subgoal4m.add_child(subgoal14m)
    subgoal4m.add_child(subgoal15m)
    subgoal5m.add_child(subgoal16m)
    subgoal5m.add_child(subgoal17m)
    subgoal5m.add_child(subgoal18m)
    subgoal6m.add_child(subgoal19m)
    subgoal6m.add_child(subgoal20m)
    subgoal6m.add_child(subgoal21m)
    subgoal7m.add_child(subgoal22m)
    subgoal7m.add_child(subgoal23m)
    subgoal7m.add_child(subgoal24m)
    subgoal8m.add_child(subgoal25m)
    subgoal8m.add_child(subgoal26m)
    subgoal8m.add_child(subgoal27m)
    subgoal9m.add_child(subgoal28m)
    subgoal9m.add_child(subgoal29m)
    subgoal9m.add_child(subgoal30m)
    subgoal10m.add_child(subgoal31m)
    subgoal10m.add_child(subgoal32m)
    subgoal10m.add_child(subgoal33m)
    subgoal11m.add_child(subgoal34m)
    subgoal11m.add_child(subgoal35m)
    subgoal11m.add_child(subgoal36m)
    subgoal12m.add_child(subgoal37m)
    subgoal12m.add_child(subgoal38m)
    subgoal12m.add_child(subgoal39m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents
    subgoal10m.agents = subgoal10_agents
    subgoal11m.agents = subgoal11_agents
    subgoal12m.agents = subgoal12_agents
    subgoal13m.agents = subgoal13_agents
    subgoal14m.agents = subgoal14_agents
    subgoal15m.agents = subgoal15_agents
    subgoal16m.agents = subgoal16_agents
    subgoal17m.agents = subgoal17_agents
    subgoal18m.agents = subgoal18_agents
    subgoal19m.agents = subgoal19_agents
    subgoal20m.agents = subgoal20_agents
    subgoal21m.agents = subgoal21_agents
    subgoal22m.agents = subgoal22_agents
    subgoal23m.agents = subgoal23_agents
    subgoal24m.agents = subgoal24_agents
    subgoal25m.agents = subgoal25_agents
    subgoal26m.agents = subgoal26_agents
    subgoal27m.agents = subgoal27_agents
    subgoal28m.agents = subgoal28_agents
    subgoal29m.agents = subgoal29_agents
    subgoal30m.agents = subgoal30_agents
    subgoal31m.agents = subgoal31_agents
    subgoal32m.agents = subgoal32_agents
    subgoal33m.agents = subgoal33_agents
    subgoal34m.agents = subgoal34_agents
    subgoal35m.agents = subgoal35_agents
    subgoal36m.agents = subgoal36_agents
    subgoal37m.agents = subgoal37_agents
    subgoal38m.agents = subgoal38_agents
    subgoal39m.agents = subgoal39_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)
    cost_node(subgoal10m)
    cost_node(subgoal11m)
    cost_node(subgoal12m)
    cost_node(subgoal13m)
    cost_node(subgoal14m)
    cost_node(subgoal15m)
    cost_node(subgoal16m)
    cost_node(subgoal17m)
    cost_node(subgoal18m)
    cost_node(subgoal19m)
    cost_node(subgoal20m)
    cost_node(subgoal21m)
    cost_node(subgoal22m)
    cost_node(subgoal23m)
    cost_node(subgoal24m)
    cost_node(subgoal25m)
    cost_node(subgoal26m)
    cost_node(subgoal27m)
    cost_node(subgoal28m)
    cost_node(subgoal29m)
    cost_node(subgoal30m)
    cost_node(subgoal31m)
    cost_node(subgoal32m)
    cost_node(subgoal33m)
    cost_node(subgoal34m)
    cost_node(subgoal35m)
    cost_node(subgoal36m)
    cost_node(subgoal37m)
    cost_node(subgoal38m)
    cost_node(subgoal39m)

    return (root,rootm)

def tree_1(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(30, 45, num_agents)
        subgoal1_agents = _random_cost(15, 25, num_agents)
        subgoal2_agents = _random_cost(15, 25, num_agents)
        subgoal3_agents = _random_cost(1, 8, num_agents)
        subgoal4_agents = _random_cost(1, 8, num_agents)
        subgoal5_agents = _random_cost(1, 8, num_agents)
        subgoal6_agents = _random_cost(1, 8, num_agents)
        subgoal7_agents = _random_cost(5, 15, num_agents)
        subgoal8_agents = _random_cost(5, 15, num_agents)
        subgoal9_agents = _random_cost(1, 6, num_agents)
        subgoal10_agents = _random_cost(1, 6, num_agents)
        subgoal11_agents = _random_cost(1, 6, num_agents)
        subgoal12_agents = _random_cost(1, 6, num_agents)
    else:
        root_agents = _equal_cost(30, 45, num_agents)
        subgoal1_agents = _equal_cost(15, 25, num_agents)
        subgoal2_agents = _equal_cost(15, 25, num_agents)
        subgoal3_agents = _equal_cost(1, 8, num_agents)
        subgoal4_agents = _equal_cost(1, 8, num_agents)
        subgoal5_agents = _equal_cost(1, 8, num_agents)
        subgoal6_agents = _equal_cost(1, 8, num_agents)
        subgoal7_agents = _equal_cost(5, 15, num_agents)
        subgoal8_agents = _equal_cost(5, 15, num_agents)
        subgoal9_agents = _equal_cost(1, 6, num_agents)
        subgoal10_agents = _equal_cost(1, 6, num_agents)
        subgoal11_agents = _equal_cost(1, 6, num_agents)
        subgoal12_agents = _equal_cost(1, 6, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)
    subgoal10 = GoalNode("Sub Goal 10", subgoal10_agents)
    subgoal11 = GoalNode("Sub Goal 11", subgoal11_agents)
    subgoal12 = GoalNode("Sub Goal 12", subgoal12_agents)

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

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)
    subgoal10m = GoalNode2("Sub Goal 10", 0)
    subgoal11m = GoalNode2("Sub Goal 11", 0)
    subgoal12m = GoalNode2("Sub Goal 12", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    subgoal1m.add_child(subgoal3m)
    subgoal1m.add_child(subgoal4m)
    subgoal1m.add_child(subgoal5m)
    subgoal1m.add_child(subgoal6m)
    subgoal2m.add_child(subgoal7m)
    subgoal2m.add_child(subgoal8m)
    subgoal7m.add_child(subgoal9m)
    subgoal7m.add_child(subgoal10m)
    subgoal4m.add_child(subgoal11m)
    subgoal4m.add_child(subgoal12m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents
    subgoal10m.agents = subgoal10_agents
    subgoal11m.agents = subgoal11_agents
    subgoal12m.agents = subgoal12_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)
    cost_node(subgoal10m)
    cost_node(subgoal11m)
    cost_node(subgoal12m)

    return (root,rootm)

def tree_2(random = False, num_agents = 3):
    if random:
        root_agents = _random_cost(30, 45, num_agents)
        subgoal1_agents = _random_cost(6, 12, num_agents)
        subgoal2_agents = _random_cost(6, 12, num_agents)
        subgoal3_agents = _random_cost(6, 12, num_agents)
        subgoal4_agents = _random_cost(6, 12, num_agents)
        subgoal5_agents = _random_cost(3, 6, num_agents)
        subgoal6_agents = _random_cost(3, 6, num_agents)
        subgoal7_agents = _random_cost(3, 6, num_agents)
        subgoal8_agents = _random_cost(3, 6, num_agents)
        subgoal9_agents = _random_cost(3, 6, num_agents)
        subgoal10_agents = _random_cost(3, 6, num_agents)
        subgoal11_agents = _random_cost(3, 6, num_agents)
        subgoal12_agents = _random_cost(3, 6, num_agents)
    else:
        root_agents = _equal_cost(30, 45, num_agents)
        subgoal1_agents = _equal_cost(6, 12, num_agents)
        subgoal2_agents = _equal_cost(6, 12, num_agents)
        subgoal3_agents = _equal_cost(6, 12, num_agents)
        subgoal4_agents = _equal_cost(6, 12, num_agents)
        subgoal5_agents = _equal_cost(3, 6, num_agents)
        subgoal6_agents = _equal_cost(3, 6, num_agents)
        subgoal7_agents = _equal_cost(3, 6, num_agents)
        subgoal8_agents = _equal_cost(3, 6, num_agents)
        subgoal9_agents = _equal_cost(3, 6, num_agents)
        subgoal10_agents = _equal_cost(3, 6, num_agents)
        subgoal11_agents = _equal_cost(3, 6, num_agents)
        subgoal12_agents = _equal_cost(3, 6, num_agents)

    # GoalNode
    root = GoalNode("Main Goal", root_agents)
    subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
    subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
    subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
    subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
    subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
    subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)
    subgoal7 = GoalNode("Sub Goal 7", subgoal7_agents)
    subgoal8 = GoalNode("Sub Goal 8", subgoal8_agents)
    subgoal9 = GoalNode("Sub Goal 9", subgoal9_agents)
    subgoal10 = GoalNode("Sub Goal 10", subgoal10_agents)
    subgoal11 = GoalNode("Sub Goal 11", subgoal11_agents)
    subgoal12 = GoalNode("Sub Goal 12", subgoal12_agents)

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

    # GoalNode2
    rootm = GoalNode2("Main Goal", 0)
    subgoal1m = GoalNode2("Sub Goal 1", 0)
    subgoal2m = GoalNode2("Sub Goal 2", 0)
    subgoal3m = GoalNode2("Sub Goal 3", 0)
    subgoal4m = GoalNode2("Sub Goal 4", 0)
    subgoal5m = GoalNode2("Sub Goal 5", 0)
    subgoal6m = GoalNode2("Sub Goal 6", 0)
    subgoal7m = GoalNode2("Sub Goal 7", 0)
    subgoal8m = GoalNode2("Sub Goal 8", 0)
    subgoal9m = GoalNode2("Sub Goal 9", 0)
    subgoal10m = GoalNode2("Sub Goal 10", 0)
    subgoal11m = GoalNode2("Sub Goal 11", 0)
    subgoal12m = GoalNode2("Sub Goal 12", 0)

    rootm.add_child(subgoal1m)
    rootm.add_child(subgoal2m)
    rootm.add_child(subgoal3m)
    rootm.add_child(subgoal4m)
    subgoal1m.add_child(subgoal5m)
    subgoal1m.add_child(subgoal6m)
    subgoal2m.add_child(subgoal7m)
    subgoal2m.add_child(subgoal8m)
    subgoal3m.add_child(subgoal9m)
    subgoal3m.add_child(subgoal10m)
    subgoal4m.add_child(subgoal11m)
    subgoal4m.add_child(subgoal12m)

    rootm.agents = root_agents
    subgoal1m.agents = subgoal1_agents
    subgoal2m.agents = subgoal2_agents
    subgoal3m.agents = subgoal3_agents
    subgoal4m.agents = subgoal4_agents
    subgoal5m.agents = subgoal5_agents
    subgoal6m.agents = subgoal6_agents
    subgoal7m.agents = subgoal7_agents
    subgoal8m.agents = subgoal8_agents
    subgoal9m.agents = subgoal9_agents
    subgoal10m.agents = subgoal10_agents
    subgoal11m.agents = subgoal11_agents
    subgoal12m.agents = subgoal12_agents

    cost_node(rootm)
    cost_node(subgoal1m)
    cost_node(subgoal2m)
    cost_node(subgoal3m)
    cost_node(subgoal4m)
    cost_node(subgoal5m)
    cost_node(subgoal6m)
    cost_node(subgoal7m)
    cost_node(subgoal8m)
    cost_node(subgoal9m)
    cost_node(subgoal10m)
    cost_node(subgoal11m)
    cost_node(subgoal12m)

    return (root, rootm)

def get_discrepancy(agents_and_goals):

    agents_costs = []

    for agent in agents_and_goals.keys():

        curr_agent_cost = 0

        for goal in agents_and_goals[agent]:
            curr_agent_cost += goal.data[agent]
        
        agents_costs.append(curr_agent_cost)

    return abs(max(agents_costs) - min(agents_costs))

#__RUNNING THE EFFICIENCY TEST FOR JONATHAN'S AND FAY'S
def efficiency_test(goal_tree, max_res: List):
    
    #level_order_transversal(goal_tree)

    AGENT = list(goal_tree.data.keys())
    
    max_resources_j = {}
    max_resources_f = max_res
    for i in range(len(AGENT)):
        max_resources_j[AGENT[i]] = max_res[i]

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
    level_order_transversal(goal_tree2)
    try:
        result = optimized_goal_allocation(goal_tree2, max_resources_f)
    except ValueError as e:
        print(f"Error encountered in inner function of optimized_goal_allocation(): {str(e)}")
        return
    
    if result:
        fresult, fresources = result
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

    
    return f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total_resources, j_total_resources, AGENT

#MAHEEN EFFICIENCY TEST
def efficiency_test_m(root: GoalNode2, max_resources) -> Tuple[int,int]:
    """
    Calculates the average cost and Total resources used of Goalnodes.

    Parameters
    ----------
    root : GoalNode2
        The root node of the goal tree.

    Returns
    -------
    float
        The average cost of the nodes with an assigned agent.
    """
    if len(max_resources) == 1:
        return (root.cost, 1)
    nodes = []
    stacks = [root]

    while stacks:
        node = stacks.pop(0)
        nodes.append(node)
        children = node.get_children()
        stacks.extend(children)
    
    agent_goal_m(nodes,max_resources)
    resources_usage = 0
    agent_used = []

    def traverse(node):
        nonlocal resources_usage
        nonlocal agent_used
        if node.assigned_agent != "":
            resources_usage += node.cost
            if node.assigned_agent not in agent_used:
                agent_used.append(node.assigned_agent)
        for child in node.get_children():
            traverse(child)

    traverse(root)

    if len(agent_used) > 0:
        return (resources_usage, len(agent_used))
    else:
        return (0, 0)
        
def bar_chart_plotting(Results: Tuple, title):
    # Define the algorithm names and total resource utilization values
    algorithm_names = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm']

    f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total_resources, j_total_resources, AGENTS = Results

    # Set the width of the bars
    bar_width = 0.4

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
    
def plotting(fay_averages, jonathan_averages, maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, iteration, scenario, num_agents_avail: List = [3] * 10):
    # Color of each algorithm
    colors = ['peachpuff', 'lightblue', 'khaki']
    algorithms = ["Fay's Algorithm", "Jonathan's Algorithm", "Maheen's Algorithm"]

    # Create figure and axes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    bar_width = 0.2

    # Determine the maximum length among fay_averages, jonathan_averages, and maheen_averages
    max_length = max(len(fay_averages), len(jonathan_averages), len(maheen_averages))

    fay_padded = np.pad(fay_averages, (0, max_length - len(fay_averages)))
    jonathan_padded = np.pad(jonathan_averages, (0, max_length - len(jonathan_averages)))
    maheen_padded = np.pad(maheen_averages, (0, max_length - len(maheen_averages)))

    # Plot the side by side bar chart for average resources on ax1
    x = np.arange(max_length)
    ax1.bar(x - bar_width, fay_padded, width=bar_width, color=colors[0], label="Fay's Algorithm")
    ax1.bar(x, jonathan_padded, width=bar_width, color=colors[1], label="Jonathan's Algorithm")
    ax1.bar(x + bar_width, maheen_padded, width=bar_width, color=colors[2], label="Maheen's Algorithm")

    
    ax1.set_ylim(0, max(max(fay_padded), max(jonathan_padded), max(maheen_padded)) + 20)    
    if num_agents_avail != [3] * 10:
        ax1.set_xlabel('Number of Available Agents')
    else:
        ax1.set_xlabel('Test cases')
    ax1.set_ylabel('Average Resources')
    ax1.set_title(scenario)
    ax1.set_xticks(x)
    ax1.set_xticklabels(x + 1)
    ax1.legend(loc='upper left')
    
            
    ax2.bar(x - bar_width, agent_fay_averages, width=bar_width, color=colors[0], label="Fay's Algorithm")
    ax2.bar(x, agent_jonathan_averages, width=bar_width, color=colors[1], label="Jonathan's Algorithm")
    ax2.bar(x + bar_width, agent_maheen_averages, width=bar_width, color=colors[2], label="Maheen's Algorithm")

    ax2.set_ylim(0, max(max(agent_fay_averages), max(agent_jonathan_averages), max(agent_maheen_averages)) + 1)

    if num_agents_avail != [3] * 10:
        ax2.set_xlabel('Number of Available Agents')
    else:
        ax2.set_xlabel('Test cases')
    ax2.set_ylabel('Average Agents Used')
    ax2.set_xticks(x)
    ax2.set_xticklabels(x + 1)

    ax2.legend(loc='upper left')

    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=1)

    plt.tight_layout()
    plt.show()

def main():
    test_cases = [(binary_symmetric,"BINARY SYMMETRIC TREE"),
        (binary_left, "BINARY LEFT TREE"),
        (binary_right, "BINARY RIGHT TREE"),
        (root,  "ROOT-ONLY TREE"),
        (tree_symmetric, "SYMMETRIC TREE"),
        (tree_left_right, "LEFT RIGHT TREE"),
        (large_binary_tree,  "LARGE BINARY TREE"),
        (large_tree, "LARGE TREE"),
        (tree_1,  "TREE 1"),
        (tree_2, "TREE 2"),]
   
    """
        SCENARIO 1: 
            - Same agent cost
            - Ten trees
            - 3 Agents

    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_1_a = "SCENARIO 1A: Same Agent Cost - 3 Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0

        for (generate_tree, title) in test_cases:
            
            tree, tree_m= generate_tree() 
            # Run each goal tree
            result = efficiency_test(tree, [40,40,40])
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, [40,40,40])
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees

        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)

        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)

    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages,agent_jonathan_averages, agent_maheen_averages, j, scenario_1_a)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_1_b = "SCENARIO 1B: Same Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0
        resources = [random.randint(35,45),random.randint(35,45),random.randint(35,45)]

        for (generate_tree, title) in test_cases:
            tree, tree_m= generate_tree() 
            
            # Run each goal tree
            result = efficiency_test(tree, resources)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, resources)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)

        
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages,agent_jonathan_averages, agent_maheen_averages, j, scenario_1_b)


    """
        SCENARIO 2: 
        - Various agent cost
        - Ten trees
        - 3 Agents
    """

    # SUB CASE: SAME MAX RESOURCES
    scenario_2_a = "SCENARIO 2A: Random Agent Cost - 3 Agents - Same Max Resources"
    print(scenario_2_a)
    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0

        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0

        no_trees = 0

        for (generate_tree, title) in test_cases:
            tree, tree_m= generate_tree(True,3) 
            # Run each goal tree
            result = efficiency_test(tree, [40,40,40])
            if not result:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, [40,40,40])
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees

        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)

    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages,agent_jonathan_averages, agent_maheen_averages, j, scenario_2_a)


            
    # SUB CASE: DIFFERENT MAX RESOURCES
    
    scenario_2_b = "SCENARIO 2B: Random Agent Cost - 3 Agents - Different Max Resources"
    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0

        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0

        no_trees = 0
        resources = [random.randint(35,45),random.randint(35,45),random.randint(35,45)]

        for (generate_tree, title) in test_cases:
            # Exclude the equal agent cost tree
            tree, tree_m= generate_tree(True,3) 
            
            # Run each goal tree
            result = efficiency_test(tree, resources)            
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, resources)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)


    plotting(fay_averages, jonathan_averages, maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_2_b)


    """
        SCENARIO 3: 
        - Vary number of agents
        - Ten trees -> hundred trees
        - Same agent cost

    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_3_a = "SCENARIO 3A: Same Agent Cost - Varying Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []
    no_agents_avail = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0

        no_agents = j + 1
        no_agents_avail.append(no_agents)
        for (generate_tree, title) in test_cases:
            tree, tree_m= generate_tree(False, no_agents) 

            # Run each goal tree
            result = efficiency_test(tree, [40] * no_agents)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, [40] * no_agents)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)
        
    plotting(fay_averages, jonathan_averages, maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_3_a, no_agents_avail)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_3_b = "SCENARIO 3B: Same Agent Cost - Varying Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []
    no_agents_avail = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0
        
        no_agents = j + 1
        no_agents_avail.append(no_agents)
        resources = []

        for i in range(no_agents):
            resources.append(random.randint(35,45))
        for (generate_tree, title) in test_cases:
            tree, tree_m= generate_tree(False, no_agents) 
            result = efficiency_test(tree, resources)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, resources)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)

        
    plotting(fay_averages, jonathan_averages, maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_3_b, no_agents_avail)


    """
        SCENARIO 4: 
        - Vary number of agents
        - Ten trees -> hundred trees
        - Vary agent cost

    """
    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_4_a = "SCENARIO 4A: Different Agent Cost - Varying Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []
    no_agents_avail = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0

        no_agents = j + 1
        no_agents_avail.append(no_agents)
        

        for (generate_tree, title) in test_cases:
            tree, tree_m= generate_tree(True, no_agents) 
            # Run each goal tree
            result = efficiency_test(tree, [40] * no_agents)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, [40] * no_agents)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)
        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)

        
    plotting(fay_averages, jonathan_averages, maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_4_a, no_agents_avail)

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_4_b = "SCENARIO 4B: Different Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []
    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []
    no_agents_avail = []

    for j in range(10):
        algo_results_fay = 0
        algo_results_jonathan = 0
        algo_results_maheen = 0
        agent_used_fay = 0
        agent_used_jonathan = 0
        agent_used_maheen = 0
        no_trees = 0
        no_agents = j + 1
        no_agents_avail.append(no_agents)
        resources = []

        for i in range(no_agents):
            resources.append(random.randint(35,45))
        for (generate_tree, title) in test_cases:

            tree, tree_m= generate_tree(True, no_agents) 
            # Provide different max resources to each agent
            result = efficiency_test(tree, resources)
            if result == None:
                continue
            (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
            #bar_chart_plotting((f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents), title)
            m_total, agents_used_m = efficiency_test_m(tree_m, resources)
            algo_results_fay += f_total
            algo_results_jonathan += j_total
            algo_results_maheen += m_total
            for a in f_agent_goals:
                if a:
                    agent_used_fay += 1
            for a in j_agent_goals:
                if a:
                    agent_used_jonathan += 1  
            agent_used_maheen += agents_used_m 
            no_trees += 1

        algo_results_fay /= no_trees
        algo_results_jonathan /= no_trees
        algo_results_maheen /= no_trees
        agent_used_fay /= no_trees
        agent_used_jonathan /= no_trees
        agent_used_maheen /= no_trees
        
        # Append the averages to the lists
        fay_averages.append(algo_results_fay)
        jonathan_averages.append(algo_results_jonathan)
        maheen_averages.append(algo_results_maheen)

        agent_fay_averages.append(agent_used_fay)
        agent_jonathan_averages.append(agent_used_jonathan)
        agent_maheen_averages.append(agent_used_maheen)
        
    plotting(fay_averages, jonathan_averages,maheen_averages, agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_4_b,no_agents_avail)
    
    """
        SCENARIO 5: 
            - Same agent cost
            - 3 Agents
            - 1000 trees
    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_5_a = "SCENARIO 5A\n 1000 Trees - Same Agent Cost - 3 Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):  # 10 trees per test case
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0
            
            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case()
                
                    # Run each goal tree
                    result = efficiency_test(tree, [40,40,40])
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, [40,40,40])
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_5_a) 

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_5_b = "SCENARIO 5B\n 1000 Trees - Same Agent Cost - 3 Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0
            resources = [random.randint(35,45),random.randint(35,45),random.randint(35,45)]

            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case()
                
                    # Run each goal tree
                    result = efficiency_test(tree, resources)
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, resources)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_5_b) 

    """
        SCENARIO 6: 
            - Random agent cost
            - 3 Agents
            - 1000 trees
    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_6_a = "SCENARIO 6A\n 1000 Trees - Random Agent Cost - 3 Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):  # 10 trees per test case
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0
            
            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(True, 3)
                
                    # Run each goal tree
                    result = efficiency_test(tree, [40,40,40])
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, [40,40,40])
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_6_a) 

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_6_b = "SCENARIO 6B\n 1000 Trees - Random Agent Cost - Varying Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    for j in range(10):
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0
            resources = [random.randint(35,45),random.randint(35,45),random.randint(35,45)]
            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(True, 3)
                
                    # Run each goal tree
                    result = efficiency_test(tree, resources)
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, resources)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_6_b) 

    """
        SCENARIO 7: 
            - Same agent cost
            - Varying Agents
            - 1000 trees
    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_7_a = "SCENARIO 7A\n 1000 Trees - Same Agent Cost - Varying Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    no_agents_avail = []

    for j in range(10):  # 10 trees per test case
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0

            no_agents = j + 1
            no_agents_avail.append(no_agents)

            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(False, no_agents)
                
                    # Run each goal tree
                    result = efficiency_test(tree, [40] * no_agents)
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, [40] * no_agents)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_7_a, no_agents_avail) 

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_7_b = "SCENARIO 7B\n 1000 Trees - Same Agent Cost - Varying Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    no_agents_avail = []
    for j in range(10):
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0
            
            no_agents = j + 1
            no_agents_avail.append(no_agents)
            resources = []

            for i in range(no_agents):
                resources.append(random.randint(35,45))

            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(False, no_agents)
                
                    # Run each goal tree
                    result = efficiency_test(tree, resources)
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, resources)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_7_b, no_agents_avail) 

    """
        SCENARIO 8: 
            - Random agent cost
            - 3 Agents
            - 1000 trees
    """

    # SUB CASE: SAME MAX RESOURCES
    # Test for 10 times each scenario
    scenario_8_a = "SCENARIO 8A\n 1000 Trees - Random Agent Cost - Varying Agents - Same Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    no_agents_avail = []

    for j in range(10):  # 10 trees per test case
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0

            no_agents = j + 1
            no_agents_avail.append(no_agents)
            
            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(True,  no_agents)
                
                    # Run each goal tree
                    result = efficiency_test(tree, [40] * no_agents )
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, [40] * no_agents)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_8_a, no_agents_avail) 

    # SUB CASE: DIFFERENT MAX RESOURCES
    # Test for 10 times each scenario
    scenario_8_b = "SCENARIO 8B\n 1000 Trees - Random Agent Cost - Varying Agents - Different Max Resources"

    # Store the average results for each algorithm
    fay_averages = []
    jonathan_averages = []
    maheen_averages = []

    agent_fay_averages = []
    agent_jonathan_averages = []
    agent_maheen_averages = []

    no_agents_avail = []

    for j in range(10):
            algo_results_fay = 0
            algo_results_jonathan = 0
            algo_results_maheen = 0
            agent_used_fay = 0
            agent_used_jonathan = 0
            agent_used_maheen = 0
            no_trees = 0

            no_agents = j + 1
            no_agents_avail.append(no_agents)

            resources = []

            for i in range(no_agents):
                resources.append(random.randint(35,45))

            for (generate_tree, title) in test_cases:
                test_case = generate_tree
                # each tree run 10 times
                for _ in range(10):  
                    tree, tree_m= test_case(True, 3)
                
                    # Run each goal tree
                    result = efficiency_test(tree, resources)
                    if result == None:
                        continue
                    (f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals, f_total, j_total, Agents) = result
                    m_total, agents_used_m = efficiency_test_m(tree_m, resources)
                    algo_results_fay += f_total
                    algo_results_jonathan += j_total
                    algo_results_maheen += m_total
                    for a in f_agent_goals:
                        if a:
                            agent_used_fay += 1
                    for a in j_agent_goals:
                        if a:
                            agent_used_jonathan += 1  
                    agent_used_maheen += agents_used_m 
                    no_trees += 1

            # Calculate averages for this tree
            algo_results_fay /= no_trees
            algo_results_jonathan /= no_trees
            algo_results_maheen /= no_trees
            agent_used_fay /= no_trees
            agent_used_jonathan /= no_trees
            agent_used_maheen /= no_trees
            
            # Append the averages to the lists
            fay_averages.append(algo_results_fay)
            jonathan_averages.append(algo_results_jonathan)
            maheen_averages.append(algo_results_maheen)
            agent_fay_averages.append(agent_used_fay)
            agent_jonathan_averages.append(agent_used_jonathan)
            agent_maheen_averages.append(agent_used_maheen)

    # Plotting for each test case
    plotting(fay_averages, jonathan_averages, maheen_averages ,agent_fay_averages, agent_jonathan_averages, agent_maheen_averages, j, scenario_8_b, no_agents_avail) 


if __name__ == "__main__":
    main()
    

