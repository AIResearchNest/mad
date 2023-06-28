from mad.data_structures import GoalNode
from typing import Dict

# private function should be as follows
def _helper_func():
    pass

def initial_goal_allocation(goal_tree: GoalNode,
                            max_resources: int) -> Dict:
    
    """
    Optimizes allocation of goals to multiple agents

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

    # write your code here

    # Raise an error if goal_tree is empty

    pass



"""
Jonathan's Algorithm
########################################################
"""
from typing import Dict, List
from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree
from mad.optimize import jonathan_average_cost
from mad.optimize import jonathan_optimal_path
from mad.optimize import jonathan_distribute_goals

def jonathan_algorithm(goal_tree: GoalNode, max_resources: int, verbose: int = 0) -> Dict:
    """
    Takes in a goal tree and finds optimal goals to accomplish the main goal and distributes them to agents evenly

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    Returns : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned (values)
    """
    if verbose > 0:
        print("Goal Tree:")
        print_goal_tree(goal_tree)
        print()
    
    # Takes in a goal tree and updates each GoalNode's agent cost to a temporary value of the average cost of all agents able to accomplish that goal
    if verbose > 0:
        print("Agent Costs:")

    jonathan_average_cost(goal_tree, verbose)
    
    if verbose > 0:
        print()

    # Takes in a goal tree and max resources for each agent and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished
    selected_goals = jonathan_optimal_path(goal_tree, max_resources)

    if verbose > 1:
        print("Selected Goals:")
        for goal in selected_goals:
            print(goal.name)
        print()

    # Takes in a list of GoalNodes and distributes them among available agents
    distributed_goals = jonathan_distribute_goals(selected_goals, max_resources, verbose)

    if verbose > 0:
        print()
        print("Goal Allocation:")
        for key, value in distributed_goals.items():
            for goal in value:
                print(f"{key}: {goal.name}, {goal.cost}")

    return distributed_goals

"""
########################################################
"""