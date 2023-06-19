from typing import Dict, List, Tuple
import sys 
import os
sys.path.append(os.path.abspath("data_structures"))
from _multi_agent_goal_nodes import GoalNode


def _suitable_agent(a: Dict) -> str:

    """
    Decides which agent will conduct the current goal based on cost

    Parameters
    ----------
    a : Dict[str: int]
        Dictionary containing the cost values for each agent

    Returns
    -------
    name: str
        Name of the agent with the minimum cost.
    """

    min_cost = list(a.values())[0]
    name = list(a.keys())[0]
    for key, value in a.items():
        if value < min_cost:
            min_cost = value
            name = key
    return name

    

def _decision_algorithm(list_goal: List[GoalNode], i: int) -> Tuple[int, List[GoalNode]]:
    
    """
    Decides whether to choose the current goal or its subgoals

    Parameters
    ----------
    list_goal: List[GoalNode]

    i: int
        the current index

    Returns
    -------
    
    i/i+1, list_goal: Tuple[int, List[GoalNode]]
        Returns the updated index and the modified list of goals needed to be conducted
    
    """

    if not list_goal[i].get_children():
        return i + 1,list_goal
    
    subgoals_cost = sum(child.cost for child in list_goal[i].get_children())
    if min(subgoals_cost, list_goal[i].cost) == subgoals_cost:
        a = list_goal[i]
        list_goal.pop(i)
        for child in a.get_children():
            list_goal.append(child)
        return i,list_goal

    else:
        return i + 1,list_goal
    
 
def initial_goal_allocation(goal_tree: GoalNode) -> Dict[str, List[str]]:
    
    """
    Optimizes allocation of goals to multiple agents

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Heirarichal Multi Agent Goal Tree 

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    
    """

    if goal_tree is None:
        raise ValueError("Goal tree is empty.")

    goal_allocation: Dict[str, List[str]] = {"grace": [], "remus": [], "franklin": []}
    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while i < len(list_goal):
        i, list_goal = _decision_algorithm(list_goal,i)

    for goal in list_goal:
        goal_allocation[goal.agent].append(goal.name)

    return goal_allocation


def main() -> None:
    pass

if __name__ == "__main__":
    main()