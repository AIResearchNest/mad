from typing import Dict, List

from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

from mad.optimize import jonathan_average_cost
from mad.optimize import jonathan_optimal_path
from mad.optimize import _get_goals
from mad.optimize import jonathan_distribute_goals
from mad.optimize import _score_allocation

def jonathan_algorithm(goal_tree: GoalNode, agents: List, max_resources: int) -> Dict:
    """
    Takes in a goal tree and finds optimal goals to accomplish the main goal and distributes them to agents evenly

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    agents : List
        List of string names of agents available
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    Returns : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned (values)
    """

    # Takes in a goal tree and updates each GoalNode's agent cost to a temporary value of the average cost of all agents able to accomplish that goal
    jonathan_average_cost(goal_tree)

    # Takes in a goal tree and max resources for each agent and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished
    selected_goals = jonathan_optimal_path(goal_tree, max_resources)
    print("Selected Goals:")
    for goal in selected_goals:
        print(goal.name)
    
    print()
    # Takes in a list of GoalNodes and distributes them among available agents
    distributed_goals = jonathan_distribute_goals(selected_goals, agents, max_resources)

    return distributed_goals