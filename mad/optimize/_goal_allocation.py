from mad.data_structures import GoalNode
from typing import Dict, List
from queue import Queue
import random

def _all_goals(goal_tree: GoalNode) -> List:

    """
    Takes the root GoalNode and creates an in-order list of all the GoalNodes

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Heirarichal Multi Agent Goal Tree
    
    Returns
    -------
    goal_nodes : List
        List of all of the GoalNodes in order
    """
    goal_nodes = []
    Q = Queue()
    Q.put(goal_tree)
    while (not Q.empty()):
        node = Q.get()
        if node == None:
            continue
        goal_nodes.append(node)
        for child in node.children:
            Q.put(child)
    return goal_nodes

def initial_goal_allocation(goal_tree: GoalNode,
                            max_resources: int) -> Dict:
    
    """
    Optimizes allocation of goals to multiple agents (Greedy Algorithm)

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Heirarichal Multi Agent Goal Tree 
    max_resources : int
        Maximum resources available for each agent

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    """

    # Raise an error if goal_tree is empty
    if goal_tree is None:
        raise ValueError("Goal tree is empty") # ???

    # Get a list of all of the goals
    goals = _all_goals(goal_tree)

    # Assign goals to best fit agent
    agent_and_goals = {}
    for goal in goals:
        # Find best agent to complete the goal
        best_agent = min(goal.data, key=lambda k: goal.data[k])

        # Updates GoalNode
        goal.assigned_agent = best_agent

        # Check if agent is already in
        if best_agent not in agent_and_goals.keys():
            agent_and_goals[best_agent] = [goal]
        else:
            # Add agent to dictionary and add goal to list
            agent_and_goals[best_agent].append(goal)
    return agent_and_goals

def random_goal_allocation(goal_tree):

    # Raise an error if goal_tree is empty
    if goal_tree is None:
        raise ValueError("Goal tree is empty") # ???
    
    # Get a list of all of the goals
    goals = _all_goals(goal_tree)

    agent_and_goals = {}
    for goal in goals:
        # Find best agent to complete the goal
        random_agent = random.choice(list(goal.data.keys()))

        # Updates GoalNode
        goal.assigned_agent = random_agent

        # Check if agent is already in
        if random_agent not in agent_and_goals.keys():
            agent_and_goals[random_agent] = [goal]
        else:
            # Add agent to dictionary and add goal to list
            agent_and_goals[random_agent].append(goal)
    return agent_and_goals

def print_assigned_goals(agent_and_goals: Dict) -> None:
    """
    Takes in a Dict(key: agent name, value: list of GoalNodes) and prints out in readable format

    Parameters
    ----------
    agents_and_goals: Dict
        Goal allocations (key: agent name, value: list of GoalNodes)
    """
    for agent in agent_and_goals.keys():
        list_of_goals = []
        for goal in agent_and_goals[agent]:
            list_of_goals.append(goal.name)
        print(f"{agent}: {list_of_goals}")
