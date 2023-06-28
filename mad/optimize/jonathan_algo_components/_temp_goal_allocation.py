from mad.data_structures import GoalNode
from typing import Dict, List

# private function should be as follows
def _get_goals(goal_tree: GoalNode) -> List:
    """
    Takes in a goal tree and traverses it using BFS and appends each GoalNode to an output list

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    """
    output = []
    q = []
    q.append(goal_tree)
    while q:
        current = q[0]
        q.pop(0)
        output.append(current)
        for child in current.get_children():
            q.append(child)

    return output

def jonathan_average_cost(goal_tree: GoalNode, verbose: int = 0) -> None:
    """
    Takes in a goal tree and updates each GoalNode's agent cost to a temporary value of the average cost of all agents able to accomplish that goal

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    """
    
    # Raise an error if goal_tree is empty (???)
    if goal_tree is None:
        raise ValueError("Tree is empty!")

    # For each goal find average cost among available agents and assign the temporary cost to the goal
    goals = _get_goals(goal_tree)

    for goal in goals:
        # Average
        costs = [x for x in goal.data.values()]
        # avg_cost = sum(costs) / len(costs)
        # goal.cost = avg_cost
        
        # Min
        goal.cost = min(costs)
        
        if verbose > 0:
            print(f"{goal.name}: {goal.cost}")
            for agent, cost in goal.data.items():
                print(f"  - {agent}: {cost}")





