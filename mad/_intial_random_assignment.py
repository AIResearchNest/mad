from typing import Dict, List
from collections import deque
import random
from mad.data_structures import GoalNode

"""
   Utilizing tri-Tree structure so G1 is parent, G2-G4 are children
  def random_nodes() - function to randomly assign the Agents to different Goals/Nodes
  Parameters
  ----------
  name : str
      Goal Name
      : GoalNode class
  data : dict
      Dictionary containing key as agent and value as planning cost  
     

  """
Agents = [5, 2, 8]  # Agents cost values in accordance to agent_names[i]
agent_names = ['g', 'r', 'f']


# function to randomly assign the Agents to different Goals/Nodes
def random_nodes() -> Dict[str, GoalNode]:
    nodes = {}
    shuffled_agents = list(zip(Agents, agent_names))
    random.shuffle(shuffled_agents)  # Shuffle the agents

    shuffled_names = ['G2', 'G3', 'G4']
    random.shuffle(shuffled_names)  # Shuffle the node names

    for i in range(len(shuffled_names)):
        name = shuffled_names[i]
        agent_value, agent_key = shuffled_agents[i]
        data = {agent_key: agent_value}
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


