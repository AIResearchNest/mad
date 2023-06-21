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

def jonathan_allocation(node):
    if not node.children:
        return [node]
    
    selected_goals = []
    child_goals = []
    
    for child in node.children:
        child_goals.extend(jonathan_allocation(child))
    
    child_cost = sum(child.cost for child in child_goals)
    
    if child_cost < node.cost:
        selected_goals.extend(child_goals)
    else:
        selected_goals.append(node)
    
    return selected_goals
