from typing import Dict, List, Tuple
import random
from data_structures import  GoalNode

def _random_cost(m: int, n: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        the starting point of the range
    n: int
        the ending point of the range

    """
    
    d = {}
    d["grace"] = random.randint(m,n)
    d["remus"] = random.randint(m,n)
    d["franklin"] = random.randint(m,n)
    print(d)
    return d

class GoalNode:
    def __init__(self, name: str, data: Dict) -> None:
        self.name = name
        self.data = data
        self.children: List[GoalNode] = []
        self.agent = _suitable_agent(data)
        self.cost = self.data[self.agent]

    def add_child(self, child: "GoalNode") -> None:
        self.children.append(child)

    def get_children(self) -> List["GoalNode"]:
        return self.children
    
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

    G1 = GoalNode("G1",_random_cost(20,40))
    G2 = GoalNode("G2",_random_cost(5,10))
    G3 = GoalNode("G3",_random_cost(5,10))
    G4 = GoalNode("G4",_random_cost(2,7))
    G5 = GoalNode("G5",_random_cost(2,7))
    G6 = GoalNode("G6",_random_cost(1,3))
    G7 = GoalNode("G7",_random_cost(1,3))
    G8 = GoalNode("G8",_random_cost(2,5))
    G9 = GoalNode("G9",_random_cost(2,5))
    G10 = GoalNode("G10",_random_cost(2,5))
    G11 = GoalNode("G11",_random_cost(2,5))

    #Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G4.add_child(G6)
    G4.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G9)
    G3.add_child(G10)
    G3.add_child(G11)

    print("\nTo complete the goal in the most optimized way, we can assign goals like this:\n")
    for agent in initial_goal_allocation(G1):
        print (agent, end = ": ")
        for i in initial_goal_allocation(G1)[agent]:
            print (i, end = " ")
        print("\n")

if __name__ == "__main__":
    main()