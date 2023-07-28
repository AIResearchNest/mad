from mad.data_structures import GoalNode, GoalNode2, print_goal_tree, print_tree_and_agents
from mad.optimize import dfs_goal_allocation, optimized_goal_allocation, agent_goal_m, cost_node
from typing import Dict
import random as r
import matplotlib.pyplot as plt
import copy
import numpy as np

# Print Functions for Maheen
def print_goal_tree_m(node, indent=0):
    prefix = "  " * indent
    print(f"{prefix}- {node.name}: {node.assigned_agent}")
    for child in node.children:
        print_goal_tree_m(child, indent + 1)

def print_tree_and_agents_m(node):
    q = []
    q.append(node)

    while q:
        current = q[0]
        q.pop(0)
        print(f"- {current.name}: {current.cost}")

        for agent in current.agents.keys():
            print(f"   - {agent}: {current.agents[agent]}")

        for child in current.get_children():
            q.append(child)

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

def get_discrepancy_opt(opt_agents_and_goals, root):
    agents_and_goals = {}

    for agent in root.data.keys():
        agents_and_goals[agent] = []

    for agent, value in opt_agents_and_goals.items():
        agents_and_goals[agent] = value

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

# Scoring Maheen
def get_goals_m(root):
    
    goals = []
    
    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        goals.append(current)

        for child in current.get_children():
            q.append(child)

    return goals

def get_total_cost_m(root):
    
    total_cost = 0
    
    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            total_cost += current.agents[current.assigned_agent]

        for child in current.get_children():
            q.append(child)

    return total_cost

def get_agents_used_m(root):

    agents_used = []

    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            if current.assigned_agent not in agents_used:
                agents_used.append(current.assigned_agent)

        for child in current.get_children():
            q.append(child)
    
    return len(agents_used)

def get_discrepancy_m(root):

    num_agents = len(root.agents)
    agents_used = {}

    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            if current.assigned_agent not in agents_used.keys():
                agents_used[current.assigned_agent] = current.agents[current.assigned_agent]
            else:
                agents_used[current.assigned_agent] += current.agents[current.assigned_agent]
        for child in current.get_children():
            q.append(child)
    
    if len(agents_used.keys()) < num_agents:
        return max(agents_used.values())
    return abs(max(agents_used.values()) - min(agents_used.values()))

def get_skew_m(root, best_case):
    return get_total_cost_m(root) - best_case

# Trees
def binary_symmetric(num_agents, random=False):
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

    return [root, rootm]

def binary_left(num_agents, random=False):
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

    return [root, rootm]

def binary_right(num_agents, random=False):
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

    return [root, rootm]

def root(num_agents, random=False):
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

    return [root, rootm]

def tree_symmetric(num_agents, random=False):
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

    return [root, rootm]

def tree_left_right(num_agents, random=False):
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

    return [root, rootm]

def large_binary_tree(num_agents, random=False):
    
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

    return [root, rootm]

def large_tree(num_agents, random=False):
    
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

    return [root, rootm]

def tree_1(num_agents, random=False):
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

    return [root, rootm]

def tree_2(num_agents, random=False):
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

    return [root, rootm]

# Scenario 1
def Test1(total_tests, seed):
    """
    3 agents
    Equal Cost
    Same resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    curr_seed = seed
    test_num = 0

    # Each bar on graph
    for test_group in range(total_tests):

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(3),
                    binary_left(3), 
                    binary_right(3), 
                    root(3), 
                    tree_symmetric(3), 
                    tree_left_right(3), 
                    large_binary_tree(3),
                    large_tree(3), 
                    tree_1(3), 
                    tree_2(3)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError:
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [50,50,50])
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 2
def Test2(total_tests, seed):
    """
    3 agents
    Equal Cost
    Different resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    curr_seed = seed
    test_num = 0

    # Each bar on graph
    for test_group in range(total_tests):

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(3),
                    binary_left(3), 
                    binary_right(3), 
                    root(3), 
                    tree_symmetric(3), 
                    tree_left_right(3), 
                    large_binary_tree(3),
                    large_tree(3), 
                    tree_1(3), 
                    tree_2(3)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError:
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [50,60,70])
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 3
def Test3(total_tests, seed):
    """
    3 agents
    Varying Cost
    Same resources
    """
    
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    curr_seed = seed
    test_num = 0

    # Each bar on graph
    for test_group in range(total_tests):

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(3, True),
                    binary_left(3, True), 
                    binary_right(3, True), 
                    root(3, True), 
                    tree_symmetric(3, True), 
                    tree_left_right(3, True), 
                    large_binary_tree(3, True),
                    large_tree(3, True), 
                    tree_1(3, True), 
                    tree_2(3, True)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [50,50,50])
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 4
def Test4(total_tests, seed):
    """
    3 agents
    Varying Cost
    Different resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    curr_seed = seed
    test_num = 0

    # Each bar on graph
    for test_group in range(total_tests):

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(3, True),
                    binary_left(3, True), 
                    binary_right(3, True), 
                    root(3, True), 
                    tree_symmetric(3, True), 
                    tree_left_right(3, True), 
                    large_binary_tree(3, True),
                    large_tree(3, True), 
                    tree_1(3, True), 
                    tree_2(3, True)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [50,60,70])
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 5
def Test5(total_tests, seed):
    """
    Varying agents
    Equal Cost
    Same resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    test_num = 0
    num_agents = 0

    # Each bar on graph
    for test_group in range(total_tests):
        curr_seed = seed

        num_agents += 1

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(num_agents),
                    binary_left(num_agents), 
                    binary_right(num_agents), 
                    root(num_agents), 
                    tree_symmetric(num_agents), 
                    tree_left_right(num_agents), 
                    large_binary_tree(num_agents),
                    large_tree(num_agents), 
                    tree_1(num_agents), 
                    tree_2(num_agents)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
                # dfs algo
                try:
                    dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 100, "remus": 100, "franklin": 100, "john": 100, "alice": 100, "jake": 100, "anna": 100, "tommy": 100, "trent": 100, "karen": 100})
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
                    fresult, fresources = optimized_goal_allocation(opt_root, [100] * num_agents)
                    curr_opt_avg_cost += get_total_cost(fresult)
                    curr_opt_agents_used += get_agents_used(fresult)
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [100] * num_agents)
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 6
def Test6(total_tests, seed):
    """
    Varying agents
    Equal Cost
    Different resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    test_num = 0
    num_agents = 0

    # Each bar on graph
    for test_group in range(total_tests):
        curr_seed = seed

        num_agents += 1

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Set opt and m resources
        res = [100, 80, 90, 70, 80, 90, 70, 80, 90, 70]
        opt_and_m_resources = []
        for i in range(num_agents):
            opt_and_m_resources.append(res[i])

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(num_agents),
                    binary_left(num_agents), 
                    binary_right(num_agents), 
                    root(num_agents), 
                    tree_symmetric(num_agents), 
                    tree_left_right(num_agents), 
                    large_binary_tree(num_agents),
                    large_tree(num_agents), 
                    tree_1(num_agents), 
                    tree_2(num_agents)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    fresult, fresources = optimized_goal_allocation(opt_root, opt_and_m_resources)
                    curr_opt_avg_cost += get_total_cost(fresult)
                    curr_opt_agents_used += get_agents_used(fresult)
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), opt_and_m_resources)
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 7
def Test7(total_tests, seed):
    """
    Varying agents
    Varying Cost
    Same resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    test_num = 0
    num_agents = 0

    # Each bar on graph
    for test_group in range(total_tests):
        curr_seed = seed

        num_agents += 1

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(num_agents, True),
                    binary_left(num_agents, True), 
                    binary_right(num_agents, True), 
                    root(num_agents, True), 
                    tree_symmetric(num_agents, True), 
                    tree_left_right(num_agents, True), 
                    large_binary_tree(num_agents, True),
                    large_tree(num_agents, True), 
                    tree_1(num_agents, True), 
                    tree_2(num_agents, True)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
                # dfs algo
                try:
                    dfs_agents_and_goals = dfs_goal_allocation(dfs_root, {"grace": 100, "remus": 100, "franklin": 100, "john": 100, "alice": 100, "jake": 100, "anna": 100, "tommy": 100, "trent": 100, "karen": 100})
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
                    fresult, fresources = optimized_goal_allocation(opt_root, [100] * num_agents)
                    curr_opt_avg_cost += get_total_cost(fresult)
                    curr_opt_agents_used += get_agents_used(fresult)
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), [100] * num_agents)
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Scenario 8
def Test8(total_tests, seed):
    """
    Varying agents
    Varying Cost
    Different resources
    """
    final_dfs_avg_costs = []
    final_dfs_avg_agents = []
    final_dfs_avg_discrepancy = []
    final_dfs_avg_skew = []
    final_dfs_fails = []

    final_opt_avg_costs = []
    final_opt_avg_agents = []
    final_opt_avg_discrepancy = []
    final_opt_avg_skew = []
    final_opt_fails = []

    final_m_avg_costs = []
    final_m_avg_agents = []
    final_m_avg_discrepancy = []
    final_m_avg_skew = []
    final_m_fails = []

    test_num = 0
    num_agents = 0

    # Each bar on graph
    for test_group in range(total_tests):
        curr_seed = seed

        num_agents += 1

        dfs_avg_costs = 0
        dfs_avg_agents = 0
        dfs_avg_discrepancy = 0
        dfs_avg_skew = 0
        dfs_fails = []

        opt_avg_costs = 0
        opt_avg_agents = 0
        opt_avg_discrepancy = 0
        opt_avg_skew = 0
        opt_fails = []

        m_avg_costs = 0
        m_avg_agents = 0
        m_avg_discrepancy = 0
        m_avg_skew = 0
        m_fails = []

        # Set opt and m resources
        res = [100, 80, 90, 70, 80, 90, 70, 80, 90, 70]
        opt_and_m_resources = []
        for i in range(num_agents):
            opt_and_m_resources.append(res[i])

        # Run all tree groups
        for group in range(100):
            r.seed(curr_seed)
            TREES = [binary_symmetric(num_agents, True),
                    binary_left(num_agents, True), 
                    binary_right(num_agents, True), 
                    root(num_agents, True), 
                    tree_symmetric(num_agents, True), 
                    tree_left_right(num_agents, True), 
                    large_binary_tree(num_agents, True),
                    large_tree(num_agents, True), 
                    tree_1(num_agents, True), 
                    tree_2(num_agents, True)]
            
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

            # Maheen Test
            curr_m_avg_cost = 0
            curr_m_agents_used = 0
            curr_m_failures = []
            curr_m_discrepancy = 0
            curr_m_skew = 0
            num_m_trees_passed = 0

            # Run each individual test
            for tree_idx in range(len(TREES)):
                test_num += 1
                
                dfs_root = TREES[tree_idx][0]
                opt_root = copy.deepcopy(dfs_root)
                m_root = TREES[tree_idx][1]
                
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
                    fresult, fresources = optimized_goal_allocation(opt_root, opt_and_m_resources)
                    curr_opt_avg_cost += get_total_cost(fresult)
                    curr_opt_agents_used += get_agents_used(fresult)
                    curr_opt_discrepancy += get_discrepancy_opt(fresult, opt_root)
                    curr_opt_skew += get_skew_opt(fresult, best_case)
                    num_opt_trees_passed += 1
                except ValueError: 
                    curr_opt_failures.append(test_num)

                # m algo
                try:
                    agent_goal_m(get_goals_m(m_root), opt_and_m_resources)
                    curr_m_avg_cost += get_total_cost_m(m_root)
                    curr_m_agents_used += get_agents_used_m(m_root)
                    curr_m_discrepancy += get_discrepancy_m(m_root)
                    curr_m_skew += get_skew_m(m_root, best_case)
                    num_m_trees_passed += 1
                except TypeError:
                    curr_m_failures.append(test_num)

            # Add Jonathan Results
            if num_dfs_trees_passed != 0:
                dfs_avg_costs += curr_dfs_avg_cost / num_dfs_trees_passed
                dfs_avg_agents += curr_dfs_agents_used / num_dfs_trees_passed
                dfs_avg_discrepancy += curr_dfs_discrepancy / num_dfs_trees_passed
                dfs_avg_skew += curr_dfs_skew / num_dfs_trees_passed
                dfs_fails.extend(curr_dfs_failures)
            else:
                dfs_fails.extend(curr_dfs_failures)

            # Add Fay Results
            if num_opt_trees_passed != 0:
                opt_avg_costs += curr_opt_avg_cost / num_opt_trees_passed
                opt_avg_agents += curr_opt_agents_used / num_opt_trees_passed
                opt_avg_discrepancy += curr_opt_discrepancy / num_opt_trees_passed
                opt_avg_skew += curr_opt_skew / num_opt_trees_passed
                opt_fails.extend(curr_opt_failures)
            else:
                opt_fails.extend(curr_opt_failures)

            # Add Maheen Results
            if num_opt_trees_passed != 0:
                m_avg_costs += curr_m_avg_cost / num_m_trees_passed
                m_avg_agents += curr_m_agents_used / num_m_trees_passed
                m_avg_discrepancy += curr_m_discrepancy / num_m_trees_passed
                m_avg_skew += curr_m_skew / num_m_trees_passed
                m_fails.extend(curr_m_failures)
            else:
                m_fails.extend(curr_m_failures)

            curr_seed += 1

        final_dfs_avg_costs.append(dfs_avg_costs / 100)
        final_dfs_avg_agents.append(dfs_avg_agents / 100)
        final_dfs_avg_discrepancy.append(dfs_avg_discrepancy / 100)
        final_dfs_avg_skew.append(dfs_avg_skew / 100)
        final_dfs_fails.append(dfs_fails)

        final_opt_avg_costs.append(opt_avg_costs / 100)
        final_opt_avg_agents.append(opt_avg_agents / 100)
        final_opt_avg_discrepancy.append(opt_avg_discrepancy / 100)
        final_opt_avg_skew.append(opt_avg_skew / 100)
        final_opt_fails.append(opt_fails)

        final_m_avg_costs.append(m_avg_costs / 100)
        final_m_avg_agents.append(m_avg_agents / 100)
        final_m_avg_discrepancy.append(m_avg_discrepancy / 100)
        final_m_avg_skew.append(m_avg_skew / 100)
        final_m_fails.append(m_fails)

    print(f"Test Number: {test_num}")
    return final_dfs_avg_costs, final_dfs_avg_agents, final_dfs_avg_discrepancy, final_dfs_avg_skew, final_dfs_fails, final_opt_avg_costs, final_opt_avg_agents, final_opt_avg_discrepancy, final_opt_avg_skew, final_opt_fails, final_m_avg_costs, final_m_avg_agents, final_m_avg_discrepancy, final_m_avg_skew, final_m_fails

# Plot Results
def plot_results(scenario, title, avg_costs1, avg_agents1, avg_discrepancy1, avg_skew1, fails1, avg_costs2, avg_agents2, avg_discrepancy2, avg_skew2, fails2, avg_costs3, avg_agents3, avg_discrepancy3, avg_skew3, fails3):

    print(f"\nScenario {scenario}")
    print("\nDFS Goal Allocation Results")
    for i in range(len(avg_costs1)):
        print(f"Test {i}: TC: {avg_costs1[i]}, F: {fails1[i]}, A: {avg_agents1[i]}, D: {avg_discrepancy1[i]}, S: {avg_skew1[i]}")
    print("\nOptimize Results")
    for i in range(len(avg_costs2)):
        print(f"Test {i}: TC: {avg_costs2[i]}, F: {fails2[i]}, A: {avg_agents2[i]}, D: {avg_discrepancy2[i]}, S: {avg_skew2[i]}")
    print("\nMaheen Results")
    for i in range(len(avg_costs3)):
        print(f"Test {i}: TC: {avg_costs3[i]}, F: {fails3[i]}, A: {avg_agents3[i]}, D: {avg_discrepancy3[i]}, S: {avg_skew3[i]}")

    # Set the width of the bars
    bar_width = 0.25

    # Create the figure and axes
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    x = np.arange(len(avg_costs1))

    # Plot 1
    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, avg_costs1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, avg_costs2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects3 = ax1.bar(x + bar_width * 2, avg_costs3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(avg_costs1), max(avg_costs2), max(avg_costs3)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Test Groups of 1000 Trees')
    ax1.set_ylabel('Resources Used')
    ax1.set_title('Average Resources Used')
    ax1.set_xticks(x + bar_width)
    ax1.set_xticklabels(x + 1)
    ax1.legend()


    # Plot 2
    # Plot the bars for Jonathan's Algorithm
    rects4 = ax2.bar(x, avg_agents1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects5 = ax2.bar(x + bar_width, avg_agents2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects6 = ax2.bar(x + bar_width * 2, avg_agents3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax2.set_ylim(0, max(max(avg_agents1), max(avg_agents2), max(avg_agents3)) + 5)

    # Set the labels and title
    ax2.set_xlabel('Test Groups of 1000 Trees')
    ax2.set_ylabel('Agents Used')
    ax2.set_title('Average Number of Agents Used')
    ax2.set_xticks(x + bar_width)
    ax2.set_xticklabels(x + 1)
    # ax2.legend()


    # Plot 3
    # Plot the bars for Jonathan's Algorithm
    rects7 = ax3.bar(x, avg_discrepancy1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects8 = ax3.bar(x + bar_width, avg_discrepancy2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects9 = ax3.bar(x + bar_width * 2, avg_discrepancy3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax3.set_ylim(0, max(max(avg_discrepancy1), max(avg_discrepancy2), max(avg_discrepancy3)) + 5)
    
    # Set the labels and title
    ax3.set_xlabel('Test Groups of 1000 Trees')
    ax3.set_ylabel('Difference in Agent\'s Cost')
    ax3.set_title('Average Cost Distribution Disparity of Agents')
    ax3.set_xticks(x + bar_width)
    ax3.set_xticklabels(x + 1)
    # ax3.legend()


    # Plot 4
    # Plot the bars for Jonathan's Algorithm
    rects10 = ax4.bar(x, avg_skew1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects11 = ax4.bar(x + bar_width, avg_skew2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects12 = ax4.bar(x + bar_width * 2, avg_skew3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax4.set_ylim(min(0, min(avg_skew3)), max(max(avg_skew1), max(avg_skew2), max(avg_skew3)) + 5)
    
    # Set the labels and title
    ax4.set_xlabel('Test Groups of 1000 Trees')
    ax4.set_ylabel('Difference from Cheapest Allocation')
    ax4.set_title('Average Cost Efficiency of Goal Allocation')
    ax4.set_xticks(x + bar_width)
    ax4.set_xticklabels(x + 1)
    # ax4.legend()
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(title, fontsize=16)

    # Display the chart
    plt.show()

def plot_results_vary_agents(scenario, title, avg_costs1, avg_agents1, avg_discrepancy1, avg_skew1, fails1, avg_costs2, avg_agents2, avg_discrepancy2, avg_skew2, fails2, avg_costs3, avg_agents3, avg_discrepancy3, avg_skew3, fails3):

    print(f"\nScenario {scenario}")
    print("\nDFS Goal Allocation Results")
    for i in range(len(avg_costs1)):
        print(f"Test {i}: TC: {avg_costs1[i]}, F: {fails1[i]}, A: {avg_agents1[i]}, D: {avg_discrepancy1[i]}, S: {avg_skew1[i]}")
    print("\nOptimize Results")
    for i in range(len(avg_costs2)):
        print(f"Test {i}: TC: {avg_costs2[i]}, F: {fails2[i]}, A: {avg_agents2[i]}, D: {avg_discrepancy2[i]}, S: {avg_skew2[i]}")
    print("\nMaheen Results")
    for i in range(len(avg_costs3)):
        print(f"Test {i}: TC: {avg_costs3[i]}, F: {fails3[i]}, A: {avg_agents3[i]}, D: {avg_discrepancy3[i]}, S: {avg_skew3[i]}")

    # Set the width of the bars
    bar_width = 0.25

    # Create the figure and axes
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    x = np.arange(len(avg_costs1))

    # Plot 1
    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, avg_costs1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, avg_costs2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects3 = ax1.bar(x + bar_width * 2, avg_costs3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(avg_costs1), max(avg_costs2), max(avg_costs3)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Number of Agents Available')
    ax1.set_ylabel('Resources Used')
    ax1.set_title('Average Resources Used')
    ax1.set_xticks(x + bar_width)
    ax1.set_xticklabels(x + 1)
    ax1.legend()


    # Plot 2
    # Plot the bars for Jonathan's Algorithm
    rects4 = ax2.bar(x, avg_agents1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax2.bar(x + bar_width, avg_agents2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects6 = ax2.bar(x + bar_width * 2, avg_agents3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax2.set_ylim(0, max(max(avg_agents1), max(avg_agents2), max(avg_agents3)) + 5)

    # Set the labels and title
    ax2.set_xlabel('Number of Agents Available')
    ax2.set_ylabel('Agents Used')
    ax2.set_title('Average Number of Agents Used')
    ax2.set_xticks(x + bar_width)
    ax2.set_xticklabels(x + 1)
    # ax2.legend()


    # Plot 3
    # Plot the bars for Jonathan's Algorithm
    rects7 = ax3.bar(x, avg_discrepancy1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects8 = ax3.bar(x + bar_width, avg_discrepancy2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects9 = ax3.bar(x + bar_width * 2, avg_discrepancy3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax3.set_ylim(0, max(max(avg_discrepancy1), max(avg_discrepancy2), max(avg_discrepancy3)) + 5)
    
    # Set the labels and title
    ax3.set_xlabel('Number of Agents Available')
    ax3.set_ylabel('Difference in Agent\'s Cost')
    ax3.set_title('Average Cost Distribution Disparity of Agents')
    ax3.set_xticks(x + bar_width)
    ax3.set_xticklabels(x + 1)
    # ax3.legend()


    # Plot 4
    # Plot the bars for Jonathan's Algorithm
    rects10 = ax4.bar(x, avg_skew1, width=bar_width, label="DFS Goal Allocation Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects11 = ax4.bar(x + bar_width, avg_skew2, width=bar_width, label="Optimize Algorithm", color='peachpuff')

    # Plot the bars for Maheen's Algorithm
    rects12 = ax4.bar(x + bar_width * 2, avg_skew3, width=bar_width, label="Maheen's Algorithm", color='lightgreen')

    #Increase the length of the y-axis
    ax4.set_ylim(min(0, min(avg_skew3)), max(max(avg_skew1), max(avg_skew2), max(avg_skew3)) + 5)
    
    # Set the labels and title
    ax4.set_xlabel('Number of Agents Available')
    ax4.set_ylabel('Difference from Cheapest Allocation')
    ax4.set_title('Average Cost Efficiency of Goal Allocation')
    ax4.set_xticks(x + bar_width)
    ax4.set_xticklabels(x + 1)
    # ax4.legend()
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(title, fontsize=16)

    # Display the chart
    plt.show()


# Main
def main():
    dfs_costs1, dfs_agents1, dfs_discrepancy1, dfs_skew1, dfs_fails1, opt_costs1, opt_agents1, opt_discrepancy1, opt_skew1, opt_fails1, m_avg_costs1, m_avg_agents1, m_avg_discrepancy1, m_avg_skew1, m_fails1 = Test1(10, 0)
    plot_results(1, "Scenario 1: 3 Agents, Equal Costs, Same Resources, 1000 Trees", dfs_costs1, dfs_agents1, dfs_discrepancy1, dfs_skew1, dfs_fails1, opt_costs1, opt_agents1, opt_discrepancy1, opt_skew1, opt_fails1, m_avg_costs1, m_avg_agents1, m_avg_discrepancy1, m_avg_skew1, m_fails1)

    dfs_costs2, dfs_agents2, dfs_discrepancy2, dfs_skew2, dfs_fails2, opt_costs2, opt_agents2, opt_discrepancy2, opt_skew2, opt_fails2, m_avg_costs2, m_avg_agents2, m_avg_discrepancy2, m_avg_skew2, m_fails2 = Test2(10, 1000)
    plot_results(2, "Scenario 2: 3 Agents, Equal Costs, Different Resources, 1000 Trees", dfs_costs2, dfs_agents2, dfs_discrepancy2, dfs_skew2, dfs_fails2, opt_costs2, opt_agents2, opt_discrepancy2, opt_skew2, opt_fails2, m_avg_costs2, m_avg_agents2, m_avg_discrepancy2, m_avg_skew2, m_fails2)

    dfs_costs3, dfs_agents3, dfs_discrepancy3, dfs_skew3, dfs_fails3, opt_costs3, opt_agents3, opt_discrepancy3, opt_skew3, opt_fails3, m_avg_costs3, m_avg_agents3, m_avg_discrepancy3, m_avg_skew3, m_fails3 = Test3(10, 2000)
    plot_results(3, "Scenario 3: 3 Agents, Varying Costs, Same Resources, 1000 Trees", dfs_costs3, dfs_agents3, dfs_discrepancy3, dfs_skew3, dfs_fails3, opt_costs3, opt_agents3, opt_discrepancy3, opt_skew3, opt_fails3, m_avg_costs3, m_avg_agents3, m_avg_discrepancy3, m_avg_skew3, m_fails3)

    dfs_costs4, dfs_agents4, dfs_discrepancy4, dfs_skew4, dfs_fails4, opt_costs4, opt_agents4, opt_discrepancy4, opt_skew4, opt_fails4, m_avg_costs4, m_avg_agents4, m_avg_discrepancy4, m_avg_skew4, m_fails4 = Test4(10, 3000)
    plot_results(4, "Scenario 4: 3 Agents, Varying Costs, Different Resources, 1000 Trees", dfs_costs4, dfs_agents4, dfs_discrepancy4, dfs_skew4, dfs_fails4, opt_costs4, opt_agents4, opt_discrepancy4, opt_skew4, opt_fails4, m_avg_costs4, m_avg_agents4, m_avg_discrepancy4, m_avg_skew4, m_fails4)

    dfs_costs5, dfs_agents5, dfs_discrepancy5, dfs_skew5, dfs_fails5, opt_costs5, opt_agents5, opt_discrepancy5, opt_skew5, opt_fails5, m_avg_costs5, m_avg_agents5, m_avg_discrepancy5, m_avg_skew5, m_fails5 = Test5(10, 4000)
    plot_results_vary_agents(5, "Scenario 5: Varying Agents, Equal Costs, Same Resources, 1000 Trees", dfs_costs5, dfs_agents5, dfs_discrepancy5, dfs_skew5, dfs_fails5, opt_costs5, opt_agents5, opt_discrepancy5, opt_skew5, opt_fails5, m_avg_costs5, m_avg_agents5, m_avg_discrepancy5, m_avg_skew5, m_fails5)

    dfs_costs6, dfs_agents6, dfs_discrepancy6, dfs_skew6, dfs_fails6, opt_costs6, opt_agents6, opt_discrepancy6, opt_skew6, opt_fails6, m_avg_costs6, m_avg_agents6, m_avg_discrepancy6, m_avg_skew6, m_fails6 = Test6(10, 5000)
    plot_results_vary_agents(6, "Scenario 6: Varying Agents, Equal Costs, Different Resources, 1000 Trees", dfs_costs6, dfs_agents6, dfs_discrepancy6, dfs_skew6, dfs_fails6, opt_costs6, opt_agents6, opt_discrepancy6, opt_skew6, opt_fails6, m_avg_costs6, m_avg_agents6, m_avg_discrepancy6, m_avg_skew6, m_fails6)

    dfs_costs7, dfs_agents7, dfs_discrepancy7, dfs_skew7, dfs_fails7, opt_costs7, opt_agents7, opt_discrepancy7, opt_skew7, opt_fails7, m_avg_costs7, m_avg_agents7, m_avg_discrepancy7, m_avg_skew7, m_fails7 = Test7(10, 6000)
    plot_results_vary_agents(7, "Scenario 7: Varying Agents, Varying Costs, Same Resources, 1000 Trees", dfs_costs7, dfs_agents7, dfs_discrepancy7, dfs_skew7, dfs_fails7, opt_costs7, opt_agents7, opt_discrepancy7, opt_skew7, opt_fails7, m_avg_costs7, m_avg_agents7, m_avg_discrepancy7, m_avg_skew7, m_fails7)

    dfs_costs8, dfs_agents8, dfs_discrepancy8, dfs_skew8, dfs_fails8, opt_costs8, opt_agents8, opt_discrepancy8, opt_skew8, opt_fails8, m_avg_costs8, m_avg_agents8, m_avg_discrepancy8, m_avg_skew8, m_fails8 = Test8(10, 7000)
    plot_results_vary_agents(8, "Scenario 8: Varying Agents, Varying Costs, Different Resources, 1000 Trees", dfs_costs8, dfs_agents8, dfs_discrepancy8, dfs_skew8, dfs_fails8, opt_costs8, opt_agents8, opt_discrepancy8, opt_skew8, opt_fails8, m_avg_costs8, m_avg_agents8, m_avg_discrepancy8, m_avg_skew8, m_fails8)

if __name__ == '__main__':
    main()
