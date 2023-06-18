from typing import Dict, List
from collections import deque
import random
from mad.data_structures import GoalNode

"""
 -----------
Focus's on Agents assigment:
 1) The array Agents has been changed to agents_cost for clarity. Here cost of agent is the time an agent takes to complete the task.
 2)Agents are assigned to nodes based on the Shortest Task First (STF) algorithm. 
The algorithm considers the nodes as tasks and the `time_needed` as the time needed to complete the task. 
 Implemnetation:
 Each node/goal is assigned a random number of seconds required to complete the task from 1-10sec. Out of all avialable
 agents (g,r,f), agent that can complete the task faster is choosen. Tasks are resolved in ascending order such that task with minimum task time
 will be completed first. 
 -----------
 Functions specs:
 Random nodes () - function to randomly assign the different Goals/Nodes random time needed to complete the goal.
 Parameters:
 name : str
      Goal Name
      : GoalNode class
  data : dict
      Dictionary containing key as agent and value as planning cost  
------------
 To do:
 - add children
 - optimization
"""



agents_cost = [5, 2, 8]  # Agents cost values in accordance to agent_names[i]
agent_names = ['g', 'r', 'f']





def random_nodes() -> Dict[str, GoalNode]:
    nodes = {}

    shuffled_names = ['G2', 'G3', 'G4']
    random.shuffle(shuffled_names)  # Shuffle the node names

    for i in range(len(shuffled_names)):
        name = shuffled_names[i]
        data = {}
        time_needed = random.randint(1, 10)  # Generate random time_needed from 1 to 10 seconds
        node = GoalNode(name, data, time_needed)
        nodes[name] = node

    return nodes


if __name__ == "__main__":
    G1 = GoalNode("G1", {})  # parent
    nodes = random_nodes()

    # Sort nodes based on time_needed in ascending order
    sorted_nodes = sorted(nodes.values(), key=lambda x: x.time_needed)

    # Assign agents to nodes based on STF algorithm
    available_agents = list(agent_names)  # Create a copy of agent_names
    for node in sorted_nodes:
        fastest_agent = None
        fastest_time = float('inf')

        for agent_key in available_agents:
            agent_value = agents_cost[agent_names.index(agent_key)]
            if agent_value < fastest_time:
                fastest_agent = agent_key
                fastest_time = agent_value

        node.data = {fastest_agent: fastest_time}
        available_agents.remove(fastest_agent)

    # Set parent-child relationships
    G1.children.extend(sorted_nodes)
    for node in sorted_nodes:
        node.parents.append(G1)


    # Perform breadth-first search (BFS)
    queue = deque([G1])
    visited = set([G1])  # Track visited nodes
    while queue:
        current_node = queue.popleft()

        if current_node.data:
            agent_key = next(iter(current_node.data))
            agent_value = current_node.data[agent_key]
            print(f"{current_node.name} has been asignmed Agent {agent_key} with cost of {agent_value} as goal takes {current_node.time_needed} seconds")

        for child_node in current_node.children:
            if child_node not in visited:
                queue.append(child_node)
                visited.add(child_node)

