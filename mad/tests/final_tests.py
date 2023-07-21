from mad.data_structures import GoalNode, print_goal_tree, print_tree_and_agents
from mad.optimize import dfs_goal_allocation, optimized_goal_allocation
from typing import Dict
import random as r
import matplotlib.pyplot as plt
import copy
import numpy as np

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
            total_cost += goal.data[agent]

    return total_cost

def get_agents_used(agents_and_goals):

    agents_used = 0

    for agent in agents_and_goals.keys():

        if len(agents_and_goals[agent]) != 0:
            agents_used += 1

    return agents_used

def get_discrepancy(agents_and_goals):

    agents_costs = []

    for agent in agents_and_goals.keys():

        curr_agent_cost = 0

        for goal in agents_and_goals[agent]:
            curr_agent_cost += goal.data[agent]
        
        agents_costs.append(curr_agent_cost)

    return abs(max(agents_costs) - min(agents_costs))

def get_skew_dfs(dfs_agents_and_goals):
    best_case = 0
    total_cost = 0

    for agent in dfs_agents_and_goals.keys():

        curr_agent_cost = 0

        for goal in dfs_agents_and_goals[agent]:
            best_case += min(goal.data.values())
            curr_agent_cost += goal.cost

        total_cost += curr_agent_cost

    return [abs(best_case - total_cost), best_case]

def get_skew_opt(opt_agents_and_goals, best_case):
    
    total_cost = 0

    for agent in opt_agents_and_goals.keys():

        curr_agent_cost = 0

        for goal in opt_agents_and_goals[agent]:
            curr_agent_cost += goal.data[agent]

        total_cost += curr_agent_cost
    
    return abs(best_case - total_cost)


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

    root = GoalNode("Main Goal", _equal_cost(50, 60, num_agents))
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

    root = GoalNode("Main Goal", _random_cost(50, 60, num_agents))
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
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

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
        
        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)
            
            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 50, "remus": 50, "franklin": 50})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [50,50,50])
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        curr_seed += 1

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 2
def Test2(total_tests, seed):
    """
    3 agents
    Equal Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

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
        
        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)
            
            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 50, "remus": 60, "franklin": 70})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [50,60,70])
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        curr_seed += 1

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 3
def Test3(total_tests, seed):
    """
    3 agents
    Varying Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

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
        
        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)
            
            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 50, "remus": 50, "franklin": 50})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [50,50,50])
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        curr_seed += 1

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 4
def Test4(total_tests, seed):
    """
    3 agents
    Varying Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

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
        
        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)
            
            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 50, "remus": 60, "franklin": 70})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [50,60,70])
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        curr_seed += 1

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 5
def Test5(total_agents, seed):
    """
    Varying agents
    Equal Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_agents):
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

        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)

            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 70, "remus": 70, "franklin": 70, "john": 70, "alice": 70, "jake": 70, "anna": 70, "tommy": 70, "trent": 70, "karen": 70})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [70] * num_agents)
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

            # curr_seed += 1

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        # curr_seed = seed

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 6
def Test6(total_agents, seed):
    """
    Varying agents
    Equal Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_agents):
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

        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        # Set opt resources
        res = [70, 80, 90, 70, 80, 90, 70, 80, 90, 70]
        opt_resources = []
        for i in range(num_agents):
            opt_resources.append(res[i])

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)

            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": res[0], "remus": res[1], "franklin": res[2], "john": res[3], "alice": res[4], "jake": res[5], "anna": res[6], "tommy": res[7], "trent": res[8], "karen": res[9]})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, opt_resources)
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

            # curr_seed += 1

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        # curr_seed = seed

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 7
def Test7(total_agents, seed):
    """
    Varying agents
    Varying Cost
    Same resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_agents):
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

        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)

            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 70, "remus": 70, "franklin": 70, "john": 70, "alice": 70, "jake": 70, "anna": 70, "tommy": 70, "trent": 70, "karen": 70})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, [70] * num_agents)
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

            # curr_seed += 1

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        # curr_seed = seed

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails

# Scenario 8
def Test8(total_agents, seed):
    """
    Varying agents
    Varying Cost
    Different resources
    """
    curr_seed = seed
    
    dfs_avg_costs = []
    dfs_avg_agents = []
    dfs_avg_discrepancy = []
    dfs_avg_skew = []
    dfs_fails = []

    opt_avg_costs = []
    opt_avg_agents = []
    opt_avg_discrepancy = []
    opt_avg_skew = []
    opt_fails = []

    test_num = 0
    num_agents = 0
    for test in range(total_agents):
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

        # Jonathan Test
        curr_dfs_avg_cost = 0
        curr_dfs_agents_used = 0
        curr_dfs_failures = []
        curr_dfs_discrepancy = 0
        curr_dfs_skew = 0
        num_dfs_trees_passed = 0

        # Fay Test
        curr_opt_avg_cost = 0
        curr_opt_agents_used = 0
        curr_opt_failures = []
        curr_opt_discrepancy = 0
        curr_opt_skew = 0
        num_opt_trees_passed = 0

        # Set opt resources
        res = [70, 80, 90, 70, 80, 90, 70, 80, 90, 70]
        opt_resources = []
        for i in range(num_agents):
            opt_resources.append(res[i])

        for tree_idx in range(len(TREES)):
            test_num += 1
            
            dfs_root = TREES[tree_idx]
            opt_root = copy.deepcopy(dfs_root)

            # dfs algo
            try:
                dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": res[0], "remus": res[1], "franklin": res[2], "john": res[3], "alice": res[4], "jake": res[5], "anna": res[6], "tommy": res[7], "trent": res[8], "karen": res[9]})
                curr_dfs_avg_cost += get_total_cost(dfs_agents_and_goals)
                curr_dfs_agents_used += get_agents_used(dfs_agents_and_goals)
                curr_dfs_discrepancy += get_discrepancy(dfs_agents_and_goals)
                skew, best_case = get_skew_dfs(dfs_agents_and_goals)
                curr_dfs_skew += skew
                num_dfs_trees_passed += 1
            except ValueError:
                curr_dfs_failures.append(test_num)

            # opt algo
            q = []
            q.append((opt_root, None)) 

            while len(q) != 0:
                level_size = len(q)

                while len(q) > 0:  
                    node, parent = q.pop(0)
                    node.initial_agent_assign()
                    children = node.get_children()
                    for child in children:
                        q.append((child, node))

            try:
                fresult, fresources = optimized_goal_allocation(opt_root, opt_resources)
                curr_opt_avg_cost += get_total_cost(fresult)
                curr_opt_agents_used += get_agents_used(fresult)
                curr_opt_discrepancy += get_discrepancy(fresult)
                curr_opt_skew += get_skew_opt(fresult, best_case)
                num_opt_trees_passed += 1
            except ValueError:
                curr_opt_failures.append(test_num)

            # curr_seed += 1

        # Add Jonathan Results
        if num_dfs_trees_passed != 0:
            dfs_avg_costs.append(curr_dfs_avg_cost / num_dfs_trees_passed)
            dfs_avg_agents.append(curr_dfs_agents_used / num_dfs_trees_passed)
            dfs_avg_discrepancy.append(curr_dfs_discrepancy / num_dfs_trees_passed)
            dfs_avg_skew.append(curr_dfs_skew / num_dfs_trees_passed)
            dfs_fails.append(curr_dfs_failures)
        else:
            dfs_avg_costs.append(0)
            dfs_avg_agents.append(0)
            dfs_avg_discrepancy.append(0)
            dfs_avg_skew.append(0)
            dfs_fails.append(curr_dfs_failures)

        # Add Fay Results
        if num_opt_trees_passed != 0:
            opt_avg_costs.append(curr_opt_avg_cost / num_opt_trees_passed)
            opt_avg_agents.append(curr_opt_agents_used / num_opt_trees_passed)
            opt_avg_discrepancy.append(curr_opt_discrepancy / num_opt_trees_passed)
            opt_avg_skew.append(curr_opt_skew / num_opt_trees_passed)
            opt_fails.append(curr_opt_failures)
        else:
            opt_avg_costs.append(0)
            opt_avg_agents.append(0)
            opt_avg_discrepancy.append(0)
            opt_avg_skew.append(0)
            opt_fails.append(curr_opt_failures)

        # curr_seed = seed

    return dfs_avg_costs, dfs_avg_agents, dfs_avg_discrepancy, dfs_avg_skew, dfs_fails, opt_avg_costs, opt_avg_agents, opt_avg_discrepancy, opt_avg_skew, opt_fails


# Plot Results
def plot_results(scenario, title, avg_costs1, avg_agents1, avg_discrepancy1, avg_skew1, fails1, avg_costs2, avg_agents2, avg_discrepancy2, avg_skew2, fails2):

    print(f"\nScenario {scenario}")
    print("\nJonathan Results")
    for i in range(len(avg_costs1)):
        print(f"Test {i}: TC: {avg_costs1[i]}, F: {fails1[i]}, A: {avg_agents1[i]}, D: {avg_discrepancy1[i]}, S: {avg_skew1[i]}")
    print("\nFay Results")
    for i in range(len(avg_costs2)):
        print(f"Test {i}: TC: {avg_costs2[i]}, F: {fails2[i]}, A: {avg_agents2[i]}, D: {avg_discrepancy2[i]}, S: {avg_skew2[i]}")

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axes
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    x = np.arange(len(avg_costs1))

    # Plot 1
    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, avg_costs1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, avg_costs2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(avg_costs1), max(avg_costs2)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Test Group')
    ax1.set_ylabel('Average Total Cost')
    ax1.set_title(f'Scenario {scenario} - Total Costs')
    ax1.set_xticks(x + bar_width / 2)
    ax1.set_xticklabels(x + 1)
    ax1.legend()


    # Plot 2
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax2.bar(x, avg_agents1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax2.bar(x + bar_width, avg_agents2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax2.set_ylim(0, max(max(avg_agents1), max(avg_agents2)) + 5)

    # Set the labels and title
    ax2.set_xlabel('Test Group')
    ax2.set_ylabel('Average Number of Agents')
    ax2.set_title(f'Scenario {scenario} - Agents Used')
    ax2.set_xticks(x + bar_width / 2)
    ax2.set_xticklabels(x + 1)
    ax2.legend()


    # Plot 3
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax3.bar(x, avg_discrepancy1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax3.bar(x + bar_width, avg_discrepancy2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax3.set_ylim(0, max(max(avg_discrepancy1), max(avg_discrepancy2)) + 5)
    
    # Set the labels and title
    ax3.set_xlabel('Test Group')
    ax3.set_ylabel('Discrepancy')
    ax3.set_title(f'Scenario {scenario} - Discrepancy')
    ax3.set_xticks(x + bar_width / 2)
    ax3.set_xticklabels(x + 1)
    ax3.legend()


    # Plot 4
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax4.bar(x, avg_skew1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax4.bar(x + bar_width, avg_skew2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax4.set_ylim(0, max(max(avg_skew1), max(avg_skew2)) + 5)
    
    # Set the labels and title
    ax4.set_xlabel('Test Group')
    ax4.set_ylabel('Skew')
    ax4.set_title(f'Scenario {scenario} - Skew')
    ax4.set_xticks(x + bar_width / 2)
    ax4.set_xticklabels(x + 1)
    ax4.legend()
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(title, fontsize=16)

    # Display the chart
    plt.show()

def plot_results_vary_agents(scenario, title, avg_costs1, avg_agents1, avg_discrepancy1, avg_skew1, fails1, avg_costs2, avg_agents2, avg_discrepancy2, avg_skew2, fails2):

    print(f"\nScenario {scenario}")
    print("\nJonathan Results")
    for i in range(len(avg_costs1)):
        print(f"Test {i}: TC: {avg_costs1[i]}, F: {fails1[i]}, A: {avg_agents1[i]}, D: {avg_discrepancy1[i]}, S: {avg_skew1[i]}")
    print("\nFay Results")
    for i in range(len(avg_costs2)):
        print(f"Test {i}: TC: {avg_costs2[i]}, F: {fails2[i]}, A: {avg_agents2[i]}, D: {avg_discrepancy2[i]}, S: {avg_skew2[i]}")

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axes
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    x = np.arange(len(avg_costs1))

    # Plot 1
    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, avg_costs1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, avg_costs2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(avg_costs1), max(avg_costs2)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Number of Agents')
    ax1.set_ylabel('Average Total Cost')
    ax1.set_title(f'Scenario {scenario} - Total Costs')
    ax1.set_xticks(x + bar_width / 2)
    ax1.set_xticklabels(x + 1)
    ax1.legend()


    # Plot 2
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax2.bar(x, avg_agents1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax2.bar(x + bar_width, avg_agents2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax2.set_ylim(0, max(max(avg_agents1), max(avg_agents2)) + 5)

    # Set the labels and title
    ax2.set_xlabel('Number of Agents')
    ax2.set_ylabel('Average Number of Agents')
    ax2.set_title(f'Scenario {scenario} - Agents Used')
    ax2.set_xticks(x + bar_width / 2)
    ax2.set_xticklabels(x + 1)
    ax2.legend()


    # Plot 3
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax3.bar(x, avg_discrepancy1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax3.bar(x + bar_width, avg_discrepancy2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax3.set_ylim(0, max(max(avg_discrepancy1), max(avg_discrepancy2)) + 5)
    
    # Set the labels and title
    ax3.set_xlabel('Number of Agents')
    ax3.set_ylabel('Discrepancy')
    ax3.set_title(f'Scenario {scenario} - Discrepancy')
    ax3.set_xticks(x + bar_width / 2)
    ax3.set_xticklabels(x + 1)
    ax3.legend()


    # Plot 4
    # Plot the bars for Jonathan's Algorithm
    rects3 = ax4.bar(x, avg_skew1, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax4.bar(x + bar_width, avg_skew2, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax4.set_ylim(0, max(max(avg_skew1), max(avg_skew2)) + 5)
    
    # Set the labels and title
    ax4.set_xlabel('Number of Agents')
    ax4.set_ylabel('Skew')
    ax4.set_title(f'Scenario {scenario} - Skew')
    ax4.set_xticks(x + bar_width / 2)
    ax4.set_xticklabels(x + 1)
    ax4.legend()
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(title, fontsize=16)

    # Display the chart
    plt.show()


def main():

    dfs_costs1, dfs_agents1, dfs_discrepancy1, dfs_skew1, dfs_fails1, opt_costs1, opt_agents1, opt_discrepancy1, opt_skew1, opt_fails1 = Test1(10, 0)
    plot_results(1, "3 Agents, Equal Costs, Same Resources, 10 Trees", dfs_costs1, dfs_agents1, dfs_discrepancy1, dfs_skew1, dfs_fails1, opt_costs1, opt_agents1, opt_discrepancy1, opt_skew1, opt_fails1)

    dfs_costs2, dfs_agents2, dfs_discrepancy2, dfs_skew2, dfs_fails2, opt_costs2, opt_agents2, opt_discrepancy2, opt_skew2, opt_fails2 = Test2(10, 100)
    plot_results(2, "3 Agents, Equal Costs, Different Resources, 10 Trees", dfs_costs2, dfs_agents2, dfs_discrepancy2, dfs_skew2, dfs_fails2, opt_costs2, opt_agents2, opt_discrepancy2, opt_skew2, opt_fails2)

    dfs_costs3, dfs_agents3, dfs_discrepancy3, dfs_skew3, dfs_fails3, opt_costs3, opt_agents3, opt_discrepancy3, opt_skew3, opt_fails3 = Test3(10, 200)
    plot_results(3, "3 Agents, Varying Costs, Same Resources, 10 Trees", dfs_costs3, dfs_agents3, dfs_discrepancy3, dfs_skew3, dfs_fails3, opt_costs3, opt_agents3, opt_discrepancy3, opt_skew3, opt_fails3)

    dfs_costs4, dfs_agents4, dfs_discrepancy4, dfs_skew4, dfs_fails4, opt_costs4, opt_agents4, opt_discrepancy4, opt_skew4, opt_fails4 = Test4(10, 300)
    plot_results(4, "3 Agents, Varying Costs, Different Resources, 10 Trees", dfs_costs4, dfs_agents4, dfs_discrepancy4, dfs_skew4, dfs_fails4, opt_costs4, opt_agents4, opt_discrepancy4, opt_skew4, opt_fails4)

    dfs_costs5, dfs_agents5, dfs_discrepancy5, dfs_skew5, dfs_fails5, opt_costs5, opt_agents5, opt_discrepancy5, opt_skew5, opt_fails5 = Test5(10, 400)
    plot_results_vary_agents(5, "Varying Agents, Equal Costs, Same Resources, 10 Trees", dfs_costs5, dfs_agents5, dfs_discrepancy5, dfs_skew5, dfs_fails5, opt_costs5, opt_agents5, opt_discrepancy5, opt_skew5, opt_fails5)

    dfs_costs6, dfs_agents6, dfs_discrepancy6, dfs_skew6, dfs_fails6, opt_costs6, opt_agents6, opt_discrepancy6, opt_skew6, opt_fails6 = Test6(10, 500)
    plot_results_vary_agents(6, "Varying Agents, Equal Costs, Different Resources, 10 Trees", dfs_costs6, dfs_agents6, dfs_discrepancy6, dfs_skew6, dfs_fails6, opt_costs6, opt_agents6, opt_discrepancy6, opt_skew6, opt_fails6)

    dfs_costs7, dfs_agents7, dfs_discrepancy7, dfs_skew7, dfs_fails7, opt_costs7, opt_agents7, opt_discrepancy7, opt_skew7, opt_fails7 = Test7(10, 600)
    plot_results_vary_agents(7, "Varying Agents, Varying Costs, Same Resources, 10 Trees", dfs_costs7, dfs_agents7, dfs_discrepancy7, dfs_skew7, dfs_fails7, opt_costs7, opt_agents7, opt_discrepancy7, opt_skew7, opt_fails7)

    dfs_costs8, dfs_agents8, dfs_discrepancy8, dfs_skew8, dfs_fails8, opt_costs8, opt_agents8, opt_discrepancy8, opt_skew8, opt_fails8 = Test8(10, 700)
    plot_results_vary_agents(8, "Varying Agents, Varying Costs, Different Resources, 10 Trees", dfs_costs8, dfs_agents8, dfs_discrepancy8, dfs_skew8, dfs_fails8, opt_costs8, opt_agents8, opt_discrepancy8, opt_skew8, opt_fails8)




    # ---------Tests----------
    # tree = r.randint(0,20)
    # num_agents = 3

    # TREES = [equal_binary_symmetric(num_agents),
    #              equal_binary_left(num_agents), 
    #              equal_binary_right(num_agents), 
    #              equal_root(num_agents), 
    #              equal_tree_symmetric(num_agents), 
    #              equal_tree_left_right(num_agents), 
    #              equal_large_binary_tree(num_agents), 
    #              equal_tree_1(num_agents), 
    #              equal_tree_2(num_agents),
    #              equal_large_tree(num_agents),
    #              random_binary_symmetric(num_agents),
    #              random_binary_left(num_agents), 
    #              random_binary_right(num_agents), 
    #              random_root(num_agents), 
    #              random_tree_symmetric(num_agents), 
    #              random_tree_left_right(num_agents), 
    #              random_large_binary_tree(num_agents), 
    #              random_tree_1(num_agents), 
    #              random_tree_2(num_agents),
    #              random_large_tree(num_agents)]

    # dfs_root = TREES[tree]
    # opt_root = copy.deepcopy(dfs_root)

    # # dfs algo
    # print("\n----Jonathan's Algorithm----")
    # agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 30, "remus": 30, "franklin": 30, "john": 30, "alice": 30, "jake": 30, "anna": 30, "tommy": 30, "trent": 30, "karen": 30})

    # print("\nJonathan Output")
    # for agent in agents_and_goals.keys():
    #     print(f"- {agent}")
    #     for goal in agents_and_goals[agent]:
    #         print(f'  - {goal.name}, {goal.cost}')

    # print(f"\nTotal Cost: {get_total_cost(agents_and_goals)}")
    # print(f"Agents Used: {get_agents_used(agents_and_goals)}")
    # print(f"Discrepancy: {get_discrepancy(agents_and_goals)}")
    # dfs_skew, best_case = get_skew_dfs(agents_and_goals)
    # print(f"Skew: {dfs_skew}")

    # print()

    # # opt algo
    # print("\n----Fay's Algorithm----")
    # q = []
    # q.append((opt_root, None)) 

    # while len(q) != 0:
    #     level_size = len(q)

    #     while len(q) > 0:  
    #         node, parent = q.pop(0)
    #         node.initial_agent_assign()
    #         children = node.get_children()
    #         for child in children:
    #             q.append((child, node))

    
    # fresult, fresources = optimized_goal_allocation(opt_root, [30] * num_agents)

    # print("\nFay Output")
    # for agent in fresult.keys():
    #     print(f"- {agent}")
    #     for goal in fresult[agent]:
    #         print(f'  - {goal.name}, {goal.data[agent]}')
    # print("\nResources")
    # for agent in fresources.keys():
    #     print(f"- {agent}: {fresources[agent]}")

    # print(f"\nTotal Cost: {get_total_cost(fresult)}")
    # print(f"Agents Used: {get_agents_used(fresult)}")
    # print(f"Discrepancy: {get_discrepancy(fresult)}")
    # print(f"Skew: {get_skew_opt(fresult, best_case)}")

    # print("\n\n----Current Tree-----")
    # print(f"\nBest Case: {best_case}\n")
    # print_tree_and_agents(opt_root)

if __name__ == '__main__':
    main()
