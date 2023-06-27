from mad.data_structures import GoalNode
from typing import List

def jonathan_optimal_path(goal_tree: GoalNode, max_resources: int) -> List:
    """
    Takes in a goal tree and max resources for each agent and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    selected_goals : List
        List of GoalNodes to be accomplished by agents in the world
    """
    
    # Break Case: if GoalNode has no children, return [goal_tree]
    if not goal_tree.children:
        return [goal_tree]
    
    # Goals that will be returned upwards for each recursion call
    selected_goals = []

    # Current GoalNodes children GoalNodes
    child_goals = []
    for child in goal_tree.children:
        child_goals.extend(jonathan_optimal_path(child, max_resources))
    
    # Finds total cost of all children GoalNodes for comparison
    child_cost = sum(child.cost for child in child_goals)
    
    # Checks that a goal cost is less than the max possible resources an agent can have (Root Goal most likely) and that the current GoalNode is cheaper than it's children
    if goal_tree.cost <= max_resources and goal_tree.cost < child_cost:
        selected_goals.append(goal_tree)
    # Otherwise add the children nodes
    else:
        selected_goals.extend(child_goals)
    
    return selected_goals