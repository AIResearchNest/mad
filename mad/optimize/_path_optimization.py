from mad.data_structures import GoalNode
from typing import List

def jonathan_optimal_path(node: GoalNode) -> List:
    if not node.children:
        return [node]
    
    selected_goals = []
    child_goals = []
    
    for child in node.children:
        child_goals.extend(jonathan_optimal_path(child))
    
    child_cost = sum(child.cost for child in child_goals)
    
    if child_cost < node.cost:
        selected_goals.extend(child_goals)
    else:
        selected_goals.append(node)
    
    return selected_goals