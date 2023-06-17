from typing import Dict, List, Tuple
import random
from data_structures import GoalNode


def _random_cost(m: int, n: int) -> Dict[str, int]:
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
    min_cost = list(a.values())[0]
    name = list(a.keys())[0]
    for key, value in a.items():
        if value < min_cost:
            min_cost = value
            name = key
    return name


def _decision_algorithm(list_goal: List[GoalNode], i: int) -> Tuple[int, List[GoalNode]]:
    if not list_goal[i].get_children():
        return i + 1,list_goal
    
    subgoals_cost = sum(child.cost for child in list_goal[i].get_children())
    if min(subgoals_cost, list_goal[i].cost) == subgoals_cost:
        a = list_goal[i]
        list_goal.pop(0)
        for child in a.get_children():
            list_goal.append(child)
        return i,list_goal

    else:
        return i + 1,list_goal

def initial_goal_allocation(goal_tree: GoalNode) -> Dict[str, List[str]]:
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
    print("Goals List:\n")
    G1 = GoalNode("G1",_random_cost(10,20))
    G2 = GoalNode("G2",_random_cost(5,10))
    G3 = GoalNode("G3",_random_cost(5,10))
    G4 = GoalNode("G4",_random_cost(2,10))
    G5 = GoalNode("G5",_random_cost(2,10))
    G6 = GoalNode("G6",_random_cost(1,5))
    G7 = GoalNode("G7",_random_cost(1,5))
    G8 = GoalNode("G8",_random_cost(2,10))
    G9 = GoalNode("G9",_random_cost(2,10))
    
    print("\n\nGoals assigned to each agent:")
    #Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G4.add_child(G6)
    G4.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G9)

    print(initial_goal_allocation(G1))


if __name__ == "__main__":
    main()