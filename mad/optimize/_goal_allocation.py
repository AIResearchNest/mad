from mad.data_structures import GoalNode
from typing import Dict, List

def _suitable_agent(a: Dict) -> str:
    min_cost = list(a.values())[0]
    name = list(a.keys())[0]
    for key, value in a.items():
        if value < min_cost:
            min_cost = value
            name = key
    return name


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


def decision_algorithm(node: GoalNode) -> List[GoalNode]:
    if not node.get_children():
        return [node]

    subgoals_cost = sum((decision_algorithm(child) for child in node.get_children()), [])
    if min(subgoals_cost, node.cost) == subgoals_cost:
        return subgoals_cost
    else:
        return [node]


def initial_goal_allocation(goal_tree: GoalNode) -> Dict[str, List[str]]:
    if goal_tree is None:
        raise ValueError("Goal tree is empty.")

    goal_allocation: Dict[str, List[str]] = {"grace": [], "remus": [], "franklin": []}

    list_goals = decision_algorithm(goal_tree)
    for goal in list_goals:
        goal_allocation[goal.agent].append(goal.name)
    return goal_allocation


def main() -> None:
    G1 = GoalNode("G1", {"grace": 13, "franklin": 14, "remus": 12})
    G2 = GoalNode("G2", {"grace": 3, "franklin": 2, "remus": 5})
    G3 = GoalNode("G3", {"grace": 4, "franklin": 14, "remus": 15})

    G1.add_child(G2)
    G1.add_child(G3)
    print(initial_goal_allocation(G1))


if __name__ == "__main__":
    main()