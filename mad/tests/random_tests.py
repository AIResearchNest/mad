import random as r
import copy
import matplotlib.pyplot as plt
import numpy as np

from typing import Dict
from mad.data_structures import GoalNode, print_goal_tree
from mad.optimize import dfs_goal_allocation
from mad.optimize import optimized_goal_allocation

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
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy"]

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
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy"]

    d = {}
    cost = r.randint(m,n)
    for i in range(agents):
        d[AGENTS[i]] = cost

    return d

def _random_agents(agents, m , n):
    chosen_agents = {}
    assigned_one = False

    for agent in agents:
        x = r.randint(0,1)
        if x == 1:
            chosen_agents[agent] = r.randrange(m, n)
            assigned_one = True

    if not assigned_one:
        agent = agents[r.randrange(0, len(agents))]
        chosen_agents[agent] = r.randrange(m, n)


    return chosen_agents

# Results Scraper
def get_results(agents_and_goals):

    num_goals = 0
    total_cost = 0
    num_agents_used = 0
    agents_costs = []
    best_case = 0
    worst_case = 0
    avg_case = 0

    for agent in agents_and_goals.keys():
        
        if len(agents_and_goals[agent]) != 0:
            num_agents_used += 1

        curr_agent_cost = 0

        for goal in agents_and_goals[agent]:
            best_case += min(goal.data.values())
            worst_case += max(goal.data.values())
            avg_case += sum(goal.data.values()) / len(goal.data.values())
            curr_agent_cost += goal.cost
            num_goals += 1
        
        agents_costs.append(curr_agent_cost)
        total_cost += curr_agent_cost

    discrepancy = abs(max(agents_costs) - min(agents_costs))
    skew = abs(best_case - total_cost)

    return [num_goals, total_cost, skew, discrepancy, num_agents_used, best_case, avg_case, worst_case]

# Test Trees
def random_binary_symetric(num_agents):

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

def equal_binary_symetric(num_agents):

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

def random_binary_left():

    root = GoalNode("Main Goal", _random_cost(25, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def random_binary_right():

    root = GoalNode("Main Goal", _random_cost(25, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    return root

def random_root():

    root = root = GoalNode("Main Goal", _random_cost(25, 30))

    return root

def random_tree_symetric():

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(5, 10))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(5, 10))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(5, 10))

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

def random_tree_left_right():

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))

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

def random_binary_select_agents():

    AGENTS = ['grace', 'remus', 'franklin']

    root = GoalNode("Main Goal", _random_agents(AGENTS, 25, 40))
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, 15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, 15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, 5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, 5, 15))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, 5, 15))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, 5, 15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def random_tree_select_agents():

    AGENTS = ['grace', 'remus', 'franklin']

    root = GoalNode("Main Goal", _random_agents(AGENTS, 45, 80))
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, 15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, 15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, 15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, 5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, 5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, 5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_agents(AGENTS, 5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_agents(AGENTS, 5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_agents(AGENTS, 5, 10))
    subgoal10 = GoalNode("Sub Goal 10", _random_agents(AGENTS, 5, 10))
    subgoal11 = GoalNode("Sub Goal 11", _random_agents(AGENTS, 5, 10))
    subgoal12 = GoalNode("Sub Goal 12", _random_agents(AGENTS, 5, 10))

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

def random_large_binary_tree_select_agents():
    
    AGENTS = ['grace', 'remus', 'franklin']

    x = 40
    y = 60
    root = GoalNode("Main Goal", _random_agents(AGENTS, x, y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, x, y))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, x, y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, x, y))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, x, y))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, x, y))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, x, y))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_agents(AGENTS, x, y))
    subgoal8 = GoalNode("Sub Goal 8", _random_agents(AGENTS, x, y))
    subgoal9 = GoalNode("Sub Goal 9", _random_agents(AGENTS, x, y))
    subgoal10 = GoalNode("Sub Goal 10", _random_agents(AGENTS, x, y))
    subgoal11 = GoalNode("Sub Goal 11", _random_agents(AGENTS, x, y))
    subgoal12 = GoalNode("Sub Goal 12", _random_agents(AGENTS, x, y))
    subgoal13 = GoalNode("Sub Goal 13", _random_agents(AGENTS, x, y))
    subgoal14 = GoalNode("Sub Goal 14", _random_agents(AGENTS, x, y))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_agents(AGENTS, x, y)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_agents(AGENTS, x, y))
    subgoal17 = GoalNode("Sub Goal 17", _random_agents(AGENTS, x, y))
    subgoal18 = GoalNode("Sub Goal 18", _random_agents(AGENTS, x, y))
    subgoal19 = GoalNode("Sub Goal 19", _random_agents(AGENTS, x, y))
    subgoal20 = GoalNode("Sub Goal 20", _random_agents(AGENTS, x, y))
    subgoal21 = GoalNode("Sub Goal 21", _random_agents(AGENTS, x, y))
    subgoal22 = GoalNode("Sub Goal 22", _random_agents(AGENTS, x, y))
    subgoal23 = GoalNode("Sub Goal 23", _random_agents(AGENTS, x, y))
    subgoal24 = GoalNode("Sub Goal 24", _random_agents(AGENTS, x, y))
    subgoal25 = GoalNode("Sub Goal 25", _random_agents(AGENTS, x, y))
    subgoal26 = GoalNode("Sub Goal 26", _random_agents(AGENTS, x, y))
    subgoal27 = GoalNode("Sub Goal 27", _random_agents(AGENTS, x, y))
    subgoal28 = GoalNode("Sub Goal 28", _random_agents(AGENTS, x, y))
    subgoal29 = GoalNode("Sub Goal 29", _random_agents(AGENTS, x, y))
    subgoal30 = GoalNode("Sub Goal 30", _random_agents(AGENTS, x, y))
    
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

# Tests
def original_test():
    # Jonathan Results
    test = []
    tree_score = []
    tree_skew = []
    tree_discrepancy = []
    tree_agents = []

    for i in range(3,8):
        
        # ----- Jonathan Test -----
        r.seed(1)
        print()
        print("---------------------")
        print(f"Test {i}:")
        print("---------------------")
        
        # Choose a tree
        # root = random_binary_symetric(i)
        # root = random_binary_left()
        # root = random_binary_right()
        # root = random_root()
        # root = random_tree_symetric()
        # root = random_tree_left_right()
        root = random_large_binary_tree(i)
        # root = random_binary_select_agents()
        # root = random_tree_select_agents()
        # root = random_large_binary_tree_select_agents()
        
        # Run algorithm
        agents_and_goals = dfs_goal_allocation(root, 50, 1)

        # Get results
        total_cost, skew, discrepancy, num_agents_used = get_results(agents_and_goals)

        # Add data
        test.append(i)
        tree_score.append(total_cost)
        tree_skew.append(skew)
        tree_discrepancy.append(discrepancy)
        tree_agents.append(num_agents_used)
    
    # Create a figure and 3D axes
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Create the scatter plot
    # ax.scatter3D(tree_agents, tree_score, tree_descrepancy)
    ax.scatter3D(tree_agents, tree_skew, tree_discrepancy)

    # Add labels to the points
    for i in range(len(test)):
        ax.text(tree_agents[i], tree_skew[i], tree_discrepancy[i], f'{test[i]}', fontsize=8)

    # Set labels and title
    ax.set_xlabel('Number of Agents')
    ax.set_ylabel('Skew from Best Case')
    ax.set_zlabel('Descrepancy')
    ax.set_title('Algorithm Tests')

    # Show the plot
    plt.show()

def num_agents_test():

    # Jonathan Results
    all_agents_tests = []
    all_agents_skews = []
    all_agents_discrepancy = []

    for i in range(1,9):
        tree_test = []
        tree_skew = []
        tree_discrepancy = []
        for num_agents in range(1, 9):
        
            # ----- Jonathan Test -----
            r.seed(i)
            print()
            print("---------------------")
            print(f"Test {i}:")
            print("---------------------")
            
            # Choose a tree
            # root = equal_binary_symetric(num_agents)
            root = equal_large_binary_tree(num_agents)
            
            # Run algorithm
            agents_and_goals = dfs_goal_allocation(root, 50, 1)

            # Get results
            num_goals, total_cost, skew, discrepancy, num_agents_used, best_case, avg_case, worst_case = get_results(agents_and_goals)

            # Add data
            tree_test.append(num_agents)
            tree_skew.append(skew)
            tree_discrepancy.append(discrepancy)
    
        all_agents_tests.append(tree_test)
        all_agents_skews.append(tree_skew)
        all_agents_discrepancy.append(tree_discrepancy)

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(12, 4))

    for j in range(len(all_agents_tests)):
        row = j // 4  # Calculate the row index
        col = j % 4  # Calculate the column index

        ax = axes[row, col]  # Use the specified subplot

        ax.plot(all_agents_tests[j], all_agents_skews[j], marker='o', label='Skew')
        ax.plot(all_agents_tests[j], all_agents_discrepancy[j], marker='o', label='Discrepancy')

        ax.set_xlabel(f'Number of Agents')
        ax.set_ylabel('Value')
        ax.set_title(f'Tree {j+1}')
        ax.legend()

        ax.set_xticks(all_agents_tests[j])
        ax.set_xticklabels(all_agents_tests[j])

    plt.tight_layout()  # Adjust subplot spacing for better layout
    plt.show()

def diff_agent_cost_test():

    # Jonathan Results
    all_agents_tests = []
    all_agents_skews = []
    all_agents_discrepancy = []
    all_agents_total_cost = []

    for tree in range(1,9):
        tree_test = []
        tree_skew = []
        tree_discrepancy = []
        tree_total_cost = []
        for test in range(1, 9):
        
            # ----- Jonathan Test -----
            r.seed(int(f'{tree}{test}'))
            print()
            print("---------------------")
            print(f"Test {tree}:")
            print("---------------------")
            
            # Choose a tree
            root = random_binary_symetric(3)
            # root = random_large_binary_tree(3)
            
            # Run algorithm
            agents_and_goals = dfs_goal_allocation(root, 50, 1)

            # Get results
            num_goals, total_cost, skew, discrepancy, num_agents_used = get_results(agents_and_goals)

            # Add data
            tree_test.append(test)
            tree_skew.append(skew)
            tree_discrepancy.append(discrepancy)
            tree_total_cost.append(total_cost)
    
        all_agents_tests.append(tree_test)
        all_agents_skews.append(tree_skew)
        all_agents_discrepancy.append(tree_discrepancy)
        all_agents_total_cost.append(tree_total_cost)

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(12, 4))

    for j in range(len(all_agents_tests)):
        row = j // 4  # Calculate the row index
        col = j % 4  # Calculate the column index

        ax = axes[row, col]  # Use the specified subplot

        ax.plot(all_agents_tests[j], all_agents_skews[j], marker='o', label='Skew')
        ax.plot(all_agents_tests[j], all_agents_discrepancy[j], marker='o', label='Discrepancy')
        ax.plot(all_agents_tests[j], all_agents_total_cost[j], marker='o', label='Total Cost')

        ax.set_xlabel('Tests')
        ax.set_ylabel('Value')
        ax.set_title(f'Tree {j+1}')
        ax.legend()

        ax.set_xticks(all_agents_tests[j])
        ax.set_xticklabels(all_agents_tests[j])

    plt.tight_layout()  # Adjust subplot spacing for better layout
    plt.show()

# Pair
def worst_avg_best_test():
    # Jonathan Results
    all_agents_tests = []
    all_agents_best = []
    all_agents_avg = []
    all_agents_worst = []
    all_agents_total_cost = []

    for tree in range(1,9):
        tree_test = []
        tree_best = []
        tree_avg = []
        tree_worst = []
        tree_total_cost = []
        for test in range(1, 9):
        
            # ----- Jonathan Test -----
            r.seed(int(f'{tree}{test}'))
            print()
            print("---------------------")
            print(f"Test {tree}:")
            print("---------------------")
            
            # Choose a tree
            root = random_binary_symetric(test)
            # root = random_large_binary_tree(3)
            
            # Run algorithm
            agents_and_goals = dfs_goal_allocation(root, 50, 1)

            # Get results
            num_goals, total_cost, skew, discrepancy, num_agents_used, best_case, avg_case, worst_case = get_results(agents_and_goals)

            # Add data
            tree_test.append(test)
            tree_best.append(best_case)
            tree_avg.append(avg_case)
            tree_worst.append(worst_case)
            tree_total_cost.append(total_cost)
    
        all_agents_tests.append(tree_test)
        all_agents_best.append(tree_best)
        all_agents_avg.append(tree_avg)
        all_agents_worst.append(tree_worst)
        all_agents_total_cost.append(tree_total_cost)

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(18, 6))

    for j in range(len(all_agents_tests)):
        row = j // 4  # Calculate the row index
        col = j % 4  # Calculate the column index

        ax = axes[row, col]  # Use the specified subplot

        ax.plot(all_agents_tests[j], all_agents_worst[j], marker='o', label='Worst')
        ax.plot(all_agents_tests[j], all_agents_avg[j], marker='o', label='Average')
        ax.plot(all_agents_tests[j], all_agents_total_cost[j], marker='o', label='Total Cost')
        ax.plot(all_agents_tests[j], all_agents_best[j], marker='o', label='Best')

        ax.set_xlabel('Num Agents')
        ax.set_ylabel('Value')
        ax.set_title(f'Test Group {j+1}')
        ax.legend()

        ax.set_xticks(all_agents_tests[j])
        ax.set_xticklabels(all_agents_tests[j])

    plt.tight_layout()  # Adjust subplot spacing for better layout
    plt.show()

def worst_avg_best_test_skew_discrepancy():
    # Jonathan Results
    all_agents_tests = []
    all_agents_best = []
    all_agents_total_cost = []
    all_agents_skew = []
    all_agents_discrepancy = []

    for tree in range(1,9):
        tree_test = []
        tree_best = []
        tree_total_cost = []
        tree_skew = []
        tree_discrepancy = []
        for test in range(1, 9):
        
            # ----- Jonathan Test -----
            r.seed(int(f'{tree}{test}'))
            print()
            print("---------------------")
            print(f"Test {tree}:")
            print("---------------------")
            
            # Choose a tree
            root = random_binary_symetric(test)
            # root = random_large_binary_tree(3)
            
            # Run algorithm
            agents_and_goals = dfs_goal_allocation(root, 50, 1)

            # Get results
            num_goals, total_cost, skew, discrepancy, num_agents_used, best_case, avg_case, worst_case = get_results(agents_and_goals)

            # Add data
            tree_test.append(test)
            tree_best.append(best_case)
            tree_skew.append(skew)
            tree_discrepancy.append(discrepancy)
            tree_total_cost.append(total_cost)
    
        all_agents_tests.append(tree_test)
        all_agents_best.append(tree_best)
        all_agents_skew.append(tree_skew)
        all_agents_discrepancy.append(tree_discrepancy)
        all_agents_total_cost.append(tree_total_cost)

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(18, 6))

    for j in range(len(all_agents_tests)):
        row = j // 4  # Calculate the row index
        col = j % 4  # Calculate the column index

        ax = axes[row, col]  # Use the specified subplot

        ax.plot(all_agents_tests[j], all_agents_total_cost[j], marker='o', label='Total Cost')
        ax.plot(all_agents_tests[j], all_agents_best[j], marker='o', label='Best')
        ax.plot(all_agents_tests[j], all_agents_discrepancy[j], marker='o', label='Discrepancy')
        ax.plot(all_agents_tests[j], all_agents_skew[j], marker='o', label='Skew')

        ax.set_xlabel('Num Agents')
        ax.set_ylabel('Value')
        ax.set_title(f'Test Group {j+1}')
        ax.legend()

        ax.set_xticks(all_agents_tests[j])
        ax.set_xticklabels(all_agents_tests[j])

    plt.tight_layout()  # Adjust subplot spacing for better layout
    plt.show()

def main():
    # num_agents_test()
    # diff_agent_cost_test()
    
    # Test multiple agents
    worst_avg_best_test()
    worst_avg_best_test_skew_discrepancy()

    # root = random_binary_select_agents()
    # agents_and_goals = dfs_goal_allocation(root, 50, 1)

if __name__ == '__main__':
    main()

