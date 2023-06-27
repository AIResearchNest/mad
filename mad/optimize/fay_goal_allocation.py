from typing import Dict, List, Tuple
from mad.data_structures.fay_multi_agent_goal_nodes import GoalNode, level_order_transversal

def fay_check_resources(goal: GoalNode, max_res: Dict[str, int]) -> bool:
    """
    Checks if an agent has enough resources to conduct a goal.

    Parameters
    ----------
    goal: GoalNode
        The current goal node

    max_res: Dict[str,int]  
        A dictionary with the agents as the keys and their corresponding resources as values

    Returns
    -------
        Returns True if the agent has enough resources, False otherwise.

    """

    return max_res[goal.agent] >= goal.cost


def fay_decision_algorithm(list_goal: List[GoalNode], i: int, max_res: Dict[str, int]) -> Tuple[int, List[GoalNode], Dict[str, int]]:
    """
    Decides whether to choose the current goal or its subgoals
    
    Parameters
    ----------
    list_goal : List[GoalNode]
        A list of the goals needed to be achieved
    i: int
        The current index
    max_res: Dict[str,int]
        A dictionary with the agents as the keys and their corresponding resources as values
    
    Returns
    -------
        Returns a tuple containing: the updated index, the modified list of goals, the updated dictionary of maximum resources

    """
    while not fay_check_resources(list_goal[i], max_res):
        list_goal[i].switch_agent() #switch to another agent to finish the goal
        if list_goal[i].agent is None: #if no agent can complete this
            a = list_goal.pop(i)  
            #if no agent can complete the goal and the goal has no child
            if not a.get_children():
                return i, [], max_res
            for child in a.get_children():
                list_goal.append(child)
            return i, list_goal, max_res
    print(list_goal[i].name + " can be completed by " + list_goal[i].agent + "\n")

    #if there is an agent can complete this goal
    if not list_goal[i].get_children(): #if this goal does not have child nodes
        max_res[list_goal[i].agent] -= list_goal[i].cost
        return i + 1, list_goal, max_res 
    
    d = max_res.copy()
    
    child_list: List[GoalNode] = []
    grand_child_list: List[GoalNode] = []

    subgoals_cost = 0

    for child in list_goal[i].get_children():
        while not fay_check_resources(child, d):
            child.switch_agent()  # switch to another agent
            if not child.agent:  # If no agent can finish this child goal
                a = child
                if not a.get_children():  # if this child node does not have children nodes
                    max_res[list_goal[i].agent] -= list_goal[i].cost
                    return i + 1, list_goal, max_res  # return the same list without any change
                
                e = []

                for grandchild in a.get_children():
                    if fay_check_resources(grandchild, d):
                        list_goal.append(grandchild)
                        e.append(grandchild)
                    else:
                        grandchild.switch_agent()
                        if grandchild.agent is None:  # if one grandchild could not complete, return the original goal list
                            return i, list_goal, max_res
                for i in e:
                    d[i.agent] -= i.cost  # subtract the cost from the resource
                    subgoals_cost += i.cost

        # if the child goal can be completed
        child_list.append(child)  # add the child goal to the child list
        d[child.agent] -= child.cost  # subtract the cost from the resource
        subgoals_cost += child.cost

    if min(subgoals_cost, list_goal[i].cost) == subgoals_cost:
        a = list_goal.pop(i)
        for child in child_list:
            list_goal.append(child)
        if grand_child_list != None:
            for grandchild in grand_child_list:
                list_goal.append(grandchild)
        return i, list_goal, max_res

    else:
        max_res[list_goal[i].agent] -= list_goal[i].cost
        return i + 1, list_goal, max_res
 
 
def fay_initial_goal_allocation(goal_tree: GoalNode, max_resources: List[int]) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    
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

    #Dictionary that contains the name and the max resource of each agent
    max_res: Dict[str,int] = {}
    
    #Name of the agents
    agents = ["grace", "remus", "franklin"]
    
    for i in range(len(agents)):
        max_res[agents[i]] = max_resources[i]

    goal_allocation: Dict[str, List[str]] = {"grace": [], "remus": [], "franklin": []}

    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while i < len(list_goal):
        i, list_goal, max_res = fay_decision_algorithm(list_goal,i, max_res)
        
        for j in list_goal:
            print(j.name, " ")
        print(max_res)
    print("\n\nThe "'most'" optimized goal tre: \n")
    level_order_transversal(goal_tree)

    for goal in list_goal:
        goal_allocation[goal.agent].append(goal.name)

    return goal_allocation, max_res

