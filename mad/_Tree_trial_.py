from typing import Dict, List
from collections import deque
import random


class GoalNode:
    """
    This class creates Multi Agent Goal Nodes

    Parameters
    ----------
    name : str
        Goal Name
    data : dict
        Dictionary containing key as agent and value as planning cost
    parents: List, default []
        List of Parent GoalNodes
    children: List, default []
        List of children GoalNodes
    """

    def __init__(self,
                 name: str,
                 data: Dict,
                 parents: List = [],
                 children: List = []) -> None:
        self.name = name
        self.data = data
        self.parents = parents
        self.children = children

#function to randomly assign the Agents to different Goals/Nodes
def random_nodes() -> Dict[str, GoalNode]:
    Agents = [5, 2, 8]
    agent_names = ['g', 'r', 'f']

    nodes = {}
    shuffled_names = ['G2', 'G3', 'G4']
    random.shuffle(shuffled_names)  # Shuffle the node names

    for i in range(len(shuffled_names)):
        name = shuffled_names[i]
        data = {agent_names[i]: Agents[i]}
        node = GoalNode(name, data)
        nodes[name] = node

    return nodes


if __name__ == "__main__":
    G1 = GoalNode("G1", {})  # parent
    nodes = random_nodes()

    # Set parent-child relationships
    G1.children.extend(nodes.values())
    for node in nodes.values():
        node.parents.append(G1)

    # Perform breadth-first search (BFS)
    queue = deque([G1])
    visited = set([G1])  # Track visited nodes
    while queue:
        current_node = queue.popleft()

        if current_node.data:
            agent_key = next(iter(current_node.data))
            agent_value = current_node.data[agent_key]
            print(f"{current_node.name} has Agent {agent_key} with cost of {agent_value}")

        for child_node in current_node.children:
            if child_node not in visited:
                queue.append(child_node)
                visited.add(child_node)

# function that  if called adds Add 3 more children to the leftmost/ available child everytime
# function that Assign those new nodes random g,r,f (in pair with their values respectively) too.

#optimize maybe by dijkstra's
